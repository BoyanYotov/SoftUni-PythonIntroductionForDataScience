my_list = input().split()
word = str(input())

filtered_list = list(word for word in my_list if word == "".join(reversed(word)))

print(filtered_list)
print(f'Found palindrome {my_list.count(word)} times')
