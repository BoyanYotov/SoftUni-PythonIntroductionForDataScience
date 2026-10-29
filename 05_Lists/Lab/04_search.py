n = int(input())
word = str(input())

my_list = []
for i in range(n):
    my_list.append(input())
print(my_list)

# filtered_list = []
# for element in my_list:
#     if word in element:
#         filtered_list.append(element)
#
# print(filtered_list)

for i in range(len(my_list) - 1, -1, -1):
    element = my_list[i]
    if word not in element:
        my_list.remove(element)

print(my_list)
