# simple_calculator

fnum = int(input("Enter the first number: "))
snum = int(input("Enter the second number: "))
operator = input(" Enter Arithmetic Operator: ")
print ("+ = addition \n- = substraction \n* = multiplication \n/ division \n% == modulus \n** exponent \n")
if (operator == "+"):
	print ("addition ", fnum+snum)
elif (operator == "-"):
	print ("substraction ", fnum-snum)
elif (operator == "*"):
	print ("multiplication ", fnum*snum)
elif (operator == "/"):
	print ("division ", fnum/snum)
elif (operator == "*"):
	print ("multiplication ", fnum*snum)
elif (operator == "%"):
	print ("modulus ", fnum%snum)
elif (operator == "**"):
	print ("exponent ", fnum**snum)
else:
	print ("Arithmetic Error Please Try Again!")