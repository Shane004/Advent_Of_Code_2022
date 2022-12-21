import Challenge1


def get_answer():
    list_of_lists = Challenge1.get_input()
    list_of_lists.sort(key=sum, reverse=True)
    total = 0
    for i in range(3):
        total += sum(list_of_lists[i])
    return total
