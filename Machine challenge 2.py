import numpy as np
import matplotlib.pyplot as plt
nums = np.array([0.5, 0.7, 1.1, 1.2, 1.3, 2.1])
plt.hist(nums, bins=[0, 1, 2, 3])
plt.title("Histogram of nums against bins")
plt.ylabel("Bins")
plt.xlabel("Numbers")
plt.show()
