def power(N, M):
    if M == 1:
        return N
    else:
        return N * power(N, M-1)
