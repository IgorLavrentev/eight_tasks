# функция которая оставляет в списке только значения с четными индексами
def even(list_original: list, counter: int) -> list:
    if counter < 1: # условие выхода из рекурсии
        return None

    print(list_original[len(list_original) - counter])
    counter -= 2
    return even(list_original, counter)


# функция для получения исходных данных (списка)
def even_indexes(initial_list: list) -> list:

    return even(initial_list, len(initial_list))
