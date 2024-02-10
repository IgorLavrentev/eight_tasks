# функция для нахождения второго максимального числа
def second_maximum(initial_list, i, counter = 0) -> int:
    if i == len(initial_list) - 1:
        return initial_list[1]

    if counter == len(initial_list):
        counter = i + 1
        i += 1

    if initial_list[i] < initial_list[counter]:
        initial_list[i],  initial_list[counter] = initial_list[counter], initial_list[i]

    counter += 1

    return second_maximum(initial_list, i, counter)


# функция для получения исходных данных (строки)
def accept(string: str) -> int:
    i_1 = 0
    counter_1 = 0
    return second_maximum(string, i_1, counter_1)
