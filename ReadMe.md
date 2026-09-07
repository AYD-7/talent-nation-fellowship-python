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


## Object-Oriented Programming (OOP)
1. Class = a standardized blueprint or template that defines the structure and attributes of an object.
2. Object = a concrete individual item built from a class template.
3. Attribute = a variable or property associated with a specific object, holding a piece of its data.
4. __init__ method = a special constructor function inside a class that automatically runs to initialize an object's attributes when it is created.
5. self = a keyword inside a class that refers directly to the specific individual object currently being created or modified.


### Linked Lists
A linked list is a linear data structure where elements are not stored in contiguous, numbered memory slots. Instead, each element is a self-contained object (called a **NODE**) that contains its own data and a pointer link (called **next**) that points directly to the next node in the chain.


#### Key Concepts
1. Node = a self-contained object that acts as a single link in a linked list, containing data and a reference to the next node
2. Pointer = an attribute inside a node that stores the memory address of the *next* node in the sequence.
3. Head = a reference pointer that tracks the first node in a linked list. If the list is empty, the head is None.
4. Traversal = the process of starting at the **head** node and following the *next* pointers step by step to read or modify each item.
5. Broken Link (Memory Leak) = an error where a pointer is overwritten before its downstream connections are saved, causing these objects to be lost in memory.


## Advanced Data Structure and Algorithm (DSA) with Python

1. 


## Generators and Yields
In simple terms, a **/*generator*/** is a function with a pause button while a **/*yield*/** is that pause button. A generator in Python is a special type of function that produces a sequence of values over time, rather than returning them all at once.
**Lazy Evaluation** is a performance strategy where values are computed only at the exact moment they're requested, rather than pre-computing them all at once.


## Decorators
Decorators in Python, are tools that let you wrap a function inside another function. They allow you to inject extra code before and after your original function runs without modifying your original code.


## Module and Import
A package is just directory contains several modules, have this file named "__init__.py" in your director. This combines all the modules into a single package. You need to use this method to import any module from the package:

    from my_pkg import my_module
  
This imports the whole module from that package but if you want to import a specific function from the module, use this:

    from my_pkg.my_module import my_function


## Packages and PyPI
PyPI (short for Python Package Index) is a giant library for Python code (similar to the npm repository in JavaScript). You use pip (similar to npm in JS) to install a package. 
* If you want to make HTTP requests, use *requests*
* If you want to work with data, use *pandas*
* If you want to build a web app, use *flask* or *django*
* If you want to make API calls, use *httpx* 

### Key Commands to note:
* To install a package, run *pip install package_name*
* To check the list of packages you have installed, run *pip list*
* To show a particular package and information, run *pip show package_name*
* To upgrade a package, run *pip install --upgrade package_name*
* To get all the installed packages and their files and save the into a file, run *pip freeze > requirements.txt*
* To install all the packages in the requirements.txt file,  run *pip install -r requirements.txt*


## Virtual Environments and $PATH
Virtual Environments in Python allow you to create "isolated" toolboxes(environment) which have their own Python interpreter. The reason why we have virtual environment is because your project can need a particular version of Python while another project needs a different version.

### Key Concepts
* venv = the Python module that allows you to create virtual environments
* $PATH = an environment variable that tells your shell where to find executable program.
* Activation = the process of making Python make use of your virtual environment's Python and not the system's Python.
* Deactivation = leaving the virtual environment's Python and returning to the system's Python. 
* Shebang = the first line of the script that tells the system which version of the interpreter to use.

To create a virtual environment in a project, go to the project's root directory and run *python -m venv myenv*
This creates a folder named **"myenv"** that gets a copy of the Python interpreter, a copy of pip and creates a clean isolated environment. 

You need to activate the venv, run this command *myenv/Scripts/activate*


## Static Typing
If you want to enforce typing, you can install **mypy** using the command *pip install mypy*. You can use the command *mypy file_name* to run and ensure you followed typing.

## Documentation and Docstrings
A docstring is a string literal inside triple quotes (""") that is placed as the first line of code of a function, module or class explaining its purpose. If you write a string at the very start of these blocks, Python automatically captures it and stores it in the object's *__doc__* attribute. 

You can use the *help()* to view a function's docstring. 

## Threading and GIL
Concurrency - managing multiple tasks at the same time.

### Key Concepts
1. Thread = an independent line of code execution running within a program.
2. GIL (Global Interpreter Lock) = a rule in standard Python that restricts execution so only one thread can run Python code at any single microsecond.
3. I/O bound Task = a task that spends most of its execution time waiting for external connection or hardware
4. CPU-bound Task = a task that spends most of its execution time performing mathematical computations on the computer's processor.
5. Race Condition = a critical bug that occurs when two threads attempt to modify the same variable at the exact same time, causing lost updates.
6. Lock = a synchronization tool used to ensure only one thread can access a shared resource at a time.
7. Daemon Thread = a background thread that is automatically terminated by Python the moment the main program exits.


## Multiprocessing and Asyncio
Threads help with concurrency with I/O-bound tasks but GIL prevents parallel execution on multiple processor cores which are CPU-bound tasks. That's why we have other options that basically help with running concurrency for CPU-bound tasks. They are **Multiprocessing** and **Asyncio**.

1. Multiprocessing = bypasses the GIL totally. Each process has its own isolated Python interpreter and its own independent GIL, allowing true parallel executions across multiple processor cores. preferably  
2. Asyncio = this uses a single thread and an event loop to handle thousands concurrent tasks. Instead of the operating system switching between threads, tasks voluntarily pause when they are waiting. 


## The AI & Data Ecosystem
1. **NumPy** is the foundation of numerical computing in Python. It provides multi-dimensional arrays and a large collection of mathematical functions. Instead of looping through a list of numbers in Python, you can perform direct operations on entire arrays at once.
**NumPy** is the backbone of every numerical work in Python. Pandas is built on top of NumPy  and many machine learning libraries use NumPy arrays.
2. **Pandas** provides a data structure for working with tabular data. It's main structure is the **DataFrame**, which is like a spreadsheet or database table in memory. With **Pandas**, you can load CSV files, filter row(s), group by categories, calculate statistics, and clean missing values.
3. **Matplotlib** and **Seaborn** are libraries that are used for data visualization. You can create charts, plots, and graphs to understand the patterns in data. They integrate well with NumPy and Pandas. 
4. **scikit-learn** is a library for classical machine learning.  It provides tools for classification, regression, clustering, and model evaluation. It is designed with a simple and consistent interface.


## Execution Speed VS Implementation Speed
Execution speed is the time time it takes a program to complete its work while implementation speed is the time it takes to design, write, test and deploy the software. In many business contexts, implementation speed is more important than execution speed. The goal is to get a product or feature into users’ hands quickly.

Python may be slower in terms of execution speed as compared to compiled languages like C, C++, and Rust but it's implementation speed is faster cause of its easy-to-understand syntax, dynamic typing, ecosystem, large community e.t.c.


##  Introspection
Every object in Python has three important characteristics:
1. Value = the data it contains. E.g., "Adeolu", 42, True.
2. Type = the kind of object it is. E.g., str, int, list. 
3. Identity = a unique identifier that distinguishes it from other objects.


## Deep Dive Into Artificial Intelligence
From this lesson I understand that there's a lot of depth to the word **INTELLIGENCE** when we say it or have a mental picture in our head. It actually has a lot of core abilities linked to it, when we say something or someone is intelligent: they/it has to be able to learn from past experiences, use these experiences and knowledge to process new or current situations and even learn again when they encounter something new from the current situation. Know which experience to use for which situation. 

While computers are deterministic in nature, you can make computers learn from experience, treat each situation different based on pattern recognition rather than always writing a program or logic to help it handle these cases. This is called **ARTIFICIAL INTELLIGENCE**.

The core abilities needed for intelligence can be split into:

### LEARNING
Learning simply means improving performance based on experience. You pass through a dusty dirt road where your white sneakers got all dirty, next time you wouldn't want to pass there. This is learning, nobody had to tell you not to pass there next time, you don't have to be told. This experience even changes your future behaviour.

In the same way, intelligent systems can learn from examples. Imagine you mark some emails as spam, over time your email app start to know which words, senders and/or patterns are likely to be spam. You don't need to write a rule for each possible spam, the app learns on its own from the millions of examples that come from you and millions of other users.

Learning is powerful because the world changes. Fraudsters change methods, traffic patterns change, music taste changes. A system that learns doesn't need to have its code rewritten, it just learns the new pattern.

**AI learns from DATA**.

### REASONING
Reasoning is the ability  to draw conclusion from available information. I made a scenario earlier on with white sneakers, and dirt road. You already have the experience that the dirt road dirties white sneakers. When next you are on your white sneakers, you would need to decide that you need to take another more suitable route to avoid getting your sneakers dirty. That's reasoning.

A machine that can reason does something similar. It takes facts or data, it takes logical steps and arrive at a conclusion. Reasoning may be simple or complex. It may involve rules, probabilities, or chains of logic. But the core idea is that it goes beyond the raw facts to form a new judgement.

### PATTERN RECOGNITION
Pattern recognition is the ability to notice regularities in data. Still using the similar context as above, you may not use that road again but you may come across another road that's a dirt road. You will notice the similarity or regularity between this new road and the former one, similarities like; brown sand, dust filling the air, lack of asphalt or tarmac e.t.c. You can then decide to avoid this road as well so as not to get your sneakers dirty. This is pattern recognition in real life.

In computing, pattern recognition is everywhere. A face unlock feature recognizes the pattern of your face. A voice assistant recognizes the pattern of your speech. A fraud detection system recognizes the pattern of your typical spending.

Pattern recognition is essential because the world is not random. There are regularities, repetitions, and relationships. Intelligent systems use these regularities to make predictions and decisions

### DECISION-MAKING
Decision-making is the ability to choose an action among alternatives. Using the same context, while you now know better to avoid any dusty dirt road, and to take another road. You will always have different roads to likely use, you cannot use more than one. You will most likely use the one that gets you to your destination the fastest or most conveniently or both. This is decision-making at play. An AI system can make similar decisions by weighing different factors.

For example, a recommendation system must decide which video to show next from thousands or millions of options. A credit card fraud system must decide whether to approve, decline, or flag a transaction. A chatbot must decide whether to answer a question, ask for clarification, or transfer to a human.

Decision-making often involves trade-offs. A system cannot show every possible video. It must choose the one most likely to be relevant. It cannot flag every transaction as fraud, or customers will be frustrated. It must balance risk and convenience. Intelligent systems make these choices by evaluating evidence and following learned strategies.


## Strengths of Deterministic Systems
1. Consistency = the system applies the same rules the same way every time.
2. Predictability = given the inputs and rules, the output can be predicted and tested.
3. Transparency = the rules can be documented and inspected. Anyone can review the logic.
4. Auditability = the history of the state changes can be traced and verified.
5. Reliability = because the behaviour is stable, the system can be trusted for critical tasks.
6. Ease of maintenance: When the rules are clear, fixing bugs or updating rules is often straightforward. You find the relevant rule and change it.
7. Efficiency: For well-defined tasks, deterministic systems can be very fast and inexpensive to run.


## Structured vs Unstructured Data
Structured data is organized into a strict, predictable format. Unstructured data is not.


## The Machine Learning (ML) Equation
Earlier said, ML is letting a computer learn from the pattern in data. There something called **features**(inputs) and **labels**(outputs). Where:
* Feature is the data you are using to train the model. The information the computer uses to make prediction
* Label is the expected outcome or known output.

Even though intelligent systems can learn from the pattern in data, human intervention is still much present in **Machine Learning**. Machine learning does not mean the human disappears. The human shifts to new tasks. The role of humans in the ML paradigm include:
* **Collecting data** from real systems.
* **Cleaning data** to remove errors.
* **Labeling data** with correct outputs.
* **Choosing features** that are relevant.
* **Selecting a learning algorithm** that is appropriate for the task.
* **Evaluating the model** to ensure it performs well.
* **Deploying and monitoring** the model over time.

### How training produces the model
During training, a learning algorithm is fed the dataset with features and labels. The algorithm adjusts its internal parameters to reduce the difference between its predictions and the true labels.

The model is not a program in the usual sense. You cannot open a model and read clear rules like you would in a traditional programming. Instead, the model contains numeric weights, thresholds, or learned structures. It behaves like a black box in many cases. You can see the inputs and outputs, but the internal reasoning may be difficult to interpret.

### Inputs → Model → Outputs
There are two phases, training and inference phases. The training phase is when you actually train the model, the inference phase is when the model is being used to make predictions. In simple words, **training** is when the model is built while **inference** is when the model is used.

The model does not store the training data, it only stores the learned parameters or patterns. 

**Training Phase**
Inputs (features + labels)
        ↓
Learning Algorithm
        ↓
Trained Model (Output)

**Training Phase**
New Inputs (features only)
        ↓
Trained Model
        ↓
Prediction (Output)

A very good thing I learned again was that there are different types of learning:
1. Supervised Learning = you train the ML model using labelled data. For example, if you want to train a model to recognise a diseased plant under supervised learning, you give it multiple examples labelling diseased plants as diseased and healthy plants as healthy. 
2. Unsupervised Learning = you give the model unlabelled grouped data, it starts to pick patterns by itself and recognise the similarities between the grouped data.
3. Reinforcement Learning = you put the model in an environment where it learns to make decisions from trial and error. You also introduce a *"carrot and stick"* approach where you give rewards when it makes the right decision and punishments when it makes the wrong one.


## Lifecycle
Training(building) - Inference(using) lifecycle. 

### Training
This is the process of creating the model

**During training, you need:**
1. A dataset with features and labels (supervised learning)
2. A learning algorithm
3. Computing power, such as a laptop, server or cloud processor.

Training can take seconds, minutes, hours or days depending on the size of the data or the complexity of the model.

During training, you also need to evaluate your model. You will need to set aside some labeled data that the model did not train on.You test the model on that held-out data you to see how well it performs. This is called **validation** or **evaluation**. It gives you an evaluation of how well your data will do on new, unseen data.


### Inference
Inference is the process of using the trained model to make predictions.

During inference, you provide new inputs that the model has never seen before and it makes a prediction.