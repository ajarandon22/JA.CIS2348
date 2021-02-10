# Jarandon Adams - 1812590

# This program will calculate a persons age in years using their birthday and current date.

print("Welcome to my Age Calculator")

# User will enter the current date here:

print("Please enter the current date below ↓")
cMonth = int(input('Current Month:'))
cDay = int(input('Current Day:'))
cYear = int(input('Current year:'))

# User will enter their birthday date here:

print("Please enter your Birthday ↓")
bMonth = int(input('Birthday Month:'))
bDay = int(input('Birth Day:'))
bYear = int(input('Birth year:'))

# Calculate age of the given person here:
# If birthday month/day are greater than current month/day (Birthday passed already), add a year to "years"

years = cYear - bYear - 1
if bMonth < cMonth:
    years += 1
elif cMonth == bMonth:
    if bDay < cDay:
        years += 1

# If the current day is their birthday, print Happy Birthday. If not, print their current age.

if cMonth == bMonth and cDay == bDay:
    print('Happy Birthday!!')
elif cMonth != bMonth or cDay != bDay:
    print('You are ' + str(years) + " years old.")
