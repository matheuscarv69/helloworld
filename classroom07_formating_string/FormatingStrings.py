name = 'Matheus'
age = 22
height = 1.70
weight = 90

bmi = weight // height ** 2
imc = weight / height ** 2

print('Old Way')
print(name, 'is', age, 'years old and his BMI is:', bmi)

print("\nUsing F'strings")
print(f'{name} is {age} years old and his BMI is: {bmi}')

print("\nRounding Values")
print(f'{name} is {age} years old and his BMI is: {bmi:.2f}')

print("\nOther Way using format function")
print('{} is {} years old and his BMI is: {:.2f}'.format(name, age, imc))

print("\nFormat function - enumerating arguments")
print('{0} is {1} years old, {0} have {2:.2f} BMI'.format(name, age, imc))

print("\nFormat function - naming arguments")
print('{name} is {age} years old and his BMI is {bmi:.2f}'.format(name=name, age=age, bmi=imc))
