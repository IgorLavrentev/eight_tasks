def palindrome(string: str) -> bool:

    # hasattr - функция, используемая для проверки наличия у объекта определенного атрибута
    if not hasattr(palindrome, 'counter'): # если у функции palindrome нет атрибута counter
        palindrome.counter = len(string)

    if len(string)//2 == len(string) - palindrome.counter: # условие окончания рекурсии
        # удаление атрибута функции для правильной работы функции при повторном вызове
        del palindrome.counter
        return True

    # сравнивание первого и последнего элемента
    if string[len(string) - palindrome.counter] == string[palindrome.counter - 1]:
        palindrome.counter -= 1
        return palindrome(string)

    return False
