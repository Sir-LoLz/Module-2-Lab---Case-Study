'''
Zachary Rosch
Student GPA Calculator
01SEP24

This program accepts a last name and GPA input
    and checks if the student is eligible for the Deans list
    or Honor Roll.
'''


# Variables
fName = "" # Input for students first name
lName = ""  # Input for students last name
gpa = 0.0 # Input for students GPA

# Static variavles
deansListThreshold = 3.5 # GPA needed to make it on the Deans List
honorRollThreshold = 3.25 # GPA needed to make it on the Honor Roll list
sentinalValue = "ZZZ"


# Housekeeping
lName = input(f"Enter a students last name. Or enter {sentinalValue} to exit :")

''' main program body '''
while lName != sentinalValue:
    
    # Get the students first name
    fName = input(f"What is {lName}'s first name? :")

    # Get the GPA of the student
    gpa = float(input(f"What is {fName} {lName}'s GPA? :"))
    
    # Test the GPA
    if gpa >= deansListThreshold:
        print(f"{fName} {lName} is eligible for Deans List.")
    elif gpa >= honorRollThreshold:
        print(f"{fName} {lName} is eligible for Honor Roll.")
    else:
        print(f"{fName} {lName} is not eligible.")

    # get the last name of the student
    lName = input(f"Enter another students last name. Or enter {sentinalValue} to exit :")

print("End of program.")
