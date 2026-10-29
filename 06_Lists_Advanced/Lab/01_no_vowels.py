# user_input = str(input())
# result = [symbol for symbol in user_input if symbol.lower() not in 'aeiou']
# print("".join(result))


user_input = str(input())
chars = list(filter(lambda c: c not in 'aeiouAEIOU', user_input))
print("".join(chars))
