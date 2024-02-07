# функция проверки является ли строка палиндромом
def palindrome(string: str, n: int) -> bool:

    if len(string)//2 ==len(string) - n: # условие окончания рекурсии
        return True
    if string[len(string) - n] == string[n - 1]: # сравнивание первого и последнего элемента
        n -= 1
        return palindrome(string, n)
    return False

# функция для получения исходных данных (строки)
def accept(string: str) -> bool:

    n = len(string) # длина строки
    if palindrome(string, n):
        return True
    return False
