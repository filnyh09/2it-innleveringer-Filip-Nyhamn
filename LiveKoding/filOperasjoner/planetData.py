
#fil = open("LiveKoding/filOperasjoner/planeter.txt", "a")
#fil.write("Mars \n")
#fil.close

#with open("LiveKoding/filOperasjoner/planeter.txt", "r") as fil:
#    for linje in fil:
#        print(linje.strip)

planet = input("\nskriv inn en planet ")
antalMaaner = int(input("hvor mange måner har den "))

with open("LiveKoding/filOperasjoner/planeter.txt", "w") as fil:
    fil.write(f"{planet}\n{antalMaaner}\n")

with open("LiveKoding/filOperasjoner/planeter.txt", "r") as fil:
    print()
    print(fil.read())

print("Planeten ble lagret")