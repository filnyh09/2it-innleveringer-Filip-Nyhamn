class Folk:
    def __init__(self, navn, alder, hoyde, yrke):
        self.navn = navn
        self.alder = alder
        self.hoyde = hoyde
        self.yrke = yrke

    def presenter(self):
        print("Hei jeg heter", self.navn)

    def  bliEldre(self):
        print("jeg var", self.alder, "år gamel")
        self.alder += 1
        print("nå er jeg", self.alder)

    def jobb(self):
        print("menneske jobber")

class laerer(Folk):
    def __init__(self, navn, alder, hoyde, yrke, elever):
        super().__init__(navn, alder, yrke, hoyde)

        self.elever = elever

    def retteProve(self):
        print(f"{self.navn} rettet prøve")

    def jobb(self):
        print("Læreren jobber")

class arbeidsledig(Folk):
    def jobb(self):
        print("arbeidsleding jobber ikke")

class Elev(Folk):
    def jobb(self):
        print("elev jobber")

ola = laerer("Ola", 14, "lærer", 187, 7)
kari = arbeidsledig("Kari", 15, 170, "Stein")
filip = Elev("Filip", 67, 200, "I kjeller")
maja = Folk("Masjascript", 69, 100, "Sjofor")

print(ola.alder)
print(kari.alder)
print(filip.alder)
print(maja.alder)

ola.presenter()

ola.bliEldre()

ola.retteProve()

ola.jobb()
kari.jobb()
filip.jobb()
maja.jobb()

arbeidere = [ola,kari,filip,maja]

for arbeider in arbeidere:
    arbeider.jobb()