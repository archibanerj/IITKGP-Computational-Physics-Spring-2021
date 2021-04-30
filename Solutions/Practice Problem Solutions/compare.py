import Rk2
import Rk4
import eulerMethod as eul
import matplotlib.pyplot as plt
import numpy as np

x_initial = 0
t_initial = 0
t_stop = 10
dt = 0.01

t1,x1 = eul.solve(x_initial,t_initial,t_stop,dt)
t2,x2 = Rk2.solve(x_initial,t_initial,t_stop,dt)
t3,x3 = Rk4.solve(x_initial,t_initial,t_stop,dt)

plt.plot(t1,x1, label = 'Rk1')
plt.plot(t2,x2, label = 'Rk2')
plt.plot(t3,x3, label = 'Rk4')

plt.legend()

plt.show()
