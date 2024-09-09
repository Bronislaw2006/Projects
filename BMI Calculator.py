#BMI CALCULATOR

height = (float(input("Enter your height in m:")))
weight = (float(input("Enter your weight in kg:")))
bmi = weight / height ** 2
bmi_as_float = float(bmi)
if bmi_as_float < 18.5:
  print(f"Your BMI is {bmi_as_float}, you are underweight.")
elif bmi_as_float < 25:
  print(f"Your BMI is {bmi_as_float}, you have a normal weight.")
elif bmi_as_float < 30:
  print(f"Your BMI is {bmi_as_float}, you are slightly overweight.")
elif bmi_as_float < 35:
  print(f"Your BMI is {bmi_as_float}, you are obese.")
elif bmi_as_float >=35:
  print(f"Your BMI is {bmi_as_float}, your are clinically obese.")