# -*- coding: utf-8 -*-
from Employee import *

file_name  = 'input.txt'

def read_file(filename):
    list_obj = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                data = line.split()
                position = ' '.join(data[:-2])
                obj1 = Employee(data[0], data[1],str( data[2]), str(data[3]), position, str(data[-1]))
                list_obj.append(obj1)
        return list_obj
    except ValueError as e:
        print(e)
    except FileNotFoundError:
        print("File Not Found Error!")
        
        
        
def average_salary(obj_list):
    av_salary = 0
    n=0
    for i in obj_list:
        salary = int(i.get_salary())
        av_salary+=salary
        n+=1
        
    av_salary /=n
    return av_salary
    

        
obj_list = read_file(file_name)

for i in obj_list:
    print(i.info())
    
#sorting by age
sorted_list = sorted(obj_list, key = lambda x: x.get_age())

print('\n sorted: \n')

for i in sorted_list:
    print(i.info())
    
# finding average salary in company 
print("\n The average salary: ", average_salary(obj_list))