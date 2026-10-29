n1 = int(input())
n2 = int(input())
n3 = int(input())


def sum_numbers(n1, n2) -> int:
    return n1 + n2


def subtract(n3) -> int:
    result = sum_numbers(n1, n2)
    return result - n3


print(subtract(n3))
