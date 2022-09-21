cart = [
    ('Product 1', 30),
    ('Product 2', 20),
    ('Product 3', 50)
]

total = sum([float(y) for x, y in cart])

print(total)
