import matplotlib.pyplot as plt
import numpy as np

T= float(input("input T = "))
t = np.linspace(0, 10, 100)
y = np.sin(2*np.pi*1/T*t)
plt.plot(t, y)
plt.title("Sine Curve")
plt.xlabel("time")
plt.ylabel("y")
plt.grid(False)
plt.show()


# temps = [28, 31, 33, 35, 27, 26, 25] 
# values = list(temps)


# values[0] = 20

# print(temps, values)