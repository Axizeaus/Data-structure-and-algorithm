from unicodedata import name


class Employee(object):
    num_of_employee = 0
    
    def __init__(self, name, rate) -> None:
        self.owed = 0
        self.name = name
        self.rate = rate
        Employee.num_of_employee += 1
        
    def __del__(self):
        Employee.num_of_employee -= 1
        
    def hours(self,num_hours):
        self.owed += num_hours * self.rate
        return (f"{num_hours} hours worked")
        
    def pay(self):
        self.owed = 0
        return (f"payed {self.name}")
        
    
emp1 = Employee('Jill', 18.5)
emp2 = Employee('Jack', 15.5)
emp3 = Employee('John', 30)

print(Employee.num_of_employee)
print(emp1.hours(20))
print(emp1.owed)
print(emp2.hours(10))
print(emp1.pay())
print(emp2.pay())