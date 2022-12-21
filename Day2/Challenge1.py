A = 1  # rock
B = 2  # paper
C = 3  # scissors

X = A  # rock
Y = B  # paper
Z = C  # scissors

WIN = 6
DRAW = 3
LOSS = 0


def win_lose_draw(column1, column2):
    if column1 == "A":
        if column2 == "X":
            return X + DRAW
        elif column2 == "Y":
            return Y + WIN
        else:
            return Z + LOSS
    elif column1 == "B":
        if column2 == "X":
            return X + LOSS
        elif column2 == "Y":
            return Y + DRAW
        else:
            return Z + WIN
    else:
        if column2 == "X":
            return X + WIN
        elif column2 == "Y":
            return Y + LOSS
        else:
            return Z + DRAW


def check_score():
    total = 0
    with open("2022_Day2_input.txt") as file:
        for line in file:
            total += win_lose_draw(line[0], line[2])
        return total
