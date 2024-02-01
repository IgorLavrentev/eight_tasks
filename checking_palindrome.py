def palindrome(string: str, str_start = None, str_end = None, counter = None) -> bool:
    
    # присвоение изменяемого значения внутри функции
    if str_start is None:
        str_start: str = ''
    if str_end is None:
        str_end: str = ''
    if counter is None:
        counter: int = 0

    if len(str_start) == len(string)//2 and str_start == str_end:
        return True
    if len(str_start) == len(string)//2 and str_start != str_end:
        return False
    str_start += string[counter] # добавление очередного элемента с начала
    str_end += string[len(string) - counter - 1] # добавление очередного элемента с конца
    counter += 1
    return palindrome(string, str_start, str_end, counter)
