class Employee:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def name_and_suurname(self):
        return self.name + " " + self.surname
    
    def full_email(self):
        return self.name.lower() + "." + self.surname.lower() + "@company.com"
        
    
employee = Employee("Tadas","Kebabas")
print(employee.name_and_suurname())
print(employee.full_email())

