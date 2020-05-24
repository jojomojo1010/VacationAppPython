from person import *

class Debt():

    def __init__(self, creditor, debitor, balance_tuple, balance):
        self.creditor = creditor
        self.debitor = debitor
        self.balance_tuple = balance_tuple
        self.balance = balance
    
    def get_balance_tuple(self):
        return self.balance_tuple
    def get_balance(self):
        return self.balance
    def get_creditor(self):
        return self.creditor
    def get_debitor(self):
        return self.debitor
    def add_balance(self, balance):
        self.balance += balance


debt_list = []
for x in person_list:
    debitor_list = [k for k in person_list if k != x]
    for y in debitor_list:
        debt_list.append(Debt(x.get_name(), y.get_name(), (x.get_number(), y.get_number()),0))






        
