import matplotlib.pyplot as plt
import numpy as np
x = [21.3, 25.1, 30.1, 35.1, 40.1, 45.1, 50.1, 55.1, 60.4]
y = [60.2086, 58.5322, 57.6422, 55.7522, 54.8622, 52.9722, 51.0822, 49.1922, 48.2488]
plt.errorbar(x, y, xerr=0.1, yerr=1.43, ls='none')
plt.grid()
plt.xlabel('Tемпература, K') # подпись осей
plt.ylabel('Поверхностная энергия единицы площади, Дж/м^2')
plt.title("Зависимость поверхностной энергии единицы площади от температуры") # подпись графика
p, v = np.polyfit(x, y, deg=1, cov=True)
p_f = np.poly1d(p)
a = p_f(20)
b = p_f(60)
x = np.arange(15, 62.01, 0.01)
plt.plot(x, -x * 0.356 + 68)
plt.show()