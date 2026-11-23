# region First Option
traffic_light_colors = ['red', 'yellow', 'green']

user_input = input("Please enter a traffic light color: ").lower().strip()
if user_input not in traffic_light_colors:
    print("Unknown traffic light color.")
    exit()
if user_input == 'red':
    print("STOP!")
elif user_input == 'yellow':
    print("BE READY!")
elif user_input == 'green':
    print("GO!")

# endregion


# region Second Option
traffic_light_colors = ['red', 'yellow', 'green']

user_input = input("Please enter a traffic light color: ").lower().strip()
if user_input not in traffic_light_colors:
    print("Unknown traffic light color.")
    exit()

match user_input:
    case 'red':
        print("STOP!")
    case 'yellow':
        print("BE READY!")
    case 'green':
        print("GO!")

# endregion