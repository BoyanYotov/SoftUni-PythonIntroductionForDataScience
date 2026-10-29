electrons = int(input())
filled_shells = list()
current_shell = 1

while True:
    needed_electrons = 2 * current_shell ** 2
    if needed_electrons <= electrons:
        electrons = electrons - needed_electrons
        filled_shells.append(needed_electrons)
        current_shell += 1
    else:
        if electrons != 0:
            filled_shells.append(electrons)
        break

print(filled_shells)
