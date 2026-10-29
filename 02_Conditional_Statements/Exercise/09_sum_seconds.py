seconds1 = int(input())
seconds2 = int(input())
seconds3 = int(input())

total_seconds = seconds1 + seconds2 + seconds3
minutes = total_seconds // 60
seconds = round(total_seconds % 60, 2)

print(f'{minutes}:{seconds:02d}')
