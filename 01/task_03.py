user_input = int(input("Enter a number of minutes: "))
hours = user_input // 60
minutes = user_input % 60
print(f"{hours} hours, {minutes} minutes")