# функция для нахождения второго максимального числа
def second_maximum(initial_list, first_max, second_max, i) -> int:
    if i == len(initial_list):
        return second_max
    if initial_list[i] >= first_max:
        second_max = first_max
        first_max = initial_list[i]
    if initial_list[i] > second_max and initial_list[i] < first_max:
        second_max = initial_list[i]
    i += 1
    return second_maximum(initial_list, first_max, second_max, i)


# функция для получения исходных данных (строки)
def accept(initial_list: list) -> int:
    i = 0 # счетчик
    if initial_list[0] > initial_list[1]:
        first_max = initial_list[0] # первое максимальное
        second_max = initial_list[1] # второе максимальное
    else:
        first_max = initial_list[1] # первое максимальное
        second_max = initial_list[0] # второе максимальное
    return second_maximum(initial_list, first_max, second_max, i)
