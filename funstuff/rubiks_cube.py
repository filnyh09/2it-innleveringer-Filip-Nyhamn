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
        self.showBack()

    def showBack(self):
        for row in reversed(self.face["Back"]):
            print("⬛⬛⬛" + "".join(reversed(row)) + "⬛⬛⬛")

    def rotateCube(self, face, clockwise=True):
        if face not in self.face or face == "Blank":
            print(f"Unknown turn face: {face}")
            return

        directions = {
            "Top": ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
            "Bottom": ((0, 1, 0), (1, 0, 0), (0, 0, -1)),
            "Left": ((-1, 0, 0), (0, 0, 1), (0, 1, 0)),
            "Right": ((1, 0, 0), (0, 0, -1), (0, 1, 0)),
            "Front": ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
            "Back": ((0, 0, -1), (-1, 0, 0), (0, 1, 0))
        }
        normals = {name: values[0] for name, values in directions.items()}
        normal_to_face = {normal: name for name, normal in normals.items()}
        axis, _, _ = directions[face]
        turn = -1 if clockwise else 1
        new_faces = {
            name: [row[:] for row in grid]
            for name, grid in self.face.items()
        }

        for source_face, grid in self.face.items():
            if source_face == "Blank":
                continue
            source_normal, horizontal, vertical = directions[source_face]
            for row in range(3):
                for column in range(3):
                    position = tuple(
                        source_normal[index]
                        + horizontal[index] * (column - 1)
                        + vertical[index] * (row - 1)
                        for index in range(3)
                    )
                    if sum(axis[index] * position[index] for index in range(3)) != 1:
                        continue

                    new_position = self.rotateVector(position, axis, turn)
                    new_normal = self.rotateVector(source_normal, axis, turn)
                    target_face = normal_to_face[new_normal]
                    _, target_horizontal, target_vertical = directions[target_face]
                    target_row = 1 + sum(
                        new_position[index] * target_vertical[index]
                        for index in range(3)
                    )
                    target_column = 1 + sum(
                        new_position[index] * target_horizontal[index]
                        for index in range(3)
                    )
                    new_faces[target_face][target_row][target_column] = grid[row][column]

        self.face = new_faces

    def rotateVector(self, vector, axis, direction):
        cross_product = (
            axis[1] * vector[2] - axis[2] * vector[1],
            axis[2] * vector[0] - axis[0] * vector[2],
            axis[0] * vector[1] - axis[1] * vector[0]
        )
        dot_product = sum(axis[index] * vector[index] for index in range(3))
        return tuple(
            direction * cross_product[index] + axis[index] * dot_product
            for index in range(3)
        )


bob = cube()

bob.showCube()

# main loop
while True:
    Command = input()
    ClearCommand = Command.casefold().replace(" ", "")

    CommandList = []
    ci = 0
    for chr in Command:
        while Command[chr] == " ":
            chr +=1
    
         

    if ClearCommand in ["exit", "close", "treminate", "leave", "resign", "discontinue", "eliminate", "stop", "cease", "end", "extinguish", "abolish", "annul", "shutdown"]:
        break

    
