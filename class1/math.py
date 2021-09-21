import numpy as np
from matplotlib import pyplot as plt
from numpy.lib.function_base import sin

x = np.arange(-1000,1000,1) 

y = sin(100*x)**2/x**2




plt.plot(x,y)

plt.show()