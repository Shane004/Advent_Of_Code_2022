import Challenge1

def get_input():
    return Challenge1.get_list_of_elf_zones()


def zone_overlap(elf_zone_list):
    overlap_count = 0
    for pair in elf_zone_list:
        if int(pair[1][0]) <= int(pair[0][0]) <= int(pair[1][1]):
            overlap_count += 1
        elif int(pair[1][0]) <= int(pair[0][1]) <= int(pair[1][1]):
            overlap_count += 1
        elif int(pair[0][0]) <= int(pair[1][0]) <= int(pair[0][1]):
            overlap_count += 1
        elif int(pair[0][0]) <= int(pair[1][1]) <= int(pair[0][1]):
            overlap_count += 1
        else:
            continue
    return overlap_count


def get_answer():
    mylist = get_input()
    overlap = zone_overlap(mylist)
    return overlap

