def get_input_as_list():
    finished_list = []
    with open("puzzle_input") as file:
        file_lines = file.readlines()
        for line in file_lines:
            line = line.strip("\n")
            finished_list.append(line)
        return finished_list


def get_priority(badge_list):
    my_list = badge_list
    priority_total = 0
    for letter in my_list:
        if letter.islower():
            priority_total += ord(letter) - 96
        else:
            priority_total += ord(letter.lower()) - 96 + 26
    return priority_total


def get_badge(item_list):
    badge_list = []
    for index in range(0, len(item_list), 3):
        for char in item_list[index]:
            if char in item_list[index+1] and char in item_list[index+2]:
                badge_list.append(char)
                break
    return badge_list


def get_answer():
    mylist = get_input_as_list()
    badge_list = get_badge(mylist)
    priority = get_priority(badge_list)
    return priority
