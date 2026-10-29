tasks = [0] * 11

while True:
    command = str(input())
    if command == 'End':
        break
    priority, task = command.split('-')
    # tasks.pop(int(priority))
    # tasks.insert(int(priority), task)
    tasks[int(priority) - 1] = task

result = [x for x in tasks if x != 0]
print(result)
