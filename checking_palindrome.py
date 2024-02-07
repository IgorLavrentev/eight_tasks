# функция проверки является ли строка палиндромом
def palindrome(string: str, n: int) -> bool:

    if len(string)//2 ==len(string) - n: # условие окончания рекурсии
        return True
    if string[len(string) - n] != string[n - 1]:
        return False
    return palindrome(string, n-1)


# функция для получения исходных данных (строки)
def accept(string: str) -> bool:

    return palindrome(string, len(string))
