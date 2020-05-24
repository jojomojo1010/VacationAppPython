class Person():

    def __init__(self,name,number):
        self.name = name
        self.number = number

    def get_name(self):
        return self.name
    def get_number(self):
        return self.number

person_list= []
names_input = ["Kevin","Mai","Joey","Frank"]
for x, y in zip(names_input, range(len(names_input))):
    person_list.append(Person(x,y))