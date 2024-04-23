'''
Farzan Feeha
ISTA 131 Final Project
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
My assigned data graphs:
Yoga usage in morning, noon, and afternoon
Weights usage in morning, noon, and afternoon
Total people in pool, total people on weight machines, total people on punching bags in a day.

'''

# Data Collected
dates = ['18-Mar', '19-Mar', '20-Mar', '21-Mar', '22-Mar', '25-Mar', '26-Mar', '27-Mar', '28-Mar', '29-Mar', '1-Apr', '2-Apr', '3-Apr', '4-Apr', '5-Apr']
yogamorning = [16, 11, 18, 16, 12, 21, 19, 25, 13, 21, 20, 12, 19, 10, 16]
yoganoon = [4, 10, 9, 8, 5, 11, 12, 15, 10, 7, 12, 10, 12, 8, 9]
yogaafternoon = [0, 0, 0, 2, 0, 3, 0, 2, 3, 3, 0, 0, 2, 3, 2]

weightsmorning = [13, 11, 14, 12, 9, 15, 7, 9, 13, 12, 6, 9, 7, 12, 14]
weightsnoon = [12, 10, 9, 9, 7, 13, 12, 11, 12, 9, 9, 13, 13, 13, 12]
weightsafternoon = [8, 6, 8, 5, 5, 7, 6, 6, 6, 9, 9, 4, 5, 7, 7]

totalpool = [77, 51, 63, 61, 62, 66, 79, 74, 53, 52, 59, 52, 54, 78, 63]
totalweights = [33, 27, 31, 26, 21, 35, 25, 26, 31, 30, 28, 26, 25, 31]
totalpunch = [17, 12, 13, 13, 15, 7, 15, 8, 12, 7, 16, 20, 14, 19, 9]

yoga_day_times = ['Morning', 'Noon', 'Afternoon']

# Plotting the Graphs
plt.figure(figsize=(10, 6))


# Yoga Room Usage
plt.plot(dates, yogamorning, label='Morning', color='blue', marker='o')
plt.plot(dates, yoganoon, label='Noon', color='green', marker='o')
plt.plot(dates, yogaafternoon, label= 'Afternoon', color='purple', marker='o')
plt.title('Yoga Room Usage')
plt.xlabel('Date')
plt.ylabel('Number of People')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Weights Usage
plt.plot(dates, weightsmorning, label='Morning', color='blue', marker='o')
plt.plot(dates, weightsnoon, label='Noon', color='green', marker='o')
plt.plot(dates, weightsafternoon, label= 'Afternoon', color='purple', marker='o')
plt.title('Weights Usage')
plt.xlabel('Date')
plt.ylabel('Number of People')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Total # of People in a Day wit Line of Regression
plt.figure(figsize=(10, 6))
plt.scatter(dates, totalpool, s=100, color='red')
plt.title('Total # of People in the Day')
x_values = np.arange(len(dates))
slope, intercept = np.polyfit(x_values, totalpool, 1)
regression_line = slope * x_values + intercept

plt.plot(x_values, regression_line, color='green', linestyle='--', label='Linear Regression')
plt.title('Combined Usage with Linear Regression')
plt.xlabel('Dates')
plt.ylabel('# of People')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

