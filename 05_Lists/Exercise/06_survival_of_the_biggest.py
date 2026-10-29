my_list = list(map(int, input().split()))
n = int(input())
# sorted_list = sorted(my_list)
#
# for i in range(n):
#     number = sorted_list[i]
#     my_list.remove(number)
#
# print(", ".join(map(str, my_list)))

for _ in range(n):
    my_list.remove(min(my_list))

print(", ".join(map(str, my_list)))
