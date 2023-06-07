def greet_users(names):
    for name in names:
        msg = (f"Hello, {name.title()}!")
        print(msg)

usernames = ['alexander','jessica']
greet_users(usernames)