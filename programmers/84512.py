from itertools import product

def solution(word):
    table = set()
    for w in product(("A","E","I","O","U",""), repeat=5):
        stripped = "".join(w)
        table.add(stripped)
    
    table = sorted(list(table))

    return table.index(word)