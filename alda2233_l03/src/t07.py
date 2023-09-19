"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed Aldakhil
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-09-19"
-------------------------------------------------------
"""
# Imports

# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


Breakfast = float(input("Enter cost of breakfast:"))
Lunch = float(input("Enter cost of lunch: "))
Supper = float(input("Enter cost of supper: "))
Total = Breakfast + Lunch + Supper
print("Meal        Cost")
print(f"Breakfast {Breakfast:>5}")
print(f"Lunch {Lunch:>9}")
print(f"Supper{Supper:>9}")
print(f"Total       {Total:.2f}")
