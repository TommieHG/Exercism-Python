def distance(strand_a, strand_b):
    hammingDistance = 0

    if len(strand_a) != len(strand_b):
        raise ValueError(".+")
    
    for x,y in zip(strand_a, strand_b):
        if x != y:
            hammingDistance += 1

    return hammingDistance
        
