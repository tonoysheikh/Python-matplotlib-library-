import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,3,5,7,9])
y = np.array([34,36,32,35,39])

plt.plot(x, y , marker = 'o')

plt.title("Dhaka Temperature")
plt.xlabel("Date")
plt.ylabel("Temperatue")

plt.grid()

plt.show()