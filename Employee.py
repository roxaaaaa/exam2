# -*- coding: utf-8 -*-
from Person import *

class Employee(Person):
    def __init__(self, name, surname, age, years, position, salary):
        super().__init__(name, surname, age)
        self.years = years
        self.position = position
        self.salary = salary
        

    def get_work_experience(self):
        return self.years
    
    def get_position(self):
        return self.position
    
    def get_salary(self):
        return self.salary
   
    def info(self):
        return f'{self.name} {self.surname} {self.age} years old has been working as a {self.position} for the last {self.years} years. Salary: {self.salary}$ '
    