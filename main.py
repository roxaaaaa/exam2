# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

file1 = pd.read_csv('file1.csv')
file2 = pd.read_csv('file2.csv')

merged_data = pd.merge(file1, file2, on='car_id', how='left')
merged_data.to_csv("merged.csv", index=False)


brands  = merged_data['make'].value_counts()
print(brands)
plt.bar(brands.index, brands)  # Use brands.index as the x-axis (unique makes)
plt.xlabel('Car Make')
plt.ylabel('Count')
plt.title('Count of Car Makes')
plt.show()

#finding the cheapest car
print('\n the cheapest car: \n')
print(merged_data.loc[merged_data['price'].idxmin()])


print('\n the most expensive car: \n')
print(merged_data.loc[merged_data['price'].idxmax()])


