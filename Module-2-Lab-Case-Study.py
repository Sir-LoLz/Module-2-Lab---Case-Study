'''
Zachary Rosch
Student GPA Calculator
01SEP24

This program accepts a last name and GPA input
    and checks if the student is eligible for the Deans list
    or Honor Roll.
'''


# Variables
fName = ""  # Input for students last name
gpa = 0.0 # Input for students GPA

# Static variavles
deansListThreshold = 3.5 # GPA needed to make it on the Deans List
honorRollThreshold = 3.25 # GPA needed to make it on the Honor Roll list
sentinalValue = "ZZZ"


# Housekeeping
fName = input(f"Enter a students name. Or enter {sentinalValue} to exit :")

''' main program body '''
while fName != sentinalValue:
    
    # Get the GPA of the student
    gpa = float(input(f"What is {fName}'s GPA? :"))
    
    # Test the GPA
    if gpa >= deansListThreshold:
        print(f"{fName} is eligible for Deans List.")
    elif gpa >= honorRollThreshold:
        print(f"{fName} is eligible for Honor Roll.")
    else:
        print(f"{fName} is not eligible.")

    # get the last name of the student
    fName = input(f"Enter another students name. Or enter {sentinalValue} to exit :")

print("End of program.")