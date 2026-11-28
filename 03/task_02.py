user_input = input("Enter a positive number: ")
if user_input.isdigit() and int(user_input) > 0:
    user_input = int(user_input)

    if user_input == 1:
        print("It is not a prime number.")
        exit()

    for i in range(2, user_input):
        if user_input % i == 0:
            print("It is not a prime number.")
            exit()


    print("It is a prime number.")

else: print("Invalid input!")


