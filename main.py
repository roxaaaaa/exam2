# -*- coding: utf-8 -*-
import numpy as np
import random
while True:
        try:
            n = int(input("Enter n: "))
            break
        except ValueError:
            print("Please enter a integer")

def creating_matrix(n):
    
    arr = np.zeros((n,n), dtype = int) 
    for i in range(n):
        for j in range(n):
            arr[i,j] = random.randint(-10, 10)
    return arr

def find(arr, n):
    min_el=[]
    
    for i in range(n):
        if arr[i,i] <0:
            min_el.append(np.min(arr[i]))
 
    return np.max(min_el)
arr = creating_matrix(n)

for row in arr:
        print(' '.join(str(i) for i in row))

print("result:" , find(arr,n))