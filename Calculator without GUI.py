#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import os
from snakecase import snakecase

for filename in os.listdir():
    os.rename(filename, snakecase(filename))

class Calculator:

    def calculator():
        while True: 
            # Defining variables
            result = 0

            # Input by user
            entry = input("Enter operand ( +, -, *, /, sqrt, exp, log ): ")

            # if the "end" is entered, stop the loop
            if entry == 'End':
                break

            # ask number from user
            num1 = float(input("Enter number 1: "))
            num1 = float(input("Enter number 2: "))

            # calculate the result
            if entry == '+':
                result = num1 + num2
            elif entry == '-':
                result = num1 - num2
            elif entry == '*':
                result = num1 * num2
            elif entry == '/':
                result = num1 / num2
            elif entry == 'sqrt':
                result = math.sqrt(num1,)
            elif entry == 'exp':
                result = math.exp(num1,)
            elif entry == 'log':
                result = math.exp(num1,)

            # results displays
            print("Current result: ")


# In[ ]:




