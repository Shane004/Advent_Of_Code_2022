def get_answer():
    priority_total = 0
    with open("puzzle_input") as file:
        for line in file:
            first_half = line[0:int(len(line)/2)]
            second_half = line[int(len(line)/2): len(line)-1]
            common_letters = []
            for letter1 in first_half:
                for letter2 in second_half:
                    if letter1 == letter2:
                        if letter1 in common_letters:
                            break
                        else:
                            common_letters.append(letter1)
                            priority_total += letter_to_number(letter1)
            common_letters.clear()
    return priority_total


def letter_to_number(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter.lower()) - 96 + 26
