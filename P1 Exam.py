#Grade_Evaluation

fname = input("Enter the First Name: ")
mname = input("Enter the Middle Name: ")
lname = input("Enter the Last Name: ")
address = input("Enter the Address: ")
subject = input("Enter the Subject: ")
grade = float(input("Enter the Grade: "))

fullname = fname + " " + lname + " " + mname

if (0 <= grade <= 49):
    gradestatus = "Failed"
elif (50 <= grade <= 60):
    gradestatus = "Very Poor"
elif (61 <= grade <= 70):
    gradestatus = "Poor"
elif (71 <= grade <= 80):
    gradestatus = "Good"
elif (81 <= grade <= 90):
    gradestatus = "Very Good"
elif (91 <= grade <= 100):
    gradestatus = "Excellent"
else:
    gradestatus = "Try again"

print("Fullname: ", fullname)
print("Address: ", address)
print("Subject code: ", subject)
print("Grade: ", grade)
print("Status:", gradestatus)