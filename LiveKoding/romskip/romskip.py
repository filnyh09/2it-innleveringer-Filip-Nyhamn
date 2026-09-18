def Lese_drivstoff():
    fil = open("drivstoff.txt", "r")
    drivstoff = int(fil.read())
    fil.close()
    return drivstoff

print("Drivstoff:", Lese_drivstoff(), "%")

def Vurdere_drivstoff(drivstoff):
    if drivstoff >= 50:
        return("Nok drivstoff")
    else:
        return("For lite drivstoff")

print(Vurdere_drivstoff(Lese_drivstoff()))
