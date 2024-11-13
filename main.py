# -*- coding: utf-8 -*-

from Class import *

filename = "info.txt"

def read_file(filename):
    obj_list = []
    with open(filename, 'r') as f:
        for line in f: 
            line = line.strip()  # Remove leading/trailing whitespace
            parts = line.split()  # Split the line into parts
            
            # Assuming format: name, hryvni, kop (e.g., 'pen 4 50')
            if len(parts) == 3:
                name = parts[0]
                hryvni = float(parts[1])
                kop = float(parts[2])
                good1 = Good(name, hryvni, kop)
                obj_list.append(good1)
    
    return obj_list

def most_expensive(arr):
    most_exp = arr[0]
    exp_price = arr[0].get_price()
    for i in range(1, len(arr)):
        if arr[i].get_price() > exp_price:
            most_exp = arr[i]
            exp_price = arr[i].get_price()
    
    return most_exp

def sort_alphabetical(arr):
    arr.sort(key = lambda x: x.get_name())
    return arr



goods_list = read_file(filename)

for i in goods_list:
    print(i.print_out())
    
most_expensive = most_expensive(goods_list)
print(" The most expensive good: " ,most_expensive.print_out())

sort_alphabetical(goods_list)
for i in goods_list:
    print(i.print_out())
