def calculate_bmi(values):
    height = float(values.get("height", 100))
    weight = float(values.get("weight", 100))
    status = 'unknown'
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        status ='Underweight'
    elif bmi < 25.0:
        status = 'Normal weight'
    elif bmi < 30:
        status = 'Overweight'
    else:
        status = 'Obese'
    return status

def getValues():
    values = {}
    values["height"] = input('How tall are you in meters')
    values["weight"] = input('How much do you weight in kg')
    return values

def main():
    "The main program"
    values = getValues()
    bmi = calculate_bmi(values)
    print("bmi is:", bmi)

main()



