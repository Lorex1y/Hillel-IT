while True:
    n_input = input("Enter a number: ")
    if n_input.isdigit():
        n_input = int(n_input)
        break
    else:
        print("Invalid input!")


fibonacci_numbers = []
a = 0
b = 1

for i in range(n_input):
    fibonacci_numbers.append(a)
    a, b = b, a + b
print(f"Fibonacci numbers of {n_input}: {fibonacci_numbers}")



