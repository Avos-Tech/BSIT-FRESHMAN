#user, password, admin, cashier, student

user = str(input("Enter the Username: "))
password = input("Enter the Password: ")

admin = str("admin")
cashier = str("cashier")
student = str("student")

if user == admin and user == password:
	print ("welcome to admin dashboard")
elif user == cashier and user == password:
	print("welcome to cashier dashboard")
elif user == student and user == password:
	print("welcome to student dashboard")
else:
	print ("try again")