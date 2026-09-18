def les_oksygen():
    fil = open("oksygen.txt", "r")
    oksygennivaaet = int(fil.read())
    fil.close
    return oksygennivaaet

def vurder_oksygen(prosent):
    if prosent >= 50:
        return("Oksygennivaa OK")
    else:
        return("Lavt oksygennivaa")

print(f"Oksygen: {les_oksygen()}%")
print(vurder_oksygen(les_oksygen()))
