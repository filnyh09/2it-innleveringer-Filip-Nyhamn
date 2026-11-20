utstyr = []
utlaan = []

def legTilUtstyr():
    utstyr.append(input("\nNytt utstyr: "))
    utlaan.append(None)


legTilUtstyr()
legTilUtstyr()

for listenom, ting in enumerate(utstyr):
    print(f"\nutstyr: {ting}")
    if utlaan[listenom] != None:
        print(f"status: {utlaan}")