# Passing Arguments 
# Because a function can have multiple parameters, a function call may need multiple arguments.

# Positional arguments
# When you call  a function, Python must match each argument in the function call with a parameter in the function in the function definition. 
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog','biscuit')

# Keyword Arguments
# A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there's no confusion. 
def describe_pet(animal_type, pet_name):
    print(f"\nI have a pet {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='dog', pet_name='biscuit')

# Default Values
# When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter's default value.
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('biscuit')