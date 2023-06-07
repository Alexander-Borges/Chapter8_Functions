# Define a Function
# Here's a simple function
def greet_user():
    print("Hello!")

greet_user()

# Passing Information to a Function
# Modified slightly, the function greet_user() can not only tell the user Hello! but also greet them by name. For the function to do this, you enter username in the parentheses of the function’s definition at def greet_user().
def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user("alexander")
greet_user("jessica")

# Using a Function with a while Loop
# You can use functions with all the Python structures you've learned about so far. For example, let's use the get_formatted_name() function with a while loop to greet users more formally.
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First_name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")