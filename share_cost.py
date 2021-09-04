class Trek:
    def __init__(self, users, amount=0):
        self.users_list = users
        self.owes_to = {}
        self.get_from = {}
        self.amount = {}

    def add_expenses(self, total_expense, persons_who_not_payed, person_who_payed):
        share = total_expense/(len(persons_who_not_payed) + 1)
        #print(share)

        self.amount[person_who_payed] = self.amount.get(person_who_payed, 0) - total_expense
        for user in persons_who_not_payed:
            self.get_from.setdefault(person_who_payed, {})[user] = self.get_from.get(person_who_payed, {}).get(user, 0) + share
            self.owes_to.setdefault(user, {})[person_who_payed] = self.get_from.get(user, {}).get(person_who_payed, 0) + share

    def get_summary(self, person):
        print(person + " amount " + str(self.amount.get(person, 0)))

        owe = self.owes_to.get(person)
        #print(owe)
        if owe:
            for key, value in owe.items():
                print(person + " owes to " + key + " amount " + str(value))
        
        _get = self.get_from.get(person)
        if _get:
            for key, value in _get.items():
                print(person + " get for " + key + " amount " + str(value))


if __name__ == "__main__":
    trek = Trek(['shaym', 'naveen', 'kartheek'])
    #shyam = Trek('shyam', 0)
    #naveen = Trek('naveen', 0)
    #kartheek = Trek('kartheek', 0)
#
    #total_expense = 10
    #share = total_expense/2
    #shaym.add_expenses(10, share, True, 'kartheek')
    #kartheek.add_expenses(10, share, False, 'shaym')


    trek.add_expenses(100, ['shaym', 'kartheek'], 'naveen')

    trek.add_expenses(300, ['kartheek'], 'shaym')
    #print(trek.owes_to)
    #print(trek.get_from)

    trek.get_summary('naveen')
    print("==========================")
    trek.get_summary('shaym')
    print("==========================")
    trek.get_summary('kartheek')