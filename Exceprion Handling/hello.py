from tkinter import Y


print("give the value a and b")
a=input("Enter value of a ==")
b=input("Enter value of b ==")

try:
    x=a
    y=b
    print(x/y)
except TypeError:
    print("Unsported Op")
except ZeroDivisionError:
    print("divison by zero is not all owed")