import math
import sys
import datetime

def list_attributes(obj, name):
    """
    Lists attributes of an object and prints them.
    """
    print(f"Attributes and methods of {name}:")
    attributes = dir(obj)
    for attribute in attributes:
        print(attribute)
    print("\n")

def main():
    # List attributes of different objects
    list_attributes(math, 'math module')
    list_attributes(sys, 'sys module')
    list_attributes(datetime, 'datetime module')
    
    # Example with a custom object
    class MyClass:
        def __init__(self):
            self.attr1 = 'value1'
        
        def method1(self):
            pass
    
    my_obj = MyClass()
    list_attributes(my_obj, 'MyClass instance')

if __name__ == "__main__":
    main()
