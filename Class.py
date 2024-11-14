# -*- coding: utf-8 -*-
import time
class Event:
    def __init__(self,name, year, month, day):
        self.name = str(name)
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
      
    def info(self):
        return f"Event {self.name} happened {self.day}/{self.month:02d}/{self.year:02d}"
    
    def get_year(self):
        return self.year
    
    def get_month(self):
        return self.month
    
    def get_day(self):
        return self.day