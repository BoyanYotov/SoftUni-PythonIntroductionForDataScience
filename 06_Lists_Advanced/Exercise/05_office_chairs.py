n = int(input())
total_chairs = 0
total_people = 0
isEnough = True

for _ in range(n):
    chairs, people = input().split()
    count_chairs = int(len(chairs))
    people = int(people)
    if people > count_chairs:
        print(f'{int(people) - count_chairs} more chairs needed in room {_ + 1}')
        isEnough = False
    else:
        total_chairs += count_chairs
        total_people += people

if isEnough:
    print(f'Game On, {abs(total_people - total_chairs)} free chairs left')
