# -*- coding: utf-8 -*-
class Car:
    def __init__(self, model, price, speed):
        self.model = model
        self.price = price
        self.speed = speed
        
    def info(self):
        return f"{self.model} with max speed {self.speed}km/h costs {self.price}$  "
    
    def get_model(self):
        return self.model
    
    def get_price(self):
        return int(self.price)
    
    def get_speed(self):
        return int(self.speed)