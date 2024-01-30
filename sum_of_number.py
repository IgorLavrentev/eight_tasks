def summ(N: int) -> int:
    if N < 1:
        return N%10
    return  N%10 + summ(N//10)
