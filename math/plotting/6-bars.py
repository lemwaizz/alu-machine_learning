#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Generate the random data for fruit quantities
np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Fruit categories (rows of the matrix)
fruit_names = ["Apples", "Bananas", "Oranges", "Peaches"]

# Color mapping for each fruit
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']  # Red, Yellow, Orange, Peach

# Plotting the stacked bar chart
fig, ax = plt.subplots()

# Bar width
bar_width = 0.5

# Create the stacked bars
ax.bar(0, fruit[0, 0], color=colors[0], width=bar_width, label=fruit_names[0])  # Apples for Farrah
ax.bar(1, fruit[0, 1], color=colors[0], width=bar_width, label=fruit_names[0])  # Apples for Fred
ax.bar(2, fruit[0, 2], color=colors[0], width=bar_width, label=fruit_names[0])  # Apples for Felicia

ax.bar(0, fruit[1, 0], bottom=fruit[0, 0], color=colors[1], width=bar_width, label=fruit_names[1])  # Bananas for Farrah
ax.bar(1, fruit[1, 1], bottom=fruit[0, 1], color=colors[1], width=bar_width, label=fruit_names[1])  # Bananas for Fred
ax.bar(2, fruit[1, 2], bottom=fruit[0, 2], color=colors[1], width=bar_width, label=fruit_names[1])  # Bananas for Felicia

ax.bar(0, fruit[2, 0], bottom=fruit[0, 0] + fruit[1, 0], color=colors[2], width=bar_width, label=fruit_names[2])  # Oranges for Farrah
ax.bar(1, fruit[2, 1], bottom=fruit[0, 1] + fruit[1, 1], color=colors[2], width=bar_width, label=fruit_names[2])  # Oranges for Fred
ax.bar(2, fruit[2, 2], bottom=fruit[0, 2] + fruit[1, 2], color=colors[2], width=bar_width, label=fruit_names[2])  # Oranges for Felicia

ax.bar(0, fruit[3, 0], bottom=fruit[0, 0] + fruit[1, 0] + fruit[2, 0], color=colors[3], width=bar_width, label=fruit_names[3])  # Peaches for Farrah
ax.bar(1, fruit[3, 1], bottom=fruit[0, 1] + fruit[1, 1] + fruit[2, 1], color=colors[3], width=bar_width, label=fruit_names[3])  # Peaches for Fred
ax.bar(2, fruit[3, 2], bottom=fruit[0, 2] + fruit[1, 2] + fruit[2, 2], color=colors[3], width=bar_width, label=fruit_names[3])  # Peaches for Felicia

# Set the x-axis labels
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['Farrah', 'Fred', 'Felicia'])

# Set the y-axis label and range
ax.set_ylabel("Quantity of Fruit")
ax.set_ylim(0, 80)
ax.set_yticks(np.arange(0, 81, 10))

# Title of the plot
ax.set_title("Number of Fruit per Person")

# Display legend
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
