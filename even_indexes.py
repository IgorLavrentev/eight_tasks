# функция которая оставляет в списке только значения с четными индексами
def even(list_original: list, counter: int) -> list:
    if counter < 1: # условие выхода из рекурсии
        return list_original
    if (counter - 1) % 2 != 0: # проверка индекса на нечетность
        del list_original[counter - 1]
    counter -= 1
    return even(list_original, counter)


# функция для получения исходных данных (списка)
def even_indexes(initial_list: list) -> list:

    return even(initial_list, len(initial_list))
