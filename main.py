class Unternehmungen():

    def __init__(self,event,kosten):
        self.event = event
        self.kosten = kosten

class Personen():

    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def set_position(self,position):
        self.position = position

    prop = property(get_position,set_position)

    def buchung(self,kosten,*args):
        anzahl = len(args)+1
        anteil = kosten/anzahl
        for x in args:
            if x.prop > self.prop:
                bilanzliste[self.prop][x.prop-1] -= anteil
            if x.prop < self.prop:
                bilanzliste[self.prop][x.prop] -= anteil


    def schulden(self):
        for x in range(len(ppl)):
            if self.prop == x:
                continue
            if self.prop > x:
                if bilanzliste[self.prop][x] < bilanzliste[x][self.prop-1]:
                    print("{} schuldet dir {} Geldeinheiten".format(ppl[x].get_name(),abs(bilanzliste[self.prop][x] - bilanzliste[x][self.prop-1])))
                if bilanzliste[self.prop][x] > bilanzliste[x][self.prop-1]:
                    print("Du schuldest {} {} Geldeinheiten".format(ppl[x].get_name(),abs(bilanzliste[x][self.prop-1]-bilanzliste[self.prop][x])))
            if self.prop < x:
                if bilanzliste[self.prop][x-1] < bilanzliste[x][self.prop]:
                    print("{} schuldet dir {} Geldeinheiten".format(ppl[x].get_name(),abs(bilanzliste[self.prop][x-1] - bilanzliste[x][self.prop])))
                if bilanzliste[self.prop][x-1] > bilanzliste[x][self.prop]:
                    print("Du schuldest {} {} Geldeinheiten".format(ppl[x].get_name(),abs(bilanzliste[x][self.prop]-bilanzliste[self.prop][x-1])))

    
ppl = []
kevin = Personen("Kevin",0)
mai = Personen("Mai",1)
joey = Personen("Joey",2)
dirk = Personen("Dirk",3)
ppl.append(kevin)
ppl.append(mai)
ppl.append(joey)
ppl.append(dirk)

bilanzliste=[]
for i in ppl:
    bilanzen=[0]*(len(ppl)-1)
    bilanzliste.append(bilanzen)

kevin.buchung( 200, mai, joey, dirk)
joey.buchung(400, mai, kevin, dirk)
joey.buchung(150, kevin, mai, dirk)
mai.buchung(70, kevin, joey, dirk)
kevin.buchung(180, joey, dirk)

print(kevin.schulden())
print(kevin.prop)
print(bilanzliste)

