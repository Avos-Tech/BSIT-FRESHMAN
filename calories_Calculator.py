def calculate_calories(weight, height, age, sex, activity_level):
    if sex.lower() == 'male':
        bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    else:
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

    activity_factors = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725
    }

    calories_needed = bmr * activity_factors[activity_level.lower()]
    return calories_needed

weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))
age = int(input("Enter your age: "))
sex = input("Enter your sex (male or female): ")
activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, very active): ")

calories = calculate_calories(weight, height, age, sex, activity_level)
print(f"You need approximately {calories:.2f} calories per day to maintain your weight.")

