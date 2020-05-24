from person import *
from debt import *

class Activity():

    def __init__(self, title, cost, payer, attendee_list):
        self.title = title
        self.cost = cost
        self.payer = payer
        self.attendee_list = attendee_list

    def get_title(self):
        return self.title
    def get_cost(self):
        return self.cost
    def get_payer(self):
        return self.payer
    def get_attendee_list(self):
        return self.attendee_list


    
    
    def entry(self):
        share = self.cost/(len(self.attendee_list) +1)
        for x in range(len(person_list)):
            if self.payer == person_list[x].get_name():

                for a in range(len(self.attendee_list)):
                    for y in range(len(person_list)):
                        if self.attendee_list[a] == person_list[y].get_name():

                            for b in range(len(debt_list)):
                                if debt_list[b].get_balance_tuple() == (person_list[x].get_number(), person_list[y].get_number()):
                                    debt_list[b].add_balance(share)
                                    print(f"{person_list[y].get_name()} hat bei {person_list[x].get_name()} {share}€ Miese gemacht für {self.title}")


activity_list = []
activity_input = [("Flight",400,"Joey",("Kevin","Mai")), ("Hotel",200,"Kevin",("Mai","Joey")), ("Rundfahrt",150,"Joey",("Kevin","Mai")),("Essen",180,"Mai",("Kevin","Frank"))]
for x in range(len(activity_input)):
    activity_list.append(Activity(activity_input[x][0], activity_input[x][1],activity_input[x][2],activity_input[x][3]))

