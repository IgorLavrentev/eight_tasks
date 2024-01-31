def palindrome(string: str, str_start: str = '', str_end: str = '', counter: int = 0) -> bool:
    if len(str_start) == len(string)//2 and str_start == str_end:
        return True
    if len(str_start) == len(string)//2 and str_start != str_end:
        return False
    str_start += string[counter] # добавление очередного элемента с начала
    str_end += string[len(string) - counter - 1] # добавление очередного элемента с конца
    counter += 1
    return palindrome(string, str_start, str_end, counter)
