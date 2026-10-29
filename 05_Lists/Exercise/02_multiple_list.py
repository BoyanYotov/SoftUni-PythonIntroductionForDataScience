factor = int(input())
count = int(input())

my_list = []
counter = factor

# while True :
#     if counter % factor == 0:
#         my_list.append(counter)
#     if len(my_list) == count:
#         break
#     counter += 1

for i in range(1, count + 1):
    my_list.append(i * factor)

print(my_list)
