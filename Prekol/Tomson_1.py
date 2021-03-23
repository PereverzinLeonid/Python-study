import matplotlib.pyplot as plt
import numpy as np

Delta_Pressure = [3.9, 3.5, 3.0, 2.5, 2.0, 1.5, 1]
Delta_Temperature = [2.80, 2.41, 1.89, 1.52, 0.98, 0.54, 0.05]

# изображение точек
plt.errorbar(Delta_Pressure, Delta_Temperature, xerr=0.1, yerr=0.07, ls='none')
plt.grid()
# подпись осей
plt.xlabel('Перепад давления, Бар')
plt.ylabel('Перевад температуры, K')
# подпись графика
plt.title("Зависимость перепада температуры \n от перепада давления при температуре $22^{\circ}$C")
# границы осей
plt.xlim(0.5, 4)
plt.ylim(-0.5, 3)
# провожу апрокимирующую прямую
x = np.arange(-0.5, 4.001, 0.001)
plt.plot(x * 1.03 + 1, x)

plt.show()
