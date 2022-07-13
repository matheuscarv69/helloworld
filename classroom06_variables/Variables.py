

name = 'Matheus'
surname = 'Carvalho'
age = 22
overEighteen = age > 18
height = 1.70
weight = 90

# IMC
bmi = weight // height ** 2

print("Name:", name)
print("Surname:", surname)
print("Age:", age)
print("Height:", height)
print("+18:", overEighteen)

print()

print(name, 'is', age, 'years old, and his IMC is:', bmi)
