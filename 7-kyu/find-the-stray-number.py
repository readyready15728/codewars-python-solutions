from collections import Counter

def stray(arr):
    occurrences = Counter()
    
    for i in arr:
        occurrences[i] += 1
        
    for k, v in occurrences.items():
        if v == 1:
            return k
