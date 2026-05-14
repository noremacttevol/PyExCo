# Day 4 practice — conditionals

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Below C")

# comparison operators
x = 10
y = 20

print(x == y)
print(x != y)
print(x < y)
print(x > y)
print(x <= 10)

# and / or
age = 24
has_id = True

if age >= 21 and has_id:
    print("Can enter")
else:
    print("Cannot enter")

# RPS from class
player = "rock"
computer = "scissors"

if player == computer:
    print("Tie")
elif (player == "rock" and computer == "scissors") or \
     (player == "scissors" and computer == "paper") or \
     (player == "paper" and computer == "rock"):
    print("Player wins")
else:
    print("Computer wins")
