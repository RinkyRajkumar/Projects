height = float(input("What is your height in centimeter? "))
weight = int(input("What is your weight? "))

height = height/100
body_mass_index = weight / (height * height)

if body_mass_index < 18.5:
    print(f"You are underweight as you are having a BMI of {body_mass_index}.")
elif body_mass_index < 25:
    print((f"You are normal in weight as you are having a BMI of {body_mass_index}."))
elif body_mass_index < 30:
    print(f"You are slightly overweight as you are having a BMI of {body_mass_index}.")
elif body_mass_index < 35:
    print(f"You are obese in weight as your are having a BMI of {body_mass_index}.")
else:
    print(f"You are morbidly obese as you are having a BMI of {body_mass_index}.")
