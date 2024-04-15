import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(100,10,120)

#plt.plot(x)
plt.hist(x)
plt.show()

print(x)