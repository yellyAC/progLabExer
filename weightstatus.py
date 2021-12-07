def bmi(*args):
    #weight in kilograms divided by height in meters squared.
    return args[0]/((args[1])/100)**2

if __name__ == "__main__":
    print("Enter your height in centimeters (cm): ")
    height = float(input())
    print("Enter your weight in kilograms (kg): ")
    weight = int(input())
    calculation = bmi (weight, height)
    print(f"your BMI is ", calculation)

    if calculation <= 18.4:
        print("Below normal weight.")
    elif calculation <= 24.9:
        print("Normal weigt")
    elif calculation <= 29.9:
        print("Overweight")
    elif calculation <= 34.9:
        print("Obesity class I")
    elif calculation <= 39.9:
        print("Obesity class II")
    else:
        print ("Obesity class III")