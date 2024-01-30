def list_len(L: list, counter = 0) -> int:

    if len(L) - 1 == 0:
        counter += 1
        return counter
    
    L.pop(0)
    counter += 1
    return list_len(L, counter) 
