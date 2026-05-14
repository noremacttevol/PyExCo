# Day 2 practice — variables and data types

name = "Cameron"
age = 24
gpa = 3.5
enrolled = True

print(name)
print(type(name))
print(type(age))
print(type(gpa))
print(type(enrolled))

# typecasting
num_str = "42"
print(int(num_str) + 8)   # 50

height_str = "5.11"
print(float(height_str))

# f-strings
print(f"My name is {name} and I am {age} years old.")
print(f"GPA: {gpa}")

# string methods
print(name.upper())
print(name.lower())
print(len(name))
