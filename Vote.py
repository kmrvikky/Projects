# Create a program to check whether a person is eligible to vote or not.
# Instructions
# Get age input from the user.
# If age is 18 or higher, print You can vote.
# If age is less than 18, print You cannot vote.


age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")
