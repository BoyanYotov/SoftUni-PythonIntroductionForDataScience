string = str(input())
counter = int(input())

repeat_string = lambda string, n: string * counter
print(repeat_string(string, counter))
