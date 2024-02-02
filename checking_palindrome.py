def palindrome(string: str) -> bool:

    if len(string) == 1 or len(string) == 0: # условие окончания рекурсии
        return True

    if string[0] == string[len(string) - 1]: # сравнивание первого и последнего элемента
        return palindrome(string[1 : len(string) - 1].replace(" ", ""))
    
    else:
        return False
