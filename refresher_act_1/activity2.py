height = 0.0
weight = 0.0
BMI = 0.0
weight = float(input('Enter your weight:- '))
height = float(input('Enter your height:- '))

BMI = weight / (height * height)

print('Weight: {}, Height: {}, BMI: {}'.format(weight,height,round(BMI,2)))
