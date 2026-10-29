char1 = input()
char2 = input()


def string_from_chars(char1, char2) -> str:
    start = ord(char1)
    final = ord(char2)
    result = []
    for i in range(start + 1, final):
        result.append(chr(i))
    return ' '.join(result)


print(string_from_chars(char1, char2))
