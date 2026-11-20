import json

utstyr = []
utlaan = []

def visStatus():
    for listenom, ting in enumerate(utstyr):
        print(f"utstyr: {ting}")
        if utlaan[listenom] != None:
            print(f"status: {utlaan[listenom]}")

def legTilUtstyr():
    utstyr.append(str(input("Nytt utstyr: ")))
    utlaan.append(None)

def visUtstyr():
    for listenom, ting in enumerate(utstyr):
            print(f"{listenom +1}. {ting}")

def laanUt():
    visUtstyr()
    try:
        ting = int(input("hvilke utstyr vil du låne ut: "))
    except ValueError:
        print("!Du kan bare skrive nommer!")
        return
    person = str(input("hvem vil du låne det ut til: "))
    try:
        utlaan[ting -1] = person
    except IndexError:
        print("!du kan bare velge utstyr som er i listen!")
        return

def leverUtstyr():
    visUtstyr()
    try:
        ting = int(input("hvilke utstyr vil du levere tilbake: "))
        utlaan[ting -1] = None
    except IndexError:
        print("!du kan bare velge utstyr som er i listen!")
        return

def write():
    data = {"utstyr": utstyr, "utlaan": utlaan}
    with open("python_lekse\IT-utstyr-system\data.json", "w") as file:
        json.dump(data, file, indent=4)

while True:
    command = input(">")
    flexcmd = command.strip().lower()

    if flexcmd == "exit":
        break

    if flexcmd == "status":
        visStatus()

    if flexcmd == "+utstyr" or flexcmd == "utstyr+":
        legTilUtstyr()

    if flexcmd == "lånut":
        laanUt()

    if flexcmd == "lever":
        leverUtstyr()

    if flexcmd == "lagre":
        write()

    if flexcmd not in ["exit", "status", "+utstyr", "utstyr+", "lånut", "lever", "lagre"]:
        print("Not a command :(")