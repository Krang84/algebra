import numpy as np
import matplotlib.pyplot as plt
x1 = np.linspace(-10,10,100)
x2l1 = (1+x1) / 2
x2l2 = (3+x1)/ 2
plt.plot(x1,x2l1)
plt.plot(x1,x2l2)
plt.show()
