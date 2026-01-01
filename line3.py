import numpy as np
import matplotlib.pyplot as plt
x_1 = np.linspace(-10,10,100)
x_2l1 = (-1-x_1)/(-2)
x_2l2 = (1+x_1)/2
plt.plot(x_1,x_2l1)
plt.plot(x_1,x_2l2)
plt.show()
