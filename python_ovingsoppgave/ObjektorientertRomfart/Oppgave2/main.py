# ------------------fra opgave 1-------
class romfartooy:
    def __init__(self, navn, hastighet, drivstoffmengde):
        self.navn = navn
        self.hastighet = hastighet
        self.drivstoffmengde = drivstoffmengde

    def presenter(self):
        return f"\n navn: {self.navn} \n hastighet: {self.hastighet} \n drivstoffmengde: {self.drivstoffmengde} \n"

    def ookeHastigheten(self):
        if (self.drivstoffmengde - 1) >= 0:
            self.hastighet += 1
            self.drivstoffmengde -= 1

# -------------------------------------

class romkargoskip(romfartooy):
    def __init__(self, navn, hastighet, drivstoffmengde, lagerplass):
        super().__init__(navn, hastighet, drivstoffmengde)

        self.lagerplass = lagerplass

class rompasasjerskip(romfartooy):
    def __init__(self, navn, hastighet, drivstoffmengde, oksygen, pasasjerer):
        super().__init__(navn, hastighet, drivstoffmengde)

        self.oksygen = oksygen
        self.pasasjerer = pasasjerer

