facebook = {}

while True:
    user_input = input()
    if user_input == "Log out":
        break

    command = user_input.split(": ")[0]
    username = user_input.split(": ")[1]

    if command == "New follower":
        if username not in facebook:
            facebook[username] = 0
    elif command == "Like":
        count = int(user_input.split(": ")[2])
        if username not in facebook:
            facebook[username] = count
        else:
            facebook[username] += int(count)
    elif command == "Comment":
        if username not in facebook:
            facebook[username] = 1
        else:
            facebook[username] += 1
    elif command == "Blocked":
        if username not in facebook:
            print(f'{username} doesn\'t exist.')
        else:
            del facebook[username]

print(f'{len(facebook)} followers')
for k, v in facebook.items():
    print(f"{k}: {v}")
