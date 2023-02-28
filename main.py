from datetime import date
import datetime

class Person:
    description: str = "A simple normal human being"

    def __init__(self, name: str, surname: str, ):
        self.name: str = name
        self.surname: str = surname



    def greet(self):
        return f"Hello my name is {self.name}"
    
    

    def walk_away(self):
        return f"{self.name} is walking away..."
    

    
    def calculate_days_left_till_black_friday(self):
        today = date.today()
        black_friday = datetime.date(2023, 11, 24)
        delta = black_friday - today
        return delta.days
    
    
    def get_eye_color(self, eye_color: str = "Brown") -> str:
        return eye_color

person = Person("Labas", "Rytas")
person2 = Person("Antanas", "Kurmiarausis")

print(person.calculate_days_left_till_black_friday())
print(person.get_eye_color("Blue"))

# print(person.name)
# print(person2.name)
# print(person.greet())
# print(person2.walk_away())
# print(person.description)


