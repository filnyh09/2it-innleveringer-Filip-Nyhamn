class romfartooy:
    def __init__(self, navn, hastighet, drivstoffmengde):
        self.navn = navn
        self.hastighet = hastighet
        self.drivstoffmengde = drivstoffmengde

    def presenter(self):
        return f"navn: {self.navn} \n hastighet: {self.hastighet} \n drivstoffmengde: {self.drivstoffmengde}"

    def ookeHastigheten(self):
        if (self.drivstoffmengde - 1) >= 0:
            self.hastighet += 1
            self.drivstoffmengde -= 1
