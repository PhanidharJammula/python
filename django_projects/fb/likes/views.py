from django.http import HttpResponse
import json
from urllib.request import urlopen
from django.shortcuts import render
from django.http.response import JsonResponse

def index(request):
    return HttpResponse("hello world!")


def get_page_data(request):
    #fb_graph_url = 'https://graph.facebook.com/v3.3/283151195924829_286055902301025?access_token=EAAFJnDR9iZBYBAF4G9bSK2Qc8fPEeqDKwjJu14LCuAjYDZAKOY9XT8FzqSKkrbZBTPzZA3GvyxY3hL1JLZAuAQ5JE5WGQs5rdMOB8pHZCZBZAsFrKEqeDdOAXAMzJZCKK99NPdq9weiSn6AxJNxFpueAdyT7hagez6pwy0dmlLIqufgEeiA18ymUtVcN5MLH5rSlWEDOU7vrCeqE5rvZBSEBMNwJr6Q5RjD0gmq9lsevn5vVyIUKt3ZB6ct&debug=all&fields=shares,likes.summary(true),comments.summary(true)&format=json&method=get&pretty=0'
    fb_graph_url = 'https://graph.facebook.com/v3.3/283151195924829_286055902301025?access_token=EAAFJnDR9iZBYBAFoobiBV0Ya62S0zseJiem9N9lXBzpcMlZAXxNlYDLZC2Xx264tlVDm6JkMK00f1dmSOwroYZAuiWheNSKaV9AjjnQCcn4LLLz1miwEcyNzgraKdCOOAgRSVclNMT4s9AQ7Nz1ENK4fGuQpXxrHVUK4a4Woqk2pDqY1ZA1mRyLZCRENAQde4ZB6DyZCqTrNjgZDZD&debug=all&fields=likes.summary(true)&format=json&method=get&pretty=0&suppress_'
    #283151195924829_286055902301025?fields=likes.summary(true)&access_token=user-access-token
    try:
        api_response = urlopen(fb_graph_url)
        api_response = api_response.read().decode('utf-8')

        try:
            data = json.loads(api_response)
            return JsonResponse({'result':data})

        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError as e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason
