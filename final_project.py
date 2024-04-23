import matplotlib.pyplot as plt
import numpy as np

# Data
dates = ['18-Mar', '19-Mar', '20-Mar', '21-Mar', '22-Mar', '25-Mar', '26-Mar', '27-Mar', '28-Mar', '29-Mar', '1-Apr', '2-Apr', '3-Apr', '4-Apr', '5-Apr']
tread_M = [2, 9, 7, 14, 9, 3, 8, 13, 15, 7, 5, 9, 12, 3, 11]
tread_N = [13, 8, 13, 9, 11, 10, 5, 12, 13, 11, 15, 11, 12, 14, 11]
tread_AN = [3, 1, 4, 1, 3, 4, 3, 4, 2, 9, 1, 5, 3, 3, 6]

punch_M = [8, 4, 10, 5, 8, 3, 6, 2, 5, 0, 11, 9, 6, 10, 3]
punch_N = [9, 5, 3, 5, 7, 4, 6, 6, 4, 7, 5, 8, 7, 6, 6]
punch_AN = [0, 3, 0, 3, 0, 0, 3, 0, 3, 0, 0, 3, 2, 3, 0]

scatter_data = [sum(x) for x in zip(tread_M, tread_N, tread_AN, punch_M, punch_N, punch_AN)]

# Plotting
plt.figure(figsize=(10, 8))

# Treadmill Usage
plt.subplot(3, 1, 1)
plt.plot(dates, tread_M, marker='o', label='Morning')
plt.plot(dates, tread_N, marker='o', label='Noon')
plt.plot(dates, tread_AN, marker='o', label='Afternoon')
plt.title('Treadmill Usage')
plt.xlabel('Date')
plt.ylabel('Usage')
plt.xticks(rotation=45)
plt.legend()

# Punching Bag Usage
plt.subplot(3, 1, 2)
plt.plot(dates, punch_M, marker='o', label='Morning')
plt.plot(dates, punch_N, marker='o', label='Noon')
plt.plot(dates, punch_AN, marker='o', label='Afternoon')
plt.title('Punching Bag Usage')
plt.xlabel('Date')
plt.ylabel('Usage')
plt.xticks(rotation=45)
plt.legend()

# Scatter plot with Linear Regression
plt.subplot(3, 1, 3)
plt.scatter(dates, scatter_data, color='red', label='Combined Usage')

# Perform linear regression
x_values = np.arange(len(dates))
slope, intercept = np.polyfit(x_values, scatter_data, 1)
regression_line = slope * x_values + intercept

# Plot the regression line
plt.plot(dates, regression_line, color='blue', linestyle='--', label='Linear Regression')

plt.title('Combined Usage with Linear Regression')
plt.xlabel('Date')
plt.ylabel('Usage')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()
