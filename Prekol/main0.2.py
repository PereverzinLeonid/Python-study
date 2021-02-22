import matplotlib.pyplot as plt
import numpy as np
x = [21.3, 25.1, 30.1, 35.1, 40.1, 45.1, 50.1, 55.1, 60.4]
y = [64, 63, 63, 62, 62, 61, 60, 59, 59]
plt.errorbar(x, y, xerr=0.1, yerr=1, ls='none')
plt.grid()
plt.xlabel('Tемпература, K') # подпись осей
plt.ylabel('Поверхностное натяжение, мH/м')
plt.title("Зависимость поверхностного натяжения воды от температуры") # подпись графика
p, v = np.polyfit(x, y, deg=1, cov=True)
p_f = np.poly1d(p)
print(v)
a = p_f(20)
b = p_f(60)
x = np.arange(15, 67.01, 0.01)
plt.plot(x, x * (b-a) / 40 + (3*a-b)/2)
plt.show()
