# -*- coding: utf-8 -*-
from Class import Car 
filename = "input.txt"

def read_file(filename):
    obj_list = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                data = line.split()
                model = ' '.join(data[:-2])
                obj = Car(model, int(data[-2]), data[-1])
                obj_list.append(obj)
    except ValueError as e:
        print(e)
    except FileNotFoundError:
        print("File isn`t found")
    return obj_list   
            
def most_speed(arr):
    new_list = []
    for i in arr:
        if i.get_speed() > 180:
            new_list.append(i)

    return new_list

def the_cheapest(arr):
    model = arr[0]
    price = arr[0].get_price()
    
    for i in range(1,len(arr)):
        if arr[i].get_price() < price:
            model = arr[i]
            price = arr[i].get_price()
            
    return model.get_model()

obj_list = read_file(filename)

for i in obj_list:
    print(i.info())
    
speed_list = most_speed(obj_list)

if speed_list == []:
    print('\nThere is no car with speed over 180km/h')
else:
    print("\nthe list of cars with over 180km/h max speed:")
    for i in speed_list:
        print(i.info())
        
print("\nThe chepest car out of the last list is ", the_cheapest(speed_list) )