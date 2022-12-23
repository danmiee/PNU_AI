import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9], 'c*--', markersize=10, linewidth=2)
plt.plot([2, 3, 4], [5, 6, 7], 'r+')
plt.xlabel('Sequence')
plt.ylabel('Time(sec)')
plt.title('Experimental Result')
plt.legend(['Mouse', 'Cat'])
plt.grid()
plt.show()


def gaussian(x):
    return np.exp(-(0.5-x)**2/1.5)

# gaussian = lambda x: np.exp(-(0.5 - x)**2/1.5)


x = np.arange(-2, 2.5, 0.01)
y = gaussian(x)

plt.plot(x, y)
plt.xlabel('x values')
plt.ylabel('exp(-(0.5-x)**2/1.5')
plt.title('Gaussian Function')
plt.show()
