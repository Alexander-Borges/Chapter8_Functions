# Returning a Simple Value
# Let's look at a function that takes a first and last name, and returns a neatly formatted full name:
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

# Making an Argument Optional
# Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to. You can use default values to make an argument optional.
def get_formatted_name(first_name,last_name, middle_name = ''):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'bon','jovi')
print(musician)
