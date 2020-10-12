print("Connecting to flipkart....")
login_choice = input("do you want to login (Y/N) ")

if login_choice == 'Y':
    user_name = input("Enter your username: ")
    print("Hello", user_name, "welcome to Flipkart Shopping")
else:
    print("Hello guest, welcome to Flipkart shopping")


print("...... Checkout here .......")

if login_choice == 'Y':
    print("you can directly checkout")
else:
    print("You must login for checkout")