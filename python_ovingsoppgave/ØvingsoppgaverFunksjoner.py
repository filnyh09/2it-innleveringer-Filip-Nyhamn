def romhilsen():
    print("Velkommen til romstasjonen!")
    print("Gjør deg klar for avreise.")

romhilsen()
romhilsen()
romhilsen()


def vis_astronaut(astronaut):
    print(f"Astronaut: {astronaut}")
    print(f"{astronaut} er klar for oppdrag!")

vis_astronaut("Nora")
vis_astronaut("Elias")
vis_astronaut("Sara")


def vis_maane(navn, forelderPlanet):
    print(f"Måne: {navn}")
    print(f"Planet: {forelderPlanet}")

vis_maane("Europa", "Jupiter")
vis_maane("Titan", "Saturn")
vis_maane("Phobos", "Mars")