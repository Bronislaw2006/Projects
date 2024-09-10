# BMI Calculator

# Ask the user for their height in meters, convert the input to float, and store it in the 'height' variable.
height = (float(input("Enter your height in m:")))

# Ask the user for their weight in kilograms, convert the input to float, and store it in the 'weight' variable.
weight = (float(input("Enter your weight in kg:")))

# Calculate BMI using the formula: weight / (height squared), and store the result in 'bmi'.
bmi = weight / height ** 2

# Convert the BMI value to a float explicitly (though it's already a float) and store it in 'bmi_as_float'.
bmi_as_float = float(bmi)

# Conditional statements to determine the BMI category based on the calculated BMI value.
# If BMI is less than 18.5, print that the user is underweight.
if bmi_as_float < 18.5:
    print(f"Your BMI is {bmi_as_float}, you are underweight.")

# If BMI is between 18.5 and 24.9, print that the user has a normal weight.
elif bmi_as_float < 25:
    print(f"Your BMI is {bmi_as_float}, you have a normal weight.")

# If BMI is between 25 and 29.9, print that the user is slightly overweight.
elif bmi_as_float < 30:
    print(f"Your BMI is {bmi_as_float}, you are slightly overweight.")

# If BMI is between 30 and 34.9, print that the user is obese.
elif bmi_as_float < 35:
    print(f"Your BMI is {bmi_as_float}, you are obese.")

# If BMI is 35 or more, print that the user is clinically obese.
elif bmi_as_float >= 35:
    print(f"Your BMI is {bmi_as_float}, you are clinically obese.")
