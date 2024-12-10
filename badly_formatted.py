"""
Module
"""


class Person:
    """
    docstring
    """

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.skills = []

    def add_skill(self, skill):
        """
        docstring
        """
        self.skills.append(skill)

    def __str__(self):
        return (
            f"Name: {self.name}, Age: {self.age}, City: {self.city},"
            f"Skills: {', '.join(self.skills) if self.skills else 'None'}"
        )


person = Person("Alice", 25, "New York")
person.add_skill("Python")
print(person)
