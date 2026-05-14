# Day 5 practice — loops and lists

# basic list
classes = ["Python 1", "Python 2", "Networking", "Linux"]

# for loop
for c in classes:
    print(f"Taking: {c}")

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# range
for i in range(1, 11):
    print(i, end=" ")
print()

# list methods
classes.append("Databases")
print(classes)

classes.remove("Linux")
print(classes)

# indexing
print(classes[0])
print(classes[-1])

# pop
last = classes.pop()
print(f"Removed: {last}")
print(classes)
