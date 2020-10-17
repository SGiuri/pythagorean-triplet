from math import gcd


def triplets_with_sum(number):
    primitives_triplets = triplets_in_range(0,number)

    sum_triplets = []

    for triplet in triplets_in_range(1,int(number**0.5)):
        if sum(triplet) == number:

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
    m = start + 1
    n = start
    primitives_triplets = []
    for mm in range(m, end, 1):
        for nn in range(n, mm, 1):
            # print(mm, nn)
            if coprime(mm, nn):

                a = mm ** 2 - nn ** 2
                b = 2 * mm * nn
                c = mm ** 2 + nn ** 2
                somma = a + b + c
                yield sorted([a,b,c])


def coprime(m, n):
    if gcd(m, n) == 1:
        return True
    return False
