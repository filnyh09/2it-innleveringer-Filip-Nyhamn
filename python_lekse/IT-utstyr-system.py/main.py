utstyr = []
utlaan = []

def legTilUtstyr():
    utstyr.append(input("\nNytt utstyr: "))
    utlaan.append(None)

def loonUt():
    for listenom, ting in enumerate(utstyr):
        print(f"{listenom + 1}. {ting}")
    input("hvilke utstyr vil du låne ut: ")


legTilUtstyr()
legTilUtstyr()


loonUt()


for listenom, ting in enumerate(utstyr):
    print(f"utstyr: {ting}")
    if utlaan[listenom] != None:
        print(f"status: {utlaan}")