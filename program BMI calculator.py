def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 19.0:
        category = "Underweight"
    elif 19.0 <= bmi < 20:
        category = "Normal weight"
    elif 20 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category
def main():
    print("Welcome!it's BMI calculator... Let's check your BMI category.")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return
        
        bmi, category = calculate_bmi(weight, height)
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    
    except ValueError:
        print("Invalid input: Please enter numbers only.")
if __name__ == "__main__":
    main()

        
