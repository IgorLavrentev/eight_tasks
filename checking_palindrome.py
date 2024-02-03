def palindrome(string: str) -> bool:

    def palindrome_two(string_t): # функция разворота строки
        if string_t == "":
            return string_t
        if string_t != "":
            return palindrome_two(string_t[1:]) + string_t[0]
        return '' # для согласования операторов return

    string_two = string
    string_two_2 = palindrome_two(string_two)

    # сравнивание исхдной строки с развернутой
    return string == string_two_2
