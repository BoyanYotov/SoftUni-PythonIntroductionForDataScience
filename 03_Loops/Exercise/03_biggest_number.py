# import sys
# from sys import maxsize
# #
# # n = int(input())
# # biggest = -sys.maxsize
# #
# # for i in range(1, n +1):
# #     number = int(input())
# #     if number > biggest:
# #         biggest = number
# #
# # print(biggest)
#

n = int(input())
numbers = [int(input()) for _ in range(n)]
biggest_number = max(numbers)
print(biggest_number)
