while True:
    n_input = input("Enter a number: ")
    if n_input.isdigit():
        n_input = int(n_input)
        break
    else:
        print("Invalid input!")

temp_num = n_input
count_of_digits = 0
sum_of_digits = 0

# calculation count and sum of digits

if temp_num == 0:
    count_of_digits = 1
else:
    while temp_num > 0:
        sum_of_digits += temp_num % 10
        temp_num //= 10
        count_of_digits += 1


print(f"count_of_digits = {count_of_digits}, sum = {sum_of_digits}")
