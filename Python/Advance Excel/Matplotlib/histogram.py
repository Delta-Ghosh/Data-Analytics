import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=100, color='blue', alpha=0.7, edgecolor='black')
plt.title("Histogram")
plt.show()
