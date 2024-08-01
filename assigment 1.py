Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class PersonObjectCamel:
...     def __init__(self, firstName, lastName, age):
...         self.firstName = firstName
...         self.lastName = lastName
...         self.age = age
... 
...     def getFullName(self):
...         return f"{self.firstName} {self.lastName}"
...     
...     def getAge(self):
...         return self.age
... 
