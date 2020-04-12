print("Please enter your height in feet and inches.Then enter your body mass,locally known as weight")
print("Your Height in ")
x=float(input("Feet: \t"))
y=float(input("Inch: "))
w=float(input("What is your mass in kg?:"))
h=x*0.3048 + y*0.0254
BMI=w/h**2
print("Your BMI is :", round(BMI,2)),

if BMI > 25:
    print("you are overweight")
    print("Your weight should be more than "),print(round(18.5*h**2,2))
    print("but less than"),print(round(25*h**2,2))
    print("An ideal BMI for you would be 22")
else:
    print('you are not overweight')
    print("You are doing good.",end=" ")
    print("An ideal BMI would be 22;",end=" ")
    print("To have a healthier life keep your body mass as ", round(22*h**2,2),"kg")


