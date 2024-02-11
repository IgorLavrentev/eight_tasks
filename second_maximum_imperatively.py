# функция для нахождения второго максимального числа
def second_maximum(initial_list: list) -> int:

    # сортировка списка по убыванию
    for i in range(len(initial_list)): # i проходит от 0 до длины списка
        counter = i + 1  # при каждом проходе задается новое значение counter
        for j in range(counter, len(initial_list)): # counter проходит от i + 1 до длины списка
            # сравнение i-го элемента с индексом элемента 'counter'
            if initial_list[i] < initial_list[j]:
                initial_list[i],  initial_list[j] = initial_list[j], initial_list[i]

    return initial_list[1] # в отсортированном списка возвращается втрой максимальный элемент
