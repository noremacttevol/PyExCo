# Day 3 practice — functions

# basic function with return
def add_numbers(num1, num2):
    return int(num1) + int(num2)

print(add_numbers(5, 10))
print(add_numbers("20", "15"))

# temperature converter
def to_fahrenheit(celsius):
    c = float(celsius)
    return (c * 9/5) + 32

print(to_fahrenheit(100))
print(to_fahrenheit(0))

# default parameter
def greet(name, title="Student"):
    return f"Hello, {title} {name}!"

print(greet("Cameron"))
print(greet("Michalak", "Daniel"))

# shopping cart example from homework
def cart_total(price1, price2):
    return float(price1) + float(price2)

print(cart_total(9.99, 14.50))
