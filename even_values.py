# функция которая оставляет в списке только четные значения
def even(list_original: list, counter: int) -> list:
    if counter < 1: # условие выхода из рекурсии
        return None
    if list_original[counter - 1] % 2 == 0: # проверка на четность
        print(list_original[counter - 1])
    counter -= 1
    return even(list_original, counter)


# функция для получения исходных данных (списка)
def even_value(initial_list: list) -> list:

    return even(initial_list, len(initial_list))
