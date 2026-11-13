class romfartooy:
    def __init__(self, navn, hastighet, drivstoffmengde):
        self.navn = navn
        self.hastighet = hastighet
        self.drivstoffmengde = drivstoffmengde

    def presenter(self):
        return f"\n navn: {self.navn} \n hastighet: {self.hastighet} \n drivstoffmengde: {self.drivstoffmengde}"

    def ookeHastigheten(self):
        if (self.drivstoffmengde - 1) >= 0:
            self.hastighet += 1
            self.drivstoffmengde -= 1

skip1 = romfartooy("Martin", 6, 27)
skip2 = romfartooy("Bannan", 8, 2)
skip3 = romfartooy("JanOlav", 5463, 67)

print(skip1.presenter())