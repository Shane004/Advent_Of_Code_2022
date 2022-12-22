def get_list_of_elf_zones():
    with open("Day4_input.txt") as file:
        elf_list = []
        raw_list = file.readlines()
        for pair in raw_list:
            pair_list = []
            pair = pair.strip("\n")
            pair = pair.rsplit(",")
            for elf in pair:
                elf = elf.rsplit("-")
                pair_list.append(elf)
            elf_list.append(pair_list.copy())
        return elf_list


def zone_overlap(elf_zone_list):
    overlap_count = 0
    for pair in elf_zone_list:
        if int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1]):
            overlap_count += 1
        elif int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1]):
            overlap_count += 1
        else:
            continue
    return overlap_count


def get_answer():
    mylist = get_list_of_elf_zones()
    overlap = zone_overlap(mylist)
    return overlap
