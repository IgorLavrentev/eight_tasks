# функция разворота строки
def line_reversal(string_t: str) -> str:
    if string_t == "":
        return string_t
    if string_t != "":
        return line_reversal(string_t[1:]) + string_t[0]
    # для согласования операторов return
    return ''

def palindrome(string: str) -> bool:
    string_reverse = line_reversal(string)
    # сравнивание исхдной строки с развернутой
    if string == string_reverse:
        return True
    return False
