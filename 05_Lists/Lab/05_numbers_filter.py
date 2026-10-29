n = int(input())
my_list = []

for i in range(n):
    number = int(input())
    my_list.append(number)

command = str(input())

match command:
    case 'even':
        my_list = list(filter(lambda x: x % 2 == 0, my_list))
        print(my_list)
    case 'odd':
        my_list = list(filter(lambda x: x % 2 != 0, my_list))
        print(my_list)
    case 'negative':
        my_list = list(filter(lambda x: x < 0, my_list))
        print(my_list)
    case 'positive':
        my_list = list(filter(lambda x: x >= 0, my_list))
        print(my_list)
