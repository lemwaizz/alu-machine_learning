#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Datasets
y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create a figure and a 3x2 grid
fig = plt.figure(figsize=(10, 8))
fig.suptitle("All in One", fontsize=16)

# Plot 1: Cubic function
ax1 = fig.add_subplot(3, 2, 1)
ax1.plot(np.arange(0, 11), y0, marker='o')
ax1.set_title("Cubic Function", fontsize='x-small')
ax1.set_xlabel("x", fontsize='x-small')
ax1.set_ylabel("y = x^3", fontsize='x-small')

# Plot 2: Scatter plot of multivariate normal distribution
ax2 = fig.add_subplot(3, 2, 2)
ax2.scatter(x1, y1, alpha=0.5, color='purple')
ax2.set_title("Multivariate Normal Distribution", fontsize='x-small')
ax2.set_xlabel("x1", fontsize='x-small')
ax2.set_ylabel("y1", fontsize='x-small')

# Plot 3: Exponential decay of Carbon-14
ax3 = fig.add_subplot(3, 2, 3)
ax3.plot(x2, y2, color='blue')
ax3.set_title("Exponential Decay of C-14", fontsize='x-small')
ax3.set_xlabel("Time (years)", fontsize='x-small')
ax3.set_ylabel("Fraction Remaining", fontsize='x-small')

# Plot 4: Exponential decay comparison
ax4 = fig.add_subplot(3, 2, 4)
ax4.plot(x3, y31, label="Half-life: 5730 years", color='red')
ax4.plot(x3, y32, label="Half-life: 1600 years", color='green')
ax4.set_title("Exponential Decay Comparison", fontsize='x-small')
ax4.set_xlabel("Time (years)", fontsize='x-small')
ax4.set_ylabel("Fraction Remaining", fontsize='x-small')
ax4.legend(fontsize='x-small')

# Plot 5: Histogram of student grades spanning two columns
ax5 = fig.add_subplot(3, 1, 3)
ax5.hist(student_grades, bins=10, color='skyblue', edgecolor='black')
ax5.set_title("Student Grades Distribution", fontsize='x-small')
ax5.set_xlabel("Grades", fontsize='x-small')
ax5.set_ylabel("Frequency", fontsize='x-small')

# Adjust layout for better spacing
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
