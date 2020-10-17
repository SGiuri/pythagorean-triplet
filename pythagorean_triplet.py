from math import gcd


def triplets_with_sum(number):
    primitives_triplets = triplets_in_range(0,number)

    sum_triplets = []

    for triplet in primitives_triplets:
        if sum(triplet) == number:
            print("T :", triplet)
            if triplet not in sum_triplets:
                sum_triplets.append(triplet)
        elif number % sum(triplet) == 0:
            molt = number // sum(triplet)
            new_triplet = [j * molt for j in triplet]
            if new_triplet not in sum_triplets:
                print("NT :", new_triplet)
                sum_triplets.append(new_triplet)

    return sum_triplets

def triplets_in_range(start, end):
    m = 2
    n = 1
    primitives_triplets = []
    for mm in range(m, end, 1):
        for nn in range(n, mm, 1):
            # print(mm, nn)
            if coprime(mm, nn):

                a = mm ** 2 - nn ** 2
                b = 2 * mm * nn
                c = mm ** 2 + nn ** 2
                somma = a + b + c
                if sorted([a, b, c]) not in primitives_triplets:
                    primitives_triplets.append(sorted([a, b, c]))
            if somma > 2 * end:
                break
        if somma > 2 * end:
            break
    return primitives_triplets

def coprime(m, n):
    if gcd(m, n) == 1:
        return True
    return False
