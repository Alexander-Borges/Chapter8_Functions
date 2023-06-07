#  Modifying a List in a Function
# When you pass a list to a function, the function can modify the list. Any changes made to the list inside the function's body are permanent, allowing you to work efficiently even when you're dealing with large amounts of data.

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant','dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model:{current_design}")
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

