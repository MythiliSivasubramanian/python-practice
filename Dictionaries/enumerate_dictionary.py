""" enumerate() with Dictionary Comprehension
1. Index - Value mapping
2. Value - Index (reverse mapping)
"""

# Predefined List of colors
colors = ["red", "blue", "green"]

# Index-  key (start as 1)
index_to_color = {index: color for index, color in enumerate(colors, start=1)}
print("Index to Color:",index_to_color)

# Color as key (reverse mapping)
color_to_index = {color: index for index, color in enumerate(colors)}
print("\nColor to Index:",color_to_index)
