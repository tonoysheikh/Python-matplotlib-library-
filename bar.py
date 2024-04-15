import matplotlib.pyplot as plt
import numpy as np

x = np.array([3,9,5,1,7])
y = np.array([34,36,32,35,39])

plt.bar(x,y)

plt.title("Dhaka Temperature")
plt.xlabel("Date")
plt.ylabel("Temperatue")

plt.show()