def beregn_avstand(fart, timer):
    if timer < 0:
        raise ValueError("Tid kan ikke vere negativ")
    return fart * timer

def beregn_drivstoff(avstand, timer):
    return avstand * timer

def velkommen(navn):
    return(f"velkommen om bord {navn}")