# Learning Python (Talent Nation)

## Call Stack
The call stack is how Python remembers where to return the execution after each *return* call.

### Redirecting Output
You can use this command *py file_name.py > output.txt* to write the output of your program in a file and not your terminal but this overwrites everything else in the file. If you want to append the new content without overwriting the old content, run  *py file_name.py >> output.txt*. Use this command to write both output and error in the file *py file_name.py > output.txt 2>&1*.

### Checking the output of a program
You can query the exit status of the last executed command in your terminal using the special shell variable $?:
*echo $?*

If it returns 0, that means the program was successful. Anything other than 0, means the program wasn't successful.

## Lambda function
A lambda function (almost like an arrow function in JS) is a compact, anonymous function that is not defined with the *def* keyword that is used for quick tasks. You need to use the keyword *lambda* to start the function and also use the keyword again just before the variable you would be using inside the lambda function
E.g:
def calculate_tax (price):
    return price + 0.50

You can do the same thing this way: 
    lambda_tax = lambda tax: tax + 0.50


*:* returns the evaluation of (tax + 0.50) and places it into the variable called lambda tax.
We have to use the list() to make it understandable when we use functions like map(), filter(), because they use lazy generators to produce output. 

**List Comprehensions** are better used when creating a new list that is going to have transformed or filtered data.

## Important Things To Note
NB:
    It's very important to note that the logical operators in Python are very different syntactically compared to languages like JS and Go. They are:

    S/N     Operator            Python              JS/Go
    01.       AND                and                 &&
    02.       OR                 or                  ||
    03.       NOT                not                 !
    
    To get day name you need to: from datetime import datetime
    datetime.now().strftime("%A") get the full day e.g Monday
    datetime.now().strftime("%a") get the short day e.g Mon

## Slicing with lists
1. Start (Where to begin)
This is the index number of the first block you want to pick up.
* Remember: Python starts counting at 0.
* If you leave it blank, Python automatically starts at the very first block (index 0). 

2. Stop (Where to finish)
This is the index where you want to stop cutting.
* Crucial Rule: Python stops before this number. It never includes the stop block itself.
* If you leave it blank, Python goes all the way to the very end of the list. 

3. Step (The stride size)
This tells Python how many steps to take to reach the next block.
* 1 means: Move forward 1 block at a time (pick every block).
* 2 means: Move forward 2 blocks at a time (skip every other block).
* -1 means: Walk backward 1 block at a time (reverse).


## Common List Methods
1. list.append(item): adds the new item to the end of the list.
2. list.index(item): returns the index position of the item.
3. list.pop(index): removes an item with the tallying index number. If none was provided, it removes the last one.
4. list.remove(item): removes the very first item that matches that value. It reads the items from left to right.
5. list.insert(item, index): adds a new item to the list based on the index position.
6. list.reverse(): reverses the order and arrangement of the list, the first becomes the last and vice versa.
7. list.count(item): returns the number of times the item appears in the list.
8. list.sort(): rearranges the list alphabetically or numerically.

## Collections
1. List = Ordered, mutable and indexed. Allows duplicate values, initialized using *[]*. 
    E.g. my_list = ["rice", "beans", "garri", "sugar"]

2. Tuple = Ordered, immutable (locked-in values), and indexed. Allows duplicate values, initialized using *()*. 
    E.g. my_tuple = ("rice", "beans", "garri", "sugar") # multiple-value tuple
    my_single_tuple = ("rice",) # use the trailing comma for a single value tuple or else the computer would mistake it as a string.

3. Dict = Unordered, mutable, and not indexed. Doesn't allow duplicate values, initialized using *{}*. Stores data in key/value pairs. 
    E.g. my_dict = {"rice": 240, "beans": 200, "garri": 50, sugar: 50}

4. Set = Unordered, immutable values, and not indexed. Doesn't allow duplicate values, initialized using *{}* as well but doesn't store data in pairs, therefore no need for colon :
    E.g. my_set = {"rice", "beans", "garri", "sugar"}


### Set Operations
1. Union = combines the unique values in two sets into a new set. Operator: **|**
2. Intersection = keeps the similar values in two sets in a new set. Operator: **&**
3. set.add(item) = adds a new item to the set.
4. set.update(iterable) = unpacks the items of an iterable e.g. lists, tuples, and strings and adds individual item to the set.


### Object-Oriented Programming (OOP)
1. Class = a standardized blueprint or template that defines the structure and attributes of an object.
2. Object = a concrete individual item built from a class template.
3. Attribute = a variable or property associated with a specific object, holding a piece of its data.
4. __init__ method = a special constructor function inside a class that automatically runs to initialize an object's attributes when it is created.
5. self = a keyword inside a class that refers directly to the specific individual object currently being created or modified.


### Linked Lists
A linked list is a linear data structure where elements are not stored in contiguous, numbered memory slots. Instead, each element is a self-contained object (called a **NODE**) that contains its own data and a pointer link (called /**next**/) that points directly to the next node in the chain.

#### Key Concepts
1. Node = a self-contained object that acts as a single link in a linked list, containing data and a reference to the next node
2. Pointer = an attribute inside a node that stores the memory address of the /*next* node in the sequence.
3. Head = a reference pointer that tracks the first node in a linked list. If the list is empty, the head is None.
4. Traversal = the process of starting at the **head** node and following the /*next* pointers step by step to read or modify each item.
5. Broken Link (Memory Leak) = an error where a pointer is overwritten before its downstream connections are saved, causing these objects to be lost in memory.


### Advanced Data Structure and Algorithm (DSA) with Python

1. 


### Generators and Yields
In simple terms, a **/*generator*/** is a function with a pause button while a **/*yield*/** is that pause button. A generator in Python is a special type of function that produces a sequence of values over time, rather than returning them all at once.
**Lazy Evaluation** is a performance strategy where values are computed only at the exact moment they're requested, rather than pre-computing them all at once.

### Decorators
Decorators in Python, are tools that let you wrap a function inside another function. They allow you to inject extra code before and after your original function runs without modifying your original code.