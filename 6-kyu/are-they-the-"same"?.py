def comp(array1, array2):
    for x, y in zip(sorted(array1), sorted(array2)):
        if x**2 != y:
            return False
    
    return True
