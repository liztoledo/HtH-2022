
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
    index = int(index)
    print(checklist[index])

def update(index, item):
    # Update code here
    index = int(index)
    checklist[index] = item

def destroy(index):
    # Destroy code here
    index = int(index)
    del checklist[index]

def mark_completed(index):
    # Add code here that marks an item as completed
    checklist[index] = "√"+ checklist[index]

def list_all_items():
    # List all items code here
    completed = 0
    incompleted = []

    return checklist

def user_input(prompt):
    # Get user input here
    return input(prompt)

def select(function_code):
    # User Selection Code here

    # Create item example
    #User selected P to print list
    if function_code == "P":
        input_item = user_input("Input item:")
        create(input_item)
        running = True
        return running
    
    #User selected A to add to list
    if function_code == "A":
        input_item = user_input("Input item:")
        create(input_item)
        running = True
        return running
        
    # User selected D to delete item from list
    elif function_code == "D":
        input_index = user_input("Select index:")
        running = True
        return running

    # User selected Read fcn
    elif function_code == "R":
        input_index = user_input("Select index:")
        read(input_index)
        running = True
        return running

    # User selected update fcn
    elif function_code == "U":
        input_index = user_input("Select index:")
        input_item = user_input("Input item:")
        update(input_index, input_item)
        running = True
        return running

    #Unvalid Command
    else:
        print("Please enter a valid checklist command.")
        running = True
        return running

running = True

while running:
    selection = user_input(
        "Press one of the following \n P to display list \n A to add to list \n D to delete from list \n U to replace an item from list \n R to Read from list \n and Q to quit")
    running = select(selection)


#What I need to complete
#P command to display list
#Q command
#Include mark_completed and list_all_items in select function
#Add U, D to selestion inputs
#Work on the list_all_items

