# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv') 


smoker_tips = data.groupby('smoker')['tip'].mean()

plt.figure(figsize=(8, 5))
plt.bar(smoker_tips.index, smoker_tips.values, color=['blue', 'orange'])
plt.title('Average Tips: Smokers vs Non-Smokers')
plt.xlabel('Smoker')
plt.ylabel('Average Tip')
plt.show()

day_tips = data.groupby('day')['tip'].mean()

plt.bar(day_tips.index, day_tips.values, color = ['green', 'yellow'])
plt.title('tips by the day of week')
plt.xlabel('day of the week')
plt.ylabel('tip')
plt.show()

time_tips = data.groupby('time')['tip'].mean()

plt.bar(time_tips.index, time_tips.values, color = ['purple', 'yellow'])
plt.title('tips by time')
plt.xlabel('day of the week')
plt.ylabel('tip')
plt.show()


plt.hist(data['bill'])
plt.title('Histogram of Total Bills')
plt.xlabel('Bill')
plt.ylabel('Frequency')
plt.show()

plt.scatter(x = data['bill'], y = data['tip'], color = ['green'])
plt.xlabel('Bill')
plt.ylabel('Tip')
plt.title('Scatter of Bills and Tips')
plt.show()

sex_tips = data.groupby('sex')['tip'].mean()

plt.bar(sex_tips.index, sex_tips.values, color = ['pink', 'blue'])
plt.xlabel('Sex')
plt.ylabel('Tip')
plt.title('male`s tip vs females tip')
plt.show()


