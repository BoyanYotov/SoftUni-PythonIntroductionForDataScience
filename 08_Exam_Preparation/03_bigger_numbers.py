numbers = list(map(int, input().split()))
n = int(input())
bigger_numbers = list(filter(lambda x: x > n, numbers))

bigger_numbers_str = list(map(lambda x: str(x), bigger_numbers))

print(" ".join(bigger_numbers_str))
