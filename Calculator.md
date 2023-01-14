```python
#D. Tutoring - Month 1 

## Project to complete for the Month 1

### Introduction

"""
In this project, you will be building a basic calculator using Python. 
The calculator will be able to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. 
By working on this project, you will learn how to:

* Use Python's built-in arithmetic operators
* Use input() and print() to interact with the user
* Use if-elif-else statements to control the flow of the program
"""
"""
Problem Set

1. Create a Python function called "calculator" that keeps running until the user chooses to exit.

2. Use input() to ask the user for the operation they want to perform (e.g. addition, subtraction, etc.). 
Store the user's input in a variable called "operator".

3. Use another input() call to ask the user for the two numbers they want to perform the operation on. 
Store these values in variables called "num1" and "num2".

4. Use an if-elif-else block to determine which operation the user wants to perform based on the value of "operator". 
Inside the block, use Python's built-in arithmetic operators to perform the corresponding calculation and store the result 
in a variable called "result".

5. Use the print() function to display the "result" to the user.

6. Add support for more advanced mathematical operations such as exponentiation, square root, 
and logarithms using a library such as math, numpy, or scipy.

7. Implement error handling for invalid input such as non-numeric input for numbers, or invalid operation selections. 
Allow the user to retry input in case of invalid input

8. Create a GUI for the calculator using a library such as Tkinter or PyQt to make the calculator more user-friendly.

9. Add the ability to perform calculations with variables. 
Allow the user to store and recall the result of previous calculations

10. Create and utilize a class that represent the calculator. 
Add a subclass that represent each operation and add the corresponding method to it

11. Implement the ability to chain multiple operations together, and evaluate the final result.

12. Allow the user to choose the number of decimal places to display in the result.

13. Your code must follow PEP 20 – The Zen of Python
"""
"""
### Python pre-requisite knowledge

Before attempting this project, it is important to have a basic understanding of the following concepts in Python:

* Variables: You should understand how to create and assign values to variables, as well as the different types of data that can be stored in variables (e.g. integers, floats, strings).

* Input and Output: You should know how to use the input() and print() functions to interact with the user and display information on the screen.

* Control Flow: You should have a basic understanding of control flow statements such as if-elif-else statements, and how they are used to control the flow of the program based on certain conditions.

* Loops: You should know how to use while loops in Python, and how they can be used to execute a block of code repeatedly until a certain condition is met.

* Basic arithmetic operations: You should know how to use the basic arithmetic operators (i.e +, - , *, /) in python, and understand their basic meaning

* Basic understanding of function: You should know how to define and call a function, and understand the purpose of a function in terms of breaking code down to smaller and reusable pieces.

* Familiarity with advanced mathematical operations, and how to perform them in Python using libraries such as numpy, scipy.

* Experience with creating graphical user interface using library such as Tkinter, PyQt

* Understanding of error handling in Python, and how to use try-except blocks to handle exceptions.

* Experience with classes, subclass, encapsulation, inheritance in OOP.

* Experience with operator overloading and use of magic methods

* Knowledge on how to chain operations using the chaining technique

* Knowledge of string formatting and the usage of "%.xf" where x is a number to set the number of decimal places.

* Knowledge of PEP 20 – The Zen of Python
"""

import this
import re
import random
import itertools
import csv
import tkinter as tk
import math

class Calculator:
    def __init__(self):
        self.result_value = 0
        self.operations = []
        self.operands = []

    def add(self, num1, num2):
        self.operations.append("add")
        self.operands.append((num1, num2))
        self.result_value = num1 + num2
        return self.result_value

    def subtract(self, num1, num2):
        self.operations.append("subtract")
        self.operands.append((num1, num2))
        self.result_value = num1 - num2
        return self.result_value

    def multiply(self, num1, num2):
        self.operations.append("multiply")
        self.operands.append((num1, num2))
        self.result_value = num1 * num2
        return self.result_value

    def divide(self, num1, num2):
        self.operations.append("divide")
        self.operands.append((num1, num2))
        self.result_value = num1 / num2
        return self.result_value

    def square_root(self, num1):
        self.operations.append("square_root")
        self.operands.append((num1,))
        self.result_value = math.sqrt(num1)
        return self.result_value
    
    def exponential(self, num1):
        self.operations.append("exponential")
        self.operands.append((num1,))
        self.result_value = math.exp(num1)
        return self.result_value
    
    def logarithm(self, num1):
        self.operations.append("logarithm")
        self.operands.append((num1,))
        self.result_value = math.log(num1)
        return self.result_value

    def recall(self):
        return self.result_value

    def evaluate(self):
        for i in range(len(self.operations)):
            if self.operations[i] == "add":
                self.result_value = self.add(self.result_value, self.operands[i][1])
            elif self.operations[i] == "subtract":
                self.result_value = self.subtract(self.result_value, self.operands[i][1])
            elif self.operations[i] == "multiply":
                self.result_value = self.subtract(self.result_value, self.operands[i][1])
            elif self.operations[i] == "divide":
                self.result_value = self.substract(self.result_value, self.operands[i][1])
            elif self.operations[i] == "square_root":
                self.result_value = self.substract(self.result_value, self.operands[i][1])
            elif self.operations[i] == "exponential":
                self.result_value = self.substract(self.result_value, self.operands[i][1])
            elif self.result_value[i] == "logarithm":
                self.result_value = self.substract(self.result_value, self.operands[i][1])
            
        # Create main window
        root = tk.Tk()
        root.title("Simple Calculator")

        # Create Entry widgets to get numbers
        num1 = tk.Entry(root)
        num1.grid(row=0, column=1)
        num2 = tk.Entry(root)
        num2.grid(row=1, column=1)

        # Create labels for Entry widgets
        tk.Label(root, text="Number 1").grid(row=0, column=0)
        tk.Label(root, text="Number 2").grid(row=1, column=0)

        # Create buttons for operations
        tk.Button(root, text="+", command=add).grid(row=2, column=0)
        tk.Button(root, text="-", command=subtract).grid(row=2, column=1)
        tk.Button(root, text="*", command=multiply).grid(row=2, column=2)
        tk.Button(root, text="/", command=divide).grid(row=2, column=3)
        tk.Button(root, text="sqrt", command=math.sqrt()).grid(row=2, column=4)
        tk.Button(root, text="exp", command=math.exp()).grid(row=2, column=5)
        tk.Button(root, text="log", command=math.log()).grid(row=2, column=6)

        # Create label to display result
        result = tk.Label(root, text="Result: ")
        result.grid(row=3, column=0, columnspan=7)

        root.mainloop()

```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    


```python
6*3
```




    18




```python

```
