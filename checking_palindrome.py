def palindrome(string: str, n: int) -> bool:

    if len(string)//2 ==len(string) - n: # условие окончания рекурсии
        return True

    if string[len(string) - n] == string[n - 1]: # сравнивание первого и последнего элемента
        n -= 1
        return palindrome(string, n)

    return False
