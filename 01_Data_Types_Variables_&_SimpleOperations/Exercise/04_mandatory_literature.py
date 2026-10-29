number_of_pages = int(input())
pages_per_hours = int(input())
days_to_finish = int(input())

hours_to_finish = number_of_pages // pages_per_hours
hours_per_day = hours_to_finish // days_to_finish

print(hours_per_day)
