import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 

# 1D
x = np.random.rand(40,1)
y = np.ones(len(x))
plt.figure
plt.scatter(x , y)
plt.xlabel('1D points')
plt.show()

# 2D
points = np.random.rand(40,2)
plt.figure
plt.scatter(points[:,0], points[:,1])
plt.xlabel('2D points')
plt.show()

# 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
points = np.random.rand(40,3)
ax.scatter(points[:,0], points[:,1], points[:,2])
plt.show()