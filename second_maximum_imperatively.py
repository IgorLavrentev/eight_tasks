def second_maximum(initial_list: list) -> int:
    first_max = initial_list[0] # первое максимальное
    second_max = initial_list[1] # второе максимальное
    for i in range(len(initial_list)):
        if initial_list[i] >= first_max:
            second_max = first_max
            first_max = initial_list[i]
            continue
        if initial_list[i] > second_max:
            second_max = initial_list[i]
    return second_max
