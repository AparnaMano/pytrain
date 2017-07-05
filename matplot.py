import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import scipy as sp
import matplotlib.pyplot as plt
a=np.array([1,2])
b=np.array([2,1])

print(np.dot(a,b))
print(a.dot(b))

#going with plotting
x=np.linspace(0,10,100)
y=np.sin(x)

plt.plot(x, y)
plt.show()
