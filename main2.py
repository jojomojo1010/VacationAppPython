from debt import *
from person import *
from activity import *

for x in activity_list:
    x.entry()

def show_debt():
    balance_diff = 0
    for x, a in zip(debt_list,range(len(debt_list))):
        for y in debt_list[a:]:
            if x.get_creditor() == y.get_debitor() and y.get_creditor() == x.get_debitor():
                if x.get_balance() > y.get_balance():
                    balance_diff = x.get_balance() - y.get_balance()
                    print(f"{x.get_debitor()} schuldet {x.get_creditor()} {balance_diff}€")
                    balance_diff = 0
                if x.get_balance() < y.get_balance():
                    balance_diff = y.get_balance() - x.get_balance()
                    print(f"{y.get_debitor()} schuldet {y.get_creditor()} {balance_diff}€")
                    balance_diff = 0

show_debt()

for i in range(len(debt_list)):
    print(debt_list[i].get_balance_tuple())
    print(debt_list[i].get_balance())
    