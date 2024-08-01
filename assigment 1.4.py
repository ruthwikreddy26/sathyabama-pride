import math
import sys
import datetime

def list_and_help(obj, name):
    """
    Lists attributes of an object, prints them, and provides help for selected attributes.
    """
    print(f"Attributes and methods of {name}:")
    attributes = dir(obj)
    for attribute in attributes:
        print(attribute)
    
    print("\nDetailed help for selected attributes:\n")
    for attribute in attributes:
        try:
            attr_obj = getattr(obj, attribute)
            if callable(attr_obj):
                print(f"Help for {name}.{attribute}:")
                help(attr_obj)
                print("\n" + "="*80 + "\n")
        except Exception as e:
            print(f"Could not get help for {name}.{attribute}: {e}")

def main():
    # List attributes and provide help for different objects
    list_and_help(math, 'math module')
    list_and_help(sys, 'sys module')
    list_and_help(datetime, 'datetime module')
    
    # Example with a custom object
    class MyClass:
        def __init__(self):
            self.attr1 = 'value1'
        
        def method1(self):
            """This is a method."""
            pass
    
    my_obj = MyClass()
    list_and_help(my_obj, 'MyClass instance')

if __name__ == "__main__":
    main()
