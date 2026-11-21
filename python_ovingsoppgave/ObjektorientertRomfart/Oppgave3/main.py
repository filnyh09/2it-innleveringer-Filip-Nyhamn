# ai har blit brukt for ideeskaping og opklaring

class enhet:
    def __init__(self, navn, status):
        self.navn = navn
        self.status = status

class SveiseRobot(enhet):
    def __init__(self, navn, status):
        super().__init__(navn, status)

    def utfoorOppdrag():
        return "Reparerer skader på romstasjonen."