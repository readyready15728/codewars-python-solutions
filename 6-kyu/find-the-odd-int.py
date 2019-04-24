from collections import Counter

def find_it(seq):
    c = Counter(seq)
    
    for k in c:
        if c[k] % 2 == 1:
            return k
