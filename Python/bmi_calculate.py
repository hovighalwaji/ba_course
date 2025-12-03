def calculate_bmi(weight, height):
    """Calculate Body Mass Index (BMI)."""
    bmi = weight / (height ** 2)
    return bmi

if __name__ == "__main__":
    # Take user input for weight and height
    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in meters: "))
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Print the BMI classification message
    if bmi < 18.5:
        print("BMI: {:.2f} - Underweight".format(bmi))
    elif 18.5 <= bmi < 25:
        print("BMI: {:.2f} - Normal weight".format(bmi))
    elif 25 <= bmi < 30:
        print("BMI: {:.2f} - Overweight".format(bmi))
    else:  # bmi >= 30
        print("BMI: {:.2f} - Obese".format(bmi))