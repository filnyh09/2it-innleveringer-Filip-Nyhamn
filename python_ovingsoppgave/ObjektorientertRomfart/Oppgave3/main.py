# ai har blit brukt for ideeskaping og opklaring

class enhet:
    def __init__(self, navn, status):
        self.navn = navn
        self.status = status


class SveiseRobot(enhet):
    def __init__(self, navn, status):
        super().__init__(navn, status)

    def utfoorOppdrag(self):
        if self.status:
            return "Reparerer skader på romstasjonen."
        else:
            return "Må vere aktive for å utføre oppdrag"

class RengjøringsEnhet(enhet):
    def __init__(self, navn, status):
        super().__init__(navn, status)

    def utfoorOppdrag(self):
        if self.status:
            return "Tømmer luftfilter."
        else:
            return "Må vere aktive for å utføre oppdrag"

class Datamaskin(enhet):
    def __init__(self, navn, status):
        super().__init__(navn, status)

    def utfoorOppdrag(self):
        if self.status:
            return "Behandler teleskopdata."
        else:
            return "Må vere aktive for å utføre oppdrag"


robin = SveiseRobot("Robin", True)
bob = RengjøringsEnhet("Bob", True)
martin = RengjøringsEnhet("Martin", True)
tenker = Datamaskin("melvin", True)
grubler = Datamaskin("Hans", False)

enhetsliste = [robin, bob, martin, tenker, grubler]