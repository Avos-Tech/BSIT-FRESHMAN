#Simple Registration Application

fname = input("Enter the First name: ")
lname = input("Enter the Last name: ")
mname = input("Enter the Middle name: ")

fullname = fname+" "+mname+" "+lname

print("Welcome to Registration Dashboard!!")

username = str(input("Enter username: "))
password = str(input("Enter the password: "))
Confirm_password = (input("confirm password: "))

if (password == Confirm_password):
	print("Registration Success, Welcome to Admin Dashboard")
elif (password != Confirm_password):
	print("Please confirm the password")
else:
	print("Please try again")