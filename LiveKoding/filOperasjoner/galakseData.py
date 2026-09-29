try:
    with open("LiveKoding/filOperasjoner/galakse.txt", "r") as fil:
        print(fil.read)
except FileNotFoundError:
    print("Filen finnes ikke")

try:
    planetNommer = int(input("Velg planetnomner"))
except ValueError:
    print("Du må skrive inn ett gylding tall")
else:
    print(planetNommer)