def cm_to_inches(cm):
    return cm / 2.54

def inches_to_cm(inches):
    return inches * 2.54

def height_conversion():
    choice = input("Do you want to convert from (1) cm to inches or (2) inches to cm? Enter 1 or 2: ")
    
    if choice == '1':
        cm = float(input("Enter height in centimeters: "))
        inches = cm_to_inches(cm)
        print(f"{cm} cm is equal to {inches:.2f} inches.")
    elif choice == '2':
        inches = float(input("Enter height in inches: "))
        cm = inches_to_cm(inches)
        print(f"{inches} inches is equal to {cm:.2f} cm.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

height_conversion()