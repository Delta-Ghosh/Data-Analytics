import matplotlib.pyplot as plt
import numpy as np

catagories = ["A"," B", "C", "D", "E"]
values = [2, 4, 6, 8, 10]

plt.bar(catagories, values, color = "red", width = 0.5)
plt.show()