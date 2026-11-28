allowed_commands = [1, 2, 3, 0]

while True:

    user_input = input("Enter 1, 2, 3 or 0 ")
    if not user_input.isdigit() or int(user_input) not in allowed_commands:
        print("\033[31m Unknown command!\033[0m")
        continue

    user_input = int(user_input)


    if user_input == 1:
        print ("Hello!")

    elif user_input == 2:
        for i in range(1, 11):
            print (i)

    elif user_input == 3:
        while True:
            n_input = input("Enter a number: ")
            if n_input.isdigit():
                print(sum(range(1, int(n_input) + 1)))
                break
            else:
                print("It is not a number.")


    elif user_input == 0:
        print("Goodbye!")
        exit()






