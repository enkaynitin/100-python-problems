def rabit_chicken_puzzle(heads, numLegs):
    for rabbits in range(heads + 1):
        chickens = heads - rabbits
        if 2 * chickens + 4 * rabbits == numLegs:
            return chickens, rabbits
    return None, None

print rabit_chicken_puzzle(35, 94)
