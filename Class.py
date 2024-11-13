# -*- coding: utf-8 -*-

class Good:
    def __init__(self, name, hryvni, kop):
            self.name = name
            self.hryvni = hryvni
            self.kop = kop
            
    def print_out(self):
        return f"{self.name} costs {int(self.hryvni)}.{int(self.kop)}"
    
    def get_price(self):
        return self.hryvni + self.kop/100
    
    def get_name(self):
        return self.name