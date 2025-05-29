from abc import ABC, abstractmethod 
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
    

class Manager(Employee):
    def __init__(self, name, base_salary):
        self.name = name 
        self.base_salary = base_salary
        
    
    def calculate_salary(self, name, base_salary):
        return self.base_salary + 1.2
        
class Developer(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name 
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        
        
    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate
        
        
class Company:
    def __init__(self, employees):
        self.employees = employees
        
        
    def add_employee(self, employee):
        self.employee.append(employee)
        
        
    def calculate_total_salary(self):
        total_salary = 0 
        for employee in employees:
            total_salary +=employee.base_salary
        return total_salary
        
        
    
