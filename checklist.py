
# Create the Checklist
from re import I

checklist = []

# Define Functions
def create(item):
    # Create item code here
    item = str(item)
    checklist.append(item)

def read(index):
    # Read code here
    return checklist[index]

def update(index, item):
    # Update code here
    checklist[index] = item

def destroy(index):
    # Destroy code here
    del checklist[index]

def mark_completed(index):
    # Add code here that marks an item as completed
    checklist[index] = "√"+ checklist[index]

def list_all_items():
    # List all items code here
    print(checklist)

def user_input(prompt):
    # Get user input here
    return input(prompt)


def select(function_code):
    # User Selection Code here
    # Create item example
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
    # User selected Read fcn
    elif function_code == "R":
        input_index = user_input("Select index:")
        read(input_index)
    # User selected update fcn
    elif function_code == "U":
        input_index = user_input("Select index:")
        input_item = user_input("Input item:")
        update(input_index, input_item)
    # User selected destroy fcn
    elif function_code == "D":
        input_index = user_input("Select index:")

running = True

while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)