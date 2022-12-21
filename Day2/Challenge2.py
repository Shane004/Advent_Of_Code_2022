A = 1  # Rock wins against Scissors & loses against Paper
B = 2  # Paper wins against Rock & loses against Scissors
C = 3  # Scissors wins against Paper & looses against Rock

X = LOSE = 0
Y = DRAW = 3
Z = WIN = 6


def win_lose_draw(column1, column2):
    if column2 == "X":
        if column1 == "A":
            return LOSE + C
        elif column1 == "B":
            return LOSE + A
        else:
            return LOSE + B
    elif column2 == "Y":
        if column1 == "A":
            return DRAW + A
        elif column1 == "B":
            return DRAW + B
        else:
            return DRAW + C
    else:
        if column1 == "A":
            return WIN + B
        elif column1 == "B":
            return WIN + C
        else:
            return WIN + A


def check_score():
    total = 0
    with open("2022_Day2_input.txt") as file:
        for line in file:
            total += win_lose_draw(line[0], line[2])
        print(total)


check_score()
