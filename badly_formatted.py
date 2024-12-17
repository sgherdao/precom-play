import requests; import json;
class Person:
    def __init__(self, name, age, city): self.name=name; self.age=age; self.city=city
    def add_skill(self, skill):
        if not hasattr(self,'skills'):
            self.skills=[] ;     self.skills.append(skill)
    def __str__(self): return f"Name: {self.name}, Age: {self.age}, City: {self.city}, Skills: {', '.join(self.skills) if hasattr(self, 'skills') else 'None'}"
person=Person("Alice",25,"New York")
person.add_skill("Python"       )
print(person)      
