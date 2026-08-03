import matplotlib.pyplot as plt
import numpy as np

stock = [20, 40, 25,25 ]
labels = ["M", "L", "XL", "XXL"]
plt.pie(stock, labels=labels, autopct='%d%%')
plt.title("Pie Chart")
plt.show()