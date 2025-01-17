#!/usr/bin/python3
"""importing libraries"""
import numpy as np
import matplotlib.pyplot as plt

"""creates an array of evenly spaced integers excluding 11 then cubes"""
y = np.arange(0, 11)**3 
x = np.arange(0, 11)

fig, ax = plt.subplots()
ax.plot(x, y, color='red')
plt.show()
