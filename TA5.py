# 2D Transient Heat Conduction

import numpy as np
import matplotlib.pyplot as plt

H = 1
L = 1
nx = 50
ny = 50
dx = L / (nx - 1)
dy = H / (ny - 1)

nt = 500
alpha = 0.0001
dt = (dx ** 2)/(4 * alpha)
# t_tot = dt * nt
s1 = (alpha * dt )/(dx ** 2)
s2 = (alpha * dt )/(dy ** 2)

'''----------------------------------------'''

x = np.linspace(0, 1, nx) #linspace = linear space
y = np.linspace(0, 1, ny)

X, Y = np.meshgrid(x,y)

'''----------------------------------------'''

# I.C.
Ti = 300
T = np.ones((ny,nx)) * Ti

# B.C.
T[0 , : ] = 300
T[-1, : ] = 400 # or T[ny - 1 , : ]
T[ : , 0 ] = 273
T[ : , -1] = 273

Tn = T

for n in range(1, nt+1):
    for j in range(1, nx-1):
        for i in range(1, ny-1):

            T[i, j] = Tn[i, j] + s2 * (Tn[i - 1, j] - 2 * (Tn[i, j]) + Tn[i + 1, j]) + s1 * (Tn[i , j - 1] - 2 * (Tn[i, j]) + Tn[i, j + 1])
            #T[j, i] dorost tar bood Shayad!
    Tn = T

plt.contourf(X, Y, T, cmap = "turbo")
plt.colorbar(label = "Temperature (K) ")
plt.xlabel("X (m) ")
plt.ylabel("Y (m) ")
plt.title("2D Transient Heat Conduction")
plt.show()