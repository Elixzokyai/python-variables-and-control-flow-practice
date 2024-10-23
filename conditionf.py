# here this program checks if a users age is appropriate to buy tickets to a concert
# - if below age 18, print no entry to console
# - if age range is 18 -25 , print free drink
# - if age is above 25, print an extra ticket

# to write functions in python we sue the keyword def
def concert_program1(age):
    # control flow
    if age < 18:
        print("No entry")
    elif 18 <= age <= 25:
        print("free drink")
    elif 25<= age <=100:
        print("Extra ticket")
    else:
        print('Not Eligible')


# to ge t functions to work you must trigger them
#type casting : converting one data type to another int()
age = int(input("Enter your age: "))

# make call to functions
concert_program1(age)
