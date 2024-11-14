# -*- coding: utf-8 -*-
from Class import *

file = "info.txt"

def read_file(filename):
    obj_list = []
    with open(filename, 'r') as f:
        for line in f:
            line  = line.strip()
            data = line.split()
            if len(data) == 4:
                temp_obj = Event(str(data[0]), int(data[1]), int(data[2]),int( data[3]))
                obj_list.append(temp_obj)
            
    return obj_list

def sorting(arr):
    sorted_arr = sorted(arr, key=lambda x: (x.get_year(), x.get_month(), x.get_day()))

    return sorted_arr

def by_year(arr, year):
    new_list = []
    for i in arr:
        arr_year = i.get_year()
        if arr_year == year:
            new_list.append(i)
            
    return new_list

obj_list = read_file(file)

for i in obj_list:
    print(i.info())
    
print("Sorted list: ")
new_list = sorting(obj_list)
for i in new_list:
    print(i.info())
    

try:    
    year = int(input("enter the year:"))
except ValueError as e:
    print(e)
new_list1 = by_year(new_list, year)
if new_list1 != []: 
    for i in new_list1:
        print(i.info())
else: 
    print("Nothing happend in %i" % year)
