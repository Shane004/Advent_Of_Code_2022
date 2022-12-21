def get_input():
    list_of_lists = []
    with open("2022_day1_input.txt") as input_file:
        elf_list = []
        for line in input_file:
            if line != "\n":
                elf_list.append(int(line))
            else:
                list_of_lists.append(elf_list.copy())
                elf_list.clear()
    return list_of_lists


def find_max_sum_list(list_of_lists):
    return sum(max(list_of_lists, key=sum))


def get_answer():
    list_of_lists = get_input()
    return find_max_sum_list(list_of_lists)