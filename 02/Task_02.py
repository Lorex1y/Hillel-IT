year = input("Enter a year: ")
if year.isdigit() and 0 < int(year) < 10000:
    year = int(year)
else:
    print("Invalid input")
    exit()

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("The year is leap.")
else :
    print("The year is not leap.")