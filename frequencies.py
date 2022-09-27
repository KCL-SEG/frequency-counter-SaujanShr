"""Frequencies function."""

def frequencies(items):
    frequencies = {}

    for item in items:
        item = str(item)
        if item in frequencies:
            frequencies[item] = frequencies[item] + 1
        else:
            frequencies[item] = 1
    
    return frequencies