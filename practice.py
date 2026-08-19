# imports
import sys  # I used it to check the version of Python I am using
import random  # works for generating random numbers
from datetime import datetime  # works with date and time, formatting and whatnot
import keyword  # used for checking if the content of a string is a keyword
from collections import deque  # for queuing
from contextlib import (
    suppress,
)  # stops the program from raising an Error mostly while using a context manager
from my_billing_package import billing  # a user-defined/custom module
from typing import Optional  # for making a type optional
import threading  # for I/O-bound tasks, creates threads (concurrency)
import multiprocessing  # for CPU-bound tasks, allows multiple tasks to run concurrently
import time  # # I used to simulate a delay in an operation. Used alongside threading threading and multiprocessing
import numpy as np  # for multi-dimensional arrays and fast numerical computations
import pandas as pd  # for working with tabular data, structured data manipulation and analysis
from sklearn.linear_model import LogisticRegression  # for machine learning

print(f"The current version of Python you are using is {sys.version}")  # version
print(
    f"Current date and time (with timezone) is {datetime.now()}"
)  # working with date and time
print(
    f"A random 6-digit number generated: {random.randrange(100000, 1000000)}"
)  # random number


"""
    NB:
        It's very important to note that the logical operators in Python are very different syntactically compared to languages like JS and Go. They are:

        S/N     Operator            Python              JS/Go
        01.       AND                and                 &&
        02.       OR                 or                  ||
        03.       NOT                not                 !
    
    To get day name you need to: from datetime import datetime
    datetime.now().strftime("%A") get the full day e.g Monday
    datetime.now().strftime("%a") get the short day e.g Mon

    
"""

"""
    Control flow:
        1. Conditionals 
            a. if...else (with elif)
            b. match - similar to the switch statement in JS
"""


def practice_conditional():

    # getting user's input and converting to an integer
    try:
        age = int(input("Enter your age, dear user: "))

    # gracefully handling error if user did not enter a number
    except ValueError:
        print("You have to input a whole number. Try again")
        # recursion
        return practice_conditional()

    # returning a response to the user
    if age >= 60:
        return "Your age is {}, you are a senior citizen".format(age)
    elif age >= 35:
        return "You are {} years old! You are fully grown adult".format(age)
    elif age >= 20:
        return "You're {} years old. You are a young adult".format(age)
    elif age >= 13:
        return "You are {} years old, you are a teenager!".format(age)
    elif 0 < age <= 12:
        return "You are very young, you are not even a teenager"
    else:
        return "Please enter a valid age"


print(practice_conditional())

day_name = datetime.now().strftime("%A")

# match practical
match day_name:
    case "Monday":
        print("Today is Monday")
    case "Tuesday":
        print("Today is Tuesday")
    case "Wednesday":
        print("Today is Wednesday")
    case "Thursday":
        print("Today is Thursday")
    case "Friday":
        print("Today is Friday")
    case "Saturday":
        print("Today is Saturday")
    case "Sunday":
        print("Today is Sunday")
    case _:
        print("There's no present day")


count = 1
while count < 11:
    print(count)
    count += 1
else:
    print(f"Count is now greater than 10.")

countries = [
    "Algeria",
    "Bulgaria",
    "China",
    "Denmark",
    "Egypt",
    "Finland",
    "Guinea-Bissau",
    "Hungary",
    "Iceland",
    "Japan",
    "Kenya",
    "Liberia",
    "Morocco",
    "Niger",
    "Oman",
    "Portugal",
    "Qatar",
    "Russia",
    "Sudan",
    "Thailand",
    "Ukraine",
    "Vietnam",
    "Wales",
    "X",
    "Yemen",
    "Zimbabwe",
]

cities = ["Accra", "Benin City", "Cologne", "Dakar", "El Paso", "Florence"]


for country in countries:
    print(
        f"An example of a country that starts with letter {country[0:1]} is {country}"
    )

print("Peru" not in countries)

"""
    isinstance(data, type) checks if a data is of that particular datatype returns a bool value. E.g: isinstance(5, int) checks if 5 is an integer.

    all() checks through the list bool values and make sure everything is true before it can return true:
        

"""


# Unpacking lists and dictionaries as a function argument
def list_add(numbers):
    # validating if the data passed is not empty and it contains only integers and floats
    if (
        not numbers
        or not isinstance(numbers, list)
        or not all(isinstance(number, (int, float)) for number in numbers)
    ):
        return "Enter a list of numbers!"

    sum = 0

    for number in numbers:
        sum += number

    return f"The sum total of the numbers are {sum}"


print("Line 122:", list_add(9))
print("Line 123:", list_add([9, 7, 5, 6.8]))
print(list_add("you"))

my_word = "even"

answer = (
    f"This is a keyword: {my_word}."
    if keyword.iskeyword(my_word)
    else f"{my_word} is not a keyword."
)
print(answer)


# normal function
def calculate_tax(price):
    return price + 0.50


print(calculate_tax(5))


# lambda function
lambda_tax = lambda tax: tax + 0.50

print(lambda_tax(5))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# transforming the list by doubling each value
lambda_doubled = map(lambda number: number * 2, numbers)
print("The list doubled:", list(lambda_doubled))

# filtering the list to only return even numbers
lambda_even_numbers = filter(lambda number: number % 2 == 0, numbers)
print("The list of even numbers:", list(lambda_even_numbers))

customers_orders = [
    {"name": "Mat", "ordered": ["coffee", "latte", "burger"], "price": 300.67},
    {
        "name": "Theresa",
        "ordered": [
            "coffee",
            "latte",
            "burger",
            "chocolate",
            "ice cream",
            "cotton candy",
            "milkshake",
            "latte",
            "burger",
        ],
        "price": 19500.99,
    },
    {
        "name": "Josh",
        "ordered": ["pancakes", "milkshake", "chocolate", "cotton candy"],
        "price": 560.80,
    },
]

# sorting the dictionary using sorted and key
sorted_by_order_number = sorted(customers_orders, key=lambda order: order["price"])

print(
    "Sorting the order by the number of orders in ascending order:",
    sorted_by_order_number,
)


menu_items = [
    {"name": "Mocha", "price": 5.00},
    {"name": "Espresso", "price": 3.50},
    {"name": "Latte", "price": 4.50},
]

# Sort the items based on their price dictionary key
sorted_by_price = sorted(menu_items, key=lambda item: item["price"])
print(sorted_by_price)

# Using the start, stop, step syntax in slicing
original_list = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
    130,
    140,
    150,
    160,
    170,
    180,
    190,
    200,
]

reversed_list = original_list[::-1]  # this reverses the list
print("Reversed list:", reversed_list)

skip_by_one_list = original_list[
    ::2
]  # this returns the whole list in the normal order but always skip the second item
print("Skipped by one list:", skip_by_one_list)

divided_list = list(map(lambda number: number // 2, original_list))
print("Divided numbers' list:", divided_list)

filtered_list = list(filter(lambda number: number % 3 == 0, original_list))
print("Filtered numbers' list:", filtered_list)


def int_converter(value):
    value = float(value)
    return isinstance(value, float)


print(int_converter("76"))


# Finding and returning the largest number in a group.
print("The largest number is", max(45, 890, 64, 712, 10785, 845314))

technologies = [
    "HTML",
    "CSS",
    "JavaScript",
    "React.js",
    "Next.js",
    "Tailwindcss",
    "Node.js",
    "Express.js",
    "WordPress",
    "Framer",
]

technologies.append("Python")  # adding Python to the end of the list
print(technologies)
technologies.append("Java")
technologies.append("Rust")
print(technologies)

technologies.pop(-1)
print(technologies)

technologies.remove("Java")
print(technologies)

technologies.sort()
print(technologies)

# creating a new list with list comprehensions instead of using a lambda function with the map function
squares = [x**2 for x in range(1, 11)]
print(squares)

# filtering a list and returning a new list of items that match the condition instead of using a lambda function with the filter function
filtered_squares = [x for x in squares if x > 13 and x < 60]
print(filtered_squares)


### tuples
my_tuple = (
    "Rice",
    "Beans",
    "Semo",
    "Pounded Yam",
    "Spaghetti",
    "Noodles",
    "Yam",
)
print(type(my_tuple))
print(my_tuple[0])
# my_tuple[0] = "Garri" # this will return an error

dimensions = (34, 48, 54)
# width, height = dimensions # this returns an error
width, height, breadth = (
    dimensions  # unpacking the values in the tuple. You must have the number of variables matching the exact number of items in the tuple
)
print(width)
single_tuple = ("Sports",)  # the comma makes the computer know it's a tuple
print(type(single_tuple))

my_dict = {
    "first_name": "Ayodeji",
    "last_name": "Aronimo",
    "address": "Off Ikere Rd, Ado, Ekiti State.",
}
my_dict["profession"] = "Software Development"
print(my_dict["first_name"])
print(my_dict)

print("first_name" in my_dict)


def dict_checker(query, dict):
    if not query in dict:
        return f"Cannot find {query} in the dictionary!!! ⚠️"

    return dict[query]


print(dict_checker("middle_name", my_dict))

# using the get() method to safely return a value in a dict
print(my_dict.get("surname", "Doesn't exist!"))
print(my_dict.get("last_name", "Doesn't exist!"))

my_set = {
    "rice",
    "beans",
    "garri",
    "sugar",
    "spaghetti",
}  # a set
print(my_set)

empty_set = set()  # this creates an empty set, {} will create an empty dict

my_second_set = {"beans", "potato", "spaghetti", "sugar", "rice", "noodles"}

union_set = (
    my_set | my_second_set
)  # union = creates a new set with only the unique values(i.e values that only appearing in one set)
print(union_set)

intersected_set = (
    my_set & my_second_set
)  # intersection = creates a new set with only values appearing in both sets
print(intersected_set)

print(my_set - my_second_set)

set_cities = {"Accra", "Abidjan", "Ankara"}
set_cities.add("Abuja")  # adds an item
print(set_cities)

more_cities = ["Athens", "Algiers", "Alexandria", "Antwerp"]
set_cities.update(more_cities)  # adds an iterable
print(set_cities)


# Object-Oriented Programming (OOP)
# creating an empty cls
class EmptyClass:
    pass


print(EmptyClass)
first_empty_class = EmptyClass()
print(type(first_empty_class))


class CoffeeCup:
    # the constructor runs immediately an object is stamped out
    def __init__(self, owner, size):
        self.owner = owner
        self.size = size
        self.content = "empty"


first_coffee_cup = CoffeeCup("Alice", "large")
print(first_coffee_cup.size)  # accessing a value from the object

first_coffee_cup.content = "Espresso"  # modifying a value from the object


class Student:
    # initialization
    def __init__(
        self,
        first_name: str,
        last_name: str,
        matric_no: str,
        department: str,
        graduation_year: int,
        middle_name: str = "",
    ):
        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()
        self.middle_name = middle_name.strip().title() or ""
        self.email = f"{self.first_name}{self.last_name}@talentnation.io".lower()
        self.matric_no = matric_no
        self.faculty = ""
        self.department = department
        self.graduation_year = graduation_year

    # the representation data (shows how the object should be created; for developers)
    def __repr__(self):
        return f"Student(first_name = '{self.first_name}', middle_name = '{self.middle_name}', last_name = '{self.last_name}', matric_no = '{self.matric_no}', department = '{self.department}', graduation_year = {self.graduation_year})"

    # the layman-readable summary of the object
    def __str__(self):
        return f"First Name: {self.first_name} \nMiddle Name: {self.middle_name} \nLast Name: {self.last_name} \nEmail: {self.email} \nMatriculation Number: {self.matric_no} \nDepartment: {self.department} \nYear of Graduation: {self.graduation_year}"

    # creating an instance method
    def get_metric_no(self):
        return f"{self.first_name}{'' if self.middle_name == '' else ' ' + self.middle_name} {self.last_name} matriculation number is {self.matric_no}"


first_student = Student(
    first_name="John",
    last_name="Doe",
    matric_no="TN15678",
    department="AI Software Engineering",
    graduation_year=2028,
)

print(repr(first_student))
print(first_student)
print(first_student.get_metric_no())

second_student = Student(
    first_name="Pamela",
    middle_name="Chika",
    last_name="Peters",
    matric_no="TN76843",
    department="Data Engineering",
    graduation_year=2030,
)
print(second_student)
print(second_student.get_metric_no())


# inheritance
# child class
class PremiumStudent(Student):
    # configuring the instantiation process
    def __init__(
        self,
        first_name: str,
        last_name: str,
        matric_no: str,
        department: str,
        graduation_year: int,
        tuition_fee: float,
        middle_name: str = "",
    ):
        # super() method that helps to execute a parent class attribute when the child class is overriding it
        super().__init__(
            first_name=first_name,
            last_name=last_name,
            matric_no=matric_no,
            department=department,
            graduation_year=graduation_year,
            middle_name=middle_name,
        )
        self.tuition_fee = float(tuition_fee)

    # inheriting and modifying the str method
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} \nTuition Paid: {self.tuition_fee}"

    def __repr__(self):
        parent_repr = super().__repr__()
        return f"{parent_repr[:-1]}, tuition_fee = {self.tuition_fee})"


first_premium_student = PremiumStudent(
    first_name="Christianah",
    last_name="Adema",
    matric_no="TN90521",
    department="MLOps Engineering",
    graduation_year=2027,
    tuition_fee=600000,
)

print(repr(first_premium_student))


# stacking
class Cupboard:
    def __init__(self):
        self._cup = []

    # representation
    def __repr__(self):
        return f"Cupboard()"

    # informational
    def __str__(self):
        content = (
            f"\n{'\n'.join(self._cup)}"
            if len(self._cup) >= 1
            else "Cupboard is currently empty"
        )
        return f"The cupboard's content: {content}"

    # add a new item (last in)
    def add_cup(self, cup):
        self._cup.append(cup)

    # actual stacking logic
    # last in first out
    def remove_cup(self):
        # checking if cup is empty
        if self.is_empty():
            print("Action Blocked: Cup is currently empty!")
            return None
        # remove the last item
        else:
            self._cup.pop()

    def is_empty(self):
        return len(self._cup) == 0


first_cup = Cupboard()
print(first_cup)
print(repr(first_cup))
first_cup.remove_cup()
first_cup.add_cup("Glass Cup")
print(first_cup)
first_cup.add_cup("Mug Cup")
first_cup.add_cup("Stainless Cup")
first_cup.add_cup("Cardboard Cup")
print(first_cup)


# queuing (with inheritance)
class CupQueue(Cupboard):

    # queuing actual logic
    def remove_cup(self):
        if self.is_empty():
            print("Action Blocked: Cup container is already empty!")
            return None
        else:
            self._cup.pop(0)


first_queue_cup = CupQueue()
print(first_queue_cup)
first_queue_cup.add_cup("A cup")
first_queue_cup.add_cup("Another cup")
first_queue_cup.add_cup("A new cup")
print(first_queue_cup)
first_queue_cup.remove_cup()
print(first_queue_cup)

# queuing using an object from collections module
queue = deque()

# add from behind
queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")
queue.appendleft("Task 0")  # add to the front of the queue
print(queue)

queue.pop()  # remove from behind: last in first out
queue.popleft()  # remove from the front: first in
print(queue)

# step-by-step implementation of a linked list


# step 1: building the class
class FellowOnMyTable:
    def __init__(self, name):
        self.fellow_name = name
        self.next = None  # defaults to empty

    def __str__(self):
        return f"The fellow's name is {self.fellow_name}"


first_fellow = FellowOnMyTable("Ayodeji")
second_fellow = FellowOnMyTable("Abiodun")
third_fellow = FellowOnMyTable("Elizabeth")
fourth_fellow = FellowOnMyTable("Heritage")


print(first_fellow)

# step 2: linking the list by using the next to point to the next object(node) in the list
first_fellow.next = second_fellow
second_fellow.next = third_fellow
third_fellow.next = fourth_fellow

print(
    first_fellow.next
)  # getting the next node (__str__ method) that follows the current fellow
print(second_fellow.next.fellow_name)  # getting the exact name of the next fellow


# step 3: building the linked list manager class
class FellowChain:
    def __init__(self):
        self.head = None

    # def append(self, name):


# BST
# step 1: building the node class
class Order:
    def __init__(self, price):
        self.price = float(price)
        self.left = None
        self.right = None


first_order = Order(4.56)
print(first_order.left)
print(first_order.right)


# step 2: creating the sorting rule
def insert(node, price):
    # base case: if we reach an empty spot, stamp out a new node here
    if node is None:
        return


# BST (from claude.ai)
class Node:  # A "Node" is one box in the tree
    def __init__(self, value):  # This runs automatically when we create a new Node
        self.value = value  # Store the number/data this node holds
        self.left = None  # Pointer to left child — starts empty (no child yet)
        self.right = None  # Pointer to right child — starts empty (no child yet)


class BST:  # The "BST" class manages the whole tree
    def __init__(self):  # Runs automatically when we create a new tree
        self.root = None  # The tree starts empty — no root node yet

    def insert(self, value):  # Public method to add a new value to the tree
        if self.root is None:  # Check: is the tree completely empty?
            self.root = Node(value)  # If yes, this new value becomes the root
            return  # Done — nothing more to do
        current = self.root  # Otherwise, start looking from the root
        while True:  # Keep looping until we place the node
            if value < current.value:  # Is our new value smaller than the current node?
                if current.left is None:  # If there's no left child yet...
                    current.left = Node(value)  # ...attach the new node here
                    return  # Done — stop the loop
                current = (
                    current.left
                )  # Otherwise, step down to the left child and repeat
            else:  # Value is bigger (or equal) to current node
                if current.right is None:  # If there's no right child yet...
                    current.right = Node(value)  # ...attach the new node here
                    return  # Done — stop the loop
                current = (
                    current.right
                )  # Otherwise, step down to the right child and repeat

    def contains(self, value):  # Public method to check if a value exists in the tree
        current = self.root  # Start looking from the root
        while (
            current is not None
        ):  # Keep going as long as we haven't fallen off the tree
            if value == current.value:  # Does the current node match what we want?
                return True  # Yes! Found it
            elif value < current.value:  # Is our target smaller than the current node?
                current = current.left  # Move to the left child
            else:  # Otherwise, target must be bigger
                current = current.right  # Move to the right child
        return False  # Loop ended without finding it — value isn't in the tree

    def inorder(self):  # Public method to get all values sorted, smallest to largest
        result = []  # Empty list to collect values as we find them
        self._inorder(self.root, result)  # Start the recursive walk from the root
        return result  # Give back the completed sorted list

    def _inorder(
        self, node, result
    ):  # Helper method (the underscore means "internal use")
        if node:  # Only do something if this node actually exists
            self._inorder(
                node.left, result
            )  # First, visit everything to the LEFT (smaller values)
            result.append(node.value)  # Then, record THIS node's value
            self._inorder(
                node.right, result
            )  # Finally, visit everything to the RIGHT (bigger values)


# ---- Example usage ----
tree = BST()  # Create a new, empty tree
for num in [8, 3, 10, 1, 6]:  # Loop through a list of numbers to insert
    tree.insert(num)  # Insert each one into the tree, one at a time

print(tree.contains(6))  # Search for 6 → prints True (it's in the tree)
print(tree.contains(5))  # Search for 5 → prints False (not in the tree)
print(tree.inorder())  # Print all values sorted → [1, 3, 6, 8, 10]


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def details(self):
        print(f"This car is a {self.brand} {self.model} {self.year}")


c1 = Car("Mercedes-Benz", "G-Wagon", 2026)
c1.details()

create_password = ""
confirm_password = ""


def password_creator():
    global create_password
    global confirm_password

    create_password = input("Create your password: ")
    confirm_password = input("Confirm your password: ")

    if create_password == confirm_password:
        print("Password created successfully!")
    else:
        print("Password do not match! Try again")
        password_creator()  # recursion


password_creator()

password_attempts = 1


def password_checker(created_password):
    password = input("Enter your password: ")
    global password_attempts

    if password != created_password:
        # a nested condition
        if password_attempts >= 5:
            print("You have tried five times, try again later!")
        else:
            print("Access denied! Try again.")
            password_attempts += 1
            password_checker(create_password)

    else:
        print("Access granted!")


password_checker(create_password)

# iterators and iterables
proteins = [
    "Ponmo",
    "Shaki",
    "Titus",
    "Pork",
]  # iterable
proteins_iterator = iter(proteins)  # iterator

print(type(proteins))
print(type(proteins_iterator))

print(next(proteins_iterator))
print(next(proteins_iterator))
print(next(proteins_iterator))
print(next(proteins_iterator))
# print(next(proteins_iterator))


# creating custom iterators
class CustomIterator:
    # dunder method to run when instantiating the object
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    # turning the object to an iterator
    def __iter__(self):
        return self

    # logic to always move to the next item in the iterable and stopping when it gets to the end of the iterable
    def __next__(self):
        # checking if it hasn't gotten to
        if self.current < self.limit:
            result = self.current  # saving the current item in a temporary variable
            self.current += 1  # moving to the next item in the iterable
            return result  # returning the current item
        # stopping the iteration when it gets to the end of the iterable
        else:
            raise StopIteration


# printing numbers
for num in CustomIterator(5):
    print(num)


# iterating a str and a list
favourite_movie_genre = "Action"
afrobeats_artistes = ["Seyi Vibez", "Fireboy", "Olamide", "Phyno"]

for i in CustomIterator(len(favourite_movie_genre)):
    print(favourite_movie_genre[i])

for i in CustomIterator(len(afrobeats_artistes)):
    print(afrobeats_artistes[i])


# generators (uses yield instead of return) and yields
def name_generator():
    yield "Ayodeji"
    yield "Aronimo"


print(
    "Memory Address of a generator:", name_generator()
)  # this only returns the memory address of the function
gen = name_generator()
print("Next item in the function:", next(gen))  # returns the next yield
print("Next item in the function:", next(gen))  # returns the next yield


def countdown(n):
    while n > 0:
        yield n
        n -= 1


cd = countdown(5)
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))


def generator_size(n):
    count = 1
    while count <= n:
        yield n
        count += 1


print(sys.getsizeof(generator_size(1000000)))


def get_orders_generator(n):
    for i in range(n):
        yield f"Order #{i}"


# Instantly returns a generator object using almost zero memory
massive_gen = get_orders_generator(1000000)
print(sys.getsizeof(massive_gen))


def get_orders_list(n):
    orders = []
    for i in range(n):
        orders.append(f"Order #{i}")
    return orders


# Generates 1,000,000 items in memory all at once
massive_list = get_orders_list(1000000)
print(f"Memory size: {sys.getsizeof(massive_list)} bytes")


# yield from (for connecting sub-generators to a generator)
# first sub-generator
def morning_shift():
    yield "Murewa"
    yield "Ayobami"
    yield "Tolulope"


# second sub-generator
def afternoon_shift():
    yield "Christianah"
    yield "Heritage"
    yield "Elizabeth"


# third sub-generator
def evening_shift():
    yield "Abiodun"
    yield "Ayodeji"
    yield "Elohor"


# consolidating them all in a single generator
def rooster():
    yield from morning_shift()
    yield from afternoon_shift()
    yield from evening_shift()


for on_duty in rooster():
    print(on_duty)


# sub-generator
def payroll():
    yield {"name": "Murewa", "role": "Software Engineering Intern", "pay": 350000}
    yield {"name": "Ayobami", "role": "System Engineer", "pay": 2300000}
    yield {"name": "Tolulope", "role": "AI/ML Engineer", "pay": 2350000}
    yield {"name": "Christianah", "role": "Full-stack Developer", "pay": 1910000}
    yield {"name": "Heritage", "role": "Product Designer", "pay": 1050000}
    yield {"name": "Elizabeth", "role": "Cybersecurity Expert", "pay": 2250000}
    yield {
        "name": "Abiodun",
        "role": "Cloud Computing and System Engineer",
        "pay": 3200000,
    }
    yield {"name": "Ayodeji", "role": "AI Agent and System Engineer", "pay": 3500000}
    yield {
        "name": "Elohor",
        "role": "Brand Strategist and Full-stack Developer",
        "pay": 2500000,
    }


# sub-generator
def calculate_salary(stream):
    for employee in stream:
        employee["salary"] = employee["pay"] - (employee["pay"] * 0.05)
        yield employee


# sub-generator
def receipt_formatter(stream):
    for employee in stream:
        yield f"Employee: {employee['name'].capitalize()} \nRole: {employee['role']} \nSalary: ₦{employee['salary']:.2f}\n"


# chaining the generators
payroll_list = payroll()
salary_calculation = calculate_salary(payroll_list)
generate_receipt = receipt_formatter(salary_calculation)

# generating the receipt
for receipt in generate_receipt:
    print(receipt)


# functions can be assigned to variables
def greeting(name):
    return f"Hello {name.title()}!"


say_hello = greeting

print(say_hello("Alice"))


# functions can be passed as an argument
def say_hello(name):
    return f"Hello, {name}!!!"


def say_goodbye(name):
    return f"Goodbye, {name}!!!"


def shout(speaker, name):
    return speaker(name).upper()


print(shout(say_hello, "Bob"))  # Output: HELLO, BOB!
print(shout(say_goodbye, "Bob"))  # Output: GOODBYE, BOB!


# functions can be returned from a functions
def make_adder(n):
    def adder(x):
        return x + n

    return adder


add_5 = make_adder(5)
print(add_5(3))  # Output: 8


# building a decorator
def decorator_function(func):
    # the function wrapper
    def wrapper():
        print("Hi, this is happening right BEFORE the function runs!")
        # executing the first-class function
        func()
        print("Hi, this is happening right AFTER the function runs!")

    # invoking the wrapper function
    wrapper()


def run_func():
    print("Function was executed!")


decorator_function(run_func)


# using the @syntax and also using a func that accepts an argument
def function_decorator(func):
    # passing positional arguments and/or keyword arguments
    def wrapper(*args, **kwargs):
        print("Na wetin dey sup before the function run ooo!!!")
        result = func(*args, **kwargs)
        print("Na wetin wan sup after the function run 000!!!")
        return result

    return wrapper


# adding the decorator
@function_decorator
def name_separator(name):
    name = list(name)
    name = " ".join(name)

    return name


print(name_separator("Peters"))

# content management
# writing a file with content management
with open("content.txt", "w") as file:
    file.write("This was written with the content management!")
    print("Content written successfully!")


# reading a file with content management
with open("content.txt", "r") as file:
    content = file.read()
    print(content)

# working with multiple files (content manager)
with open("input.txt", "r") as in_file, open("output.txt", "w") as out_file:
    content = in_file.read()
    out_file.write(content.upper())
    print("Both files have been closed successfully!")

# suppressing exceptions
with suppress(FileNotFoundError):
    # this file does not suppress but the program will not crash when it attempts to read it:
    with open("missing.txt", "r") as file:
        data = file.read()
    # no exception is raised if the file is missing


# creating custom content management

#
base_cost = billing.calculate_subtotal(2000, 8)
final_amount = billing.apply_discount(base_cost, 0.15)
receipt = billing.format_receipt("Joshua", final_amount)

print(receipt)

# static typing

# dropping hints


def count_alpha(content: str) -> int:
    count = 0

    # guard clause
    if len(content) == 0:
        return count

    # checking for alphabets and counting 'em
    for char in content:
        if char.isalpha():
            count += 1

    return count


print("The number of alpha counts:", count_alpha("25huoq90i"))

# Exception Handling with try/except


def teams_designator() -> dict:
    # docstrings
    """
    This is a function that gets the number of contestants and creates the number of teams of two you can create with the contestants and return the team names.
    """
    try:
        no_of_contestants = int(input("Enter the number of contestants: "))
    except ValueError:
        return f"Invalid number!"

    # guard clauses
    if no_of_contestants % 6 != 0:
        return f"There is at least one contestant who doesn't have a team. A team must have exactly six members"

    # getting the number of teams and creating teams
    no_of_teams = no_of_contestants // 6  # returning an int
    teams = [f"Team {team + 1}" for team in range(no_of_teams)]

    return {
        "no_of_contestants": no_of_contestants,
        "no_of_teams": no_of_teams,
        "teams": teams,
    }


print(teams_designator())


# threading
def save_task(task):
    print(f"[{task} saving...] Wait for a while")
    time.sleep(5)
    print(f"[{task} saved] You can move on to other things")


# creating threads
thread1 = threading.Thread(target=save_task, args=("Build client-side application",))
thread2 = threading.Thread(
    target=save_task, args=("Create server and set up database",)
)
thread3 = threading.Thread(
    target=save_task, args=("Connect server-side logic to client-side application",)
)

# starting the thread (i.e. executing the code concurrently)
thread1.start()
thread2.start()
thread3.start()

# joining(chaining) the threads together
thread1.join()
thread2.join()
thread3.join()


# using NumPy
prices = np.array([345, 679, 102, 225, 1383, 903, 543, 760])
discounts = (
    prices * 0.8
)  # this implicitly multiplies every item in the array with 0.8 and return the result
print(discounts)

# using Pandas
df = pd.read_csv("./assets/datasets/MOCK_DATA.csv")
Mock_Data = df.head()
print(Mock_Data)


# using scikit-learn (sklearn)
model = LogisticRegression() # initializing the model
# model.fit(X_train, y_train) # training the model
# prediction = model.predict(X_test)

# print(prediction)

print(id(Mock_Data)) # introspection, checking for it's unique identifier

# right-angle triangle
for i in range(6):
    print("*" * i)