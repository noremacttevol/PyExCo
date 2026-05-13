1) Add Two Numbers
You’re working on a calculator app. Write a function add_numbers(num1, num2) that takes two numbers (as strings or ints), adds them together, and returns the result as an integer.
def add_numbers(num1, num2):
    """Takes two numbers (strings or ints) and returns their sum as an integer."""
    return int(num1) + int(num2)

2) Temperature Converter
You're creating a weather dashboard that requires a Celsius → Fahrenheit converter. Write a function to_fahrenheit(celsius) that takes in a Celsius value (string or float), converts it using the formula (C * 9/5) + 32, and returns the result as a float.
def to_fahrenheit(celsius):
    """Converts a Celsius value (string or float) to Fahrenheit and returns a float."""
    celsius_val = float(celsius)
    fahrenheit = (celsius_val * 9/5) + 32
    return float(fahrenheit)

3) Age in Five Years
A social media app wants to show how old someone will be in five years and has hired you to write the code. Create a function age_in_five(age) that takes in the current age (string or int), adds 5, and returns the result as an integer.
def age_in_five(age):
    """Takes in the current age (string or int), adds 5, and returns the result as an integer."""
    return int(age) + 5

4) Shopping Cart Total
The checkout system at Amazon needs help and Jeff himself has personally asked you to intervene. Write a function cart_total(price1, price2) that takes in two prices (as strings or floats), adds them, and returns the result as a float.
def cart_total(price1, price2):
    """Takes in two prices (as strings or floats), adds them, and returns the result as a float."""
    return float(price1) + float(price2)

5) Greeting Generator
Google's new chatbot system needs to personalize greetings to users and you've been assigned to the team responsible. Write a function greet(name) that takes in a name (string or bytes), and returns "Hello, (name)!" as a string.
def greet(name):
    """Takes in a name (string or bytes) and returns 'Hello, (name)!' as a string."""
    if isinstance(name, bytes):
        name = name.decode('utf-8')
    return f'Hello, {name}!'

6) Double or Nothing
An online casino app needs your help creating a "double down" feature on one of their most popular games. Write a function double(value) that takes in a number (string or int), multiplies it by 2, and returns the result as an integer.
def double(value):
    """Takes in a number (string or int), multiplies it by 2, and returns the result as an integer."""
    return int(value) * 2

7) Employee Registration
The HR system at your company stores first and last names separately, but the CEO wants a "full name" stored as well because he believes it will save the company millions. Write a function full_name(first, last) that takes two strings, combines them with a space in between, and returns the result as a string.
def full_name(first, last):
    """Takes two strings, combines them with a space in between, and returns the result as a string."""
    return f"{first} {last}"

8) Count Characters
Your fancy new LLM needs to record word length before tokenizing an input. Write a function length(word) that takes in a string (or number), counts how many characters it has, and returns the result as an integer.
def length(word):
    """Takes in a string (or number), counts how many characters it has, and returns the result as an integer."""
    return len(str(word))

9) Rectangle Area
Chip and Jo have designed an interior design tool that needs area calculations and you've been hired to help. Write a function area(width, height) that takes two values (strings or ints), multiplies them, and returns the result as an integer.
def area(width, height):
    """Takes two values (strings or ints), multiplies them, and returns the result as an integer."""
    return int(width) * int(height)

10) Username Generator
A website you're working on automatically creates usernames from a first initial and a last name. Write a function make_username(first, last) that takes two strings, a first and last name, builds the username in all lowercase, and returns it to the user in the message "Your username is: ."
def make_username(first, last):
    """Takes two strings, a first and last name, builds the username in all lowercase."""
    username = (first[0] + last).lower()
    return f"Your username is: {username}."

