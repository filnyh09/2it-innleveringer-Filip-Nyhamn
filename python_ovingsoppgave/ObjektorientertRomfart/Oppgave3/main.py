# ai har blit brukt for ideeskaping og opklaring

class enhet:
    def __init__(self, navn, status):
        self.navn = navn
        self.status = status


class SveiseRobot(enhet):
    def __init__(self, navn, status):
        super().__init__(navn, status)

    def utfoorOppdrag(self):
        if self.status
            return "Reparerer skader på romstasjonen."
        else:
            return "Må vere aktive for å utføre oppdrag"

class RengjøringsEnhet(enhet):
    def __init__(self, navn, status):
        super().__init__(navn, status)

    def utfoorOppdrag(self):
        return "Tømmer luftfilter."

class Datamaskin(enhet):
    def __init__(self, navn, status):
        super().__init__(navn, status)

    def utfoorOppdrag(self):
        return "Behandler teleskopdata."


robin = SveiseRobot("Robin", True)