```python
import math
import pylint
import os
!pip install snakecase

for filename in os.listdir():
    os.rename(filename, snakecase(filename))

class Calculator:
    
    def _init_(Self, name):
        self.name = name
        
    def print_name(self):
        print(self.name)

    def Calculator():
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
```

    Requirement already satisfied: snakecase in c:\users\bonum\anaconda3\lib\site-packages (1.0.1)
    


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp\ipykernel_6688\2767239178.py in <module>
          5 
          6 for filename in os.listdir():
    ----> 7     os.rename(filename, snakecase(filename))
          8 
          9 class Calculator:
    

    NameError: name 'snakecase' is not defined



```python

```


```python

```
