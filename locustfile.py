from locust import User, task, between
from twisted.internet import defer, reactor
from twisted.internet.task import deferLater
from redis import StrictRedis
import argparse
import random
import requests
import json
import pickle
import time
import sys
from locust.contrib.fasthttp import FastHttpUser
import gevent
from copy import deepcopy

MATCH_ID = 'pslt20_2021_g028'  # match_key
CONTEST_ID = 1  # for free contest it's 10120

save_team_count = 0
register_contest_count = 0

connection = StrictRedis(host='localhost', port=6379, db=2)
users = set()
registered_players = set()
count = 0

user_count=0
TEAM_PLAYERS = {}
TEAM = {'spent_credits': None, 'bow_count': 4, 'ar_count': 2,
        'wkt_count': 1, 'b_count': None, 'captain': None, 'team_b': None,
        'vice_captain': None, 'team_a': None, 'bat_count': 4,
        'team_name': 'Team1', 'players': None, 'a_count': None}



url_session = "https://staging-new-nucleus-api.indianrummynetwork.com/service/1/authentication/system_login"
url_save = "https://games-staging-new.indianfantasynetwork.com/api/game/team/save?target=cric"
url_register_contest = "https://games-staging-new.indianfantasynetwork.com/api/game/contest/register?target=cric"

#url_save =  "http://localhost:12432/api/game/team/save?target=cric"
#url_register_contest = "http://localhost:12436/api/game/contest/register?target=cric"

def get_registered_players():
    global registered_players

    if not registered_players:
        r = StrictRedis(host='127.0.0.1', port=6379, db=2)
        players = r.smembers("registration" + ':' + str(CONTEST_ID) + ':' + str(MATCH_ID))
        for i in players:
            i = i.decode('utf-8')
            i_parts = i.split(':')
            registered_players.add(int(i_parts[1]))
    return registered_players

def pick_users():
    global users

    if not users:
        r = StrictRedis(host='127.0.0.1', port=6379, db=2)
        user = r.smembers('users_set')
        for i in user:
            user_id = i.decode('utf-8')
            users.add(user_id)

        users = users - registered_players

    return users.pop()


def get_session_id(user_id):
    global user_count
    global url_session

    user_count=user_count + 1 
    
    url = url_session
    payload = {"id":"1","jsonrpc":"2.0","method":"authentication.proxy_login","params":["f6ZO7j11myA8PA3M",None, None, int(user_id)]}
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload))
    res = json.loads(response.text)
    
    session_id = res['result']['session_id']
    print(f"USER COUNT ==> {user_count}, SESSION ID: {session_id}")
    #print(f"USER COUNT: === {user_count} === USER ID: {user_id} SESSION ID: {session_id}")

    return session_id


def update_match_players():
    global TEAM
    global TEAM_PLAYERS
    global count

    match = connection.hget('matches', MATCH_ID)

    match = pickle.loads(match)

    if not match:
        sys.exit(0)

    for team_x in ['team_a', 'team_b']:
        team = match.get(team_x)
        TEAM[team_x] = team.get('key')
        TEAM_PLAYERS.update(team.get('players', {}))

def create_team():
    keepers = []
    batsmen = []
    allrounder = []
    bowler = []
    for player, info in TEAM_PLAYERS.items():
        if info['seasonal_role'] == 'bowler':
            bowler.append(player)
        elif info['seasonal_role'] == 'batsman':
            batsmen.append(player)
        elif info['seasonal_role'] == 'allrounder':
            allrounder.append(player)
        elif info['seasonal_role'] == 'keeper':
            keepers.append(player)

    while True:
        players = []
        credits = 0
        team_a = 0
        team_b = 0
        players.append(random.choice(keepers))
        players.extend(random.sample(batsmen, 4))
        players.extend(random.sample(allrounder, 2))
        players.extend(random.sample(bowler, 4))

        for player in players:
            credits += TEAM_PLAYERS[player]['credit_value']
            if TEAM_PLAYERS[player]['team_key'] == 'a':
                team_a += 1
            else:
                team_b += 1

        if credits <= 100 and team_a < 8 and team_b < 8:
            TEAM['a_count'] = team_a
            TEAM['b_count'] = team_b
            TEAM['spent_credits'] = credits
            TEAM['captain'] = random.choice(players)
            while True:
                TEAM['vice_captain'] = random.choice(players)
                if TEAM['vice_captain'] != TEAM['captain']:
                    break
            TEAM['players'] = players
            break
    TEAM['team_name']='TEAM1'

def save_team(session_id):
    global url_save

    create_team()
    print("==== Save Team ===== %s", TEAM)

    #players = deepcopy(TEAM['players'])
    #TEAM['captain'] = random.choice(players)
    #players.remove(TEAM['captain'])
    #TEAM['vice_captain'] = random.choice(players)

    data = {'team': TEAM, 'session_id': session_id,
            'match_id': MATCH_ID, "api_key": "f6ZO7j11myA8PA3M"}

    headers = {'Content-Type': 'application/json'}
    response1 = requests.request("POST", url_save,
                          headers=headers, data=json.dumps(data))

    if response1.status_code == 200:
        resp1 = json.loads(response1.text) if response1.text else {}
    else:
        resp1 = {}
    if resp1.get('status') == 'success':
        hkey_name = 'success'
    else:
        hkey_name = str(response1.text) + '__' + str(response1.status_code)

    event_key = "game_load_test" + ":" + "save_team"
    connection.hincrby(event_key, hkey_name, 1)
    #print('RESPONSE of the *** SAVE TEAM *** %s %s, %s'%(session_id, response1.status_code, time.time()))
    
    return resp1
    

def register_contest(session_id, user_id):
    global url_register_contest

    data = {'match_id': MATCH_ID, 'team_id': 1, "user_id": int(user_id),
            "session_id_register": session_id, "contest_id": CONTEST_ID ,
            "api_key": "f6ZO7j11myA8PA3M", "server_id": "fantasy-server:klyloadtest:12436"}

    headers = {'Content-Type': 'application/json'}
    response2 = requests.request("POST", url_register_contest,
                          headers=headers, data=json.dumps(data))
    
    if response2.status_code == 200:
        resp2 = json.loads(response2.text) if response2.text else {}
    else:
        resp2 = {}
    if resp2.get('status') == 'success':
        hkey_name = 'success'
    else:
        hkey_name = str(response2.text) + '__' + str(response2.status_code)

    event_key = "game_load_test" + ":" + "register_contest"
    connection.hincrby(event_key, hkey_name, 1)
    print('RESPONSE of the ### CONTEST REGISTER ### %s %s, %s, %s'%(session_id, response2.text, response2.status_code, time.time()))

    return resp2


def make_request(session_id, user_id):
    update_match_players()
    save_team(session_id)
    register_contest(session_id, user_id)
    


class User(FastHttpUser):
    global user_count
    #wait_time = between(2, 5)
    port_id = ['12433','12434','12435']
    host = "https://games-staging-new.indianfantasynetwork.com"
    #host = "http://localhost:" + random.choice(port_id)

    min_wait = 10000
    max_wait = 15000

    def __init__(self, parent):
        super(User, self).__init__(parent)
        get_registered_players()
        self.user_id = pick_users()
        self.session_id = get_session_id(self.user_id)
        if self.session_id:
            #update_match_players()
            gevent.spawn(make_request, self.session_id, self.user_id)

            #before = time.time()
            #save_response = save_team(self.session_id)
            #after = time.time()
            #if save_response.get('status') == 'success':
            #    print("======================================================================================================== SAVE TEAM of %s response time %.4f sec"%(self.session_id, after-before))

            #before = time.time()
            #register_response = register_contest(self.session_id)
            #after = time.time()
            #if register_response.get('status') == 'success':
            #    print("====================================================================================================== REGISTER CONTEST %s response time %.4f sec"%(self.session_id, after-before))
            pass

    @task(1)
    def save_team(self):
        pass

    """
    @task(1)
    def save_and_register(self):
        global save_team_count, register_contest_count

        ## Save Team ##
        #create_team()
        #print("==== Save Team ===== %s", TEAM)
        #players = deepcopy(TEAM['players'])
        #TEAM['captain'] = random.choice(players)
        #players.remove(TEAM['captain'])
        #TEAM['vice_captain'] = random.choice(players)

        before = time.time()
        data = {'team': TEAM, 'session_id': self.session_id,
                'match_id': MATCH_ID, "api_key": "f6ZO7j11myA8PA3M"}
        headers = {'Content-Type': 'application/json'}
        response1 = self.client.post("/api/game/team/save?target=cric", headers=headers, data=json.dumps(data))
        after = time.time()

        save_team_count += 1
        if response1.status_code == 200:
            resp1 = json.loads(response1.text) if response1.text else {}
        else:
            resp1 = {}

        if resp1.get('status') == 'success':
            print("======================================================================================================== SAVE TEAM of %s response time %.4f sec"%(self.session_id, after-before))
            hkey_name = 'success'
        else:
            hkey_name = str(response1.text) + '__' + str(response1.status_code)

        event_key = "game_load_test" + ":" + "save_team"                            
        connection.hincrby(event_key, hkey_name, 1)
        #print('SAVE TEAM COUNT ===> %s'%(save_team_count))
        

        #gevent.sleep(0.5)


        ## Contest Register ##
        before = time.time()
        data = {'match_id': MATCH_ID, 'team_id': 1,
                'session_id': self.session_id, "contest_id": CONTEST_ID , "api_key": "f6ZO7j11myA8PA3M"}
        headers = {'Content-Type': 'application/json'}
        response2 = self.client.post("/api/game/contest/register?server_id=fantasy_gs:10.49.2.192:12433&target=cric", headers=headers, data=json.dumps(data))
        after = time.time()

        register_contest_count += 1
        if response2.status_code == 200:
            resp2 = json.loads(response2.text) if response2.text else {}
        else:
            resp2 = {}

        if resp2.get('status') == 'success':
            print("====================================================================================================== REGISTER CONTEST %s response time %.4f sec"%(self.session_id, after-before))
            hkey_name = 'success'
        else:
            hkey_name = str(response2.text) + '__' + str(response2.status_code)

        event_key = "game_load_test" + ":" + "register_contest"
        connection.hincrby(event_key, hkey_name, 1)
        #print('REGISTER CONTEST COUNT =========> %s'%(register_contest_count))



    @task(1)
    def get_player(self):

        headers = {'Content-Type': 'application/json'}
        r1 = self.client.post("/api/game/player/contests", headers=headers,
                              data=json.dumps({"session_id": self.session_id, "api_key": "f6ZO7j11myA8PA3M"}))
        
        print("=== RESPONSE of Get Player Contests === %s"%(r1.status_code))

    @task(1)
    def update(self):
        pass

        #headers = {'Content-Type': 'application/json'}
        #r1 = self.client.post("/api/game/team/update", headers=headers,
        #        data=json.dumps({"session_id": self.session_id, "match_id":MATCH_ID,"team":TEAM,"team_id":1, "api_key": "f6ZO7j11myA8PA3M"}))
        #
        #print("=== Response of Update Team === %s"%(r1.status_code))

    @task(1)
    def get_team(self):

        headers = {'Content-Type': 'application/json'}
        r1 = self.client.post("/api/game/team/get", headers=headers,
                data=json.dumps({"session_id": self.session_id,"match_id":MATCH_ID, "api_key": "f6ZO7j11myA8PA3M"}))
        
        print("=== Response of Team GET === %s"%(r1.status_code))

    @task(1)
    def contests(self):

        headers = {'Content-Type': 'application/json'}
        r1 = self.client.post("/api/game/player/teams/contests", headers=headers,
                data=json.dumps({"session_id": self.session_id,"match_id":MATCH_ID, "api_key": "f6ZO7j11myA8PA3M"}))
        
        print("=== Response of Player Team Contests === %s"%(r1.status_code))
    """
