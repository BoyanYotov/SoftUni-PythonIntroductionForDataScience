def password_validator(password):
    is_valid = True

    if not len(password) >= 6 and len(password) <= 10:
        print('Password must be between 6 and 10 characters')
        is_valid = False

    for symbol in password:
        if not symbol.isalnum():
            print('Password must consist only of letters and digits')
            is_valid = False
            break

    counter = 0
    for symbol in password:
        if symbol.isnumeric():
            counter += 1
    if counter < 2:
        print('Password must have at least 2 digits')
        is_valid = False

    if is_valid:
        print('Password is valid')


password = str(input())
password_validator(password)
