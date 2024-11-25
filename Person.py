# -*- coding: utf-8 -*-
class Person:
    def __init__(self, name, surname, age):
        self.name = name 
        self.surname = surname
        self.age = age
        
    def info(self):
        return f'{self.name} {self.surname} {self.age} years old.'
    
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_surname(self):
        return self.surname

