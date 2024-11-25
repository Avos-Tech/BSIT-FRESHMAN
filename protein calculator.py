def calculate_protein(weight_kg, activity_level, goal):
    
    protein_recommendations = {
        'sedentary': 0.8,
        'lightly active': 1.0,
        'moderately active': 1.2,
    }
    
    if goal == 'muscle gain':
        protein_multiplier = 1.2
    elif goal == 'weight loss':
        protein_multiplier = 1.0
    elif goal == 'maintenance':
        protein_multiplier = 1.0
    else:
        raise ValueError("Invalid goal. Choose from 'muscle gain', 'weight loss', or 'maintenance'.")

    if activity_level not in protein_recommendations:
        raise ValueError("Invalid activity level. Choose from 'sedentary', 'lightly active', 'moderately active'.")
    
    protein_per_kg = protein_recommendations[activity_level]
    daily_protein = weight_kg * protein_per_kg * protein_multiplier
    
    return daily_protein

def main():
    print("Welcome to the Protein Calculator!")
    
    weight = float(input("Enter your weight in kg: "))
    activity_level = input("Enter your activity level (sedentary, lightly active, moderately active): ").strip().lower()
    goal = input("Enter your goal (muscle gain, weight loss, maintenance): ").strip().lower()
    
    try:
        protein_needs = calculate_protein(weight, activity_level, goal)
        print(f"You should aim for approximately {protein_needs:.2f} grams of protein per day.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()