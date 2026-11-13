class romfartooy:
    def __init__(self, navn, hastighet, drivstoffmengde):
        self.navn = navn
        self.hastighet = hastighet
        self.drivstoffmengde = drivstoffmengde

    def presenter(self):
        return f"navn: {self.navn} \n hastighet: {self.hastighet} \n drivstoffmengde: {self.drivstoffmengde}"