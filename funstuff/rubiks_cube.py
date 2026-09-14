class cube:
    def __init__(self):
        self.face = {
            "Top": [
                ["⬜", "⬜", "⬜"], 
                ["⬜", "⬜", "⬜"], 
                ["⬜", "⬜", "⬜"]
                ],
            "Bottom": [
                ["🟨", "🟨", "🟨"], 
                ["🟨", "🟨", "🟨"], 
                ["🟨", "🟨", "🟨"]
                ],
            "Left": [
                ["🟩", "🟩", "🟩"], 
                ["🟩", "🟩", "🟩"], 
                ["🟩", "🟩", "🟩"]
                ],
            "Right": [
                ["🟦", "🟦", "🟦"], 
                ["🟦", "🟦", "🟦"], 
                ["🟦", "🟦", "🟦"]
                ],
            "Front": [
                ["🟥", "🟥", "🟥"], 
                ["🟥", "🟥", "🟥"], 
                ["🟥", "🟥", "🟥"]
                ]
                ,
            "Back": [
                ["🟧", "🟧", "🟧"], 
                ["🟧", "🟧", "🟧"], 
                ["🟧", "🟧", "🟧"]
                ]
                ,
            "Blank": [
                ["⬛", "⬛", "⬛"], 
                ["⬛", "⬛", "⬛"], 
                ["⬛", "⬛", "⬛"]
                ]
        }

    def showFace(self, *faces):
        for face in faces:
            if face not in self.face:
                if face not in self.face:
                    print(f"Unknown face: {face}")
                    return
        for rows in zip(*(self.face[face] for face in faces)):
            print("".join("".join(row) for row in rows))

    def showCube(self):
        self.showFace("Blank", "Top", "Blank")
        self.showFace("Left", "Front", "Right")
        self.showFace("Blank", "Bottom", "Blank")
        self.showFace("Blank", "Back", "Blank")

    def getPoint(self, face, row, column):
        return self.face[face][row][column]

    def rotateCube(self, face):
        temp = self.face
        print(self.getPoint("Top", 1, 2))


bob = cube()

bob.rotateCube("Top")
bob.showCube()