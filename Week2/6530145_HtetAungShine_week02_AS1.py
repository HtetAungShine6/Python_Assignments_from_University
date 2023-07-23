week = int(input("Enter weeks : "))
day = int(input("Enter days : "))
totalWeeksInHours = week * 24 * 7
totalDaysInHours = day * 24
total_hours = totalWeeksInHours + totalDaysInHours
print(f'The total number of hours is {total_hours} hours ')