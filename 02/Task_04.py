username = input("Please enter your username: ")
email = input("Please enter your email: ")
age = input("Please enter your age: ")
password = input("Please enter your password: ")

input_errors = []

# username check
if len(username) < 5:
    input_errors.append("Your username is too short. Must be at least 5 characters.")
if  username and username[0].isdigit():
    input_errors.append("Your username cannot start with a number.")
if " " in username:
    input_errors.append("Your username cannot contain whitespace.")

# email check
if email.count("@") != 1:
    input_errors.append("Your email address is not valid. Must contain exactly one '@' character.")

# age check
if not age.isdigit():
    input_errors.append("Your age is not valid. Must be a number.")
else:
    age = int(age)
    if age < 16:
        input_errors.append("Your age must be at least 16.")

# password check
same_characters = True
if len(password) < 8:
    input_errors.append("Your password must be at least 8 characters.")
if " " in password:
    input_errors.append("Your password cannot contain whitespace.")

if password and password.count(password[0]) == len(password):
    input_errors.append("Password cannot consist of one character.")





if not input_errors:
    print("You have successfully signed up.")

else:
    print(*input_errors, sep="\n")