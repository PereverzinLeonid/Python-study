import matplotlib.pyplot as plt
import numpy as np
import math as m

# set of voltages

U_1 = [21.02, 19.47, 18.10, 16.81, 15.61, 14.49, 13.46, 12.55, 11.72, 10.90, 10.13]

U_2 = [18.42, 17.88, 17.27, 16.74, 16.25, 15.80, 14.90, 14.47, 14.06, 13.69, 13.30, 12.97, 12.60, 12.26, 11.94, 11.59, 11.26, 10.95, 10.65, 10.35, 10.08, 9.80, 9.54, 9.27, 9.01, 8.81]

U_3 = [16.01, 15.79, 15.50, 15.25, 14.98, 14.68, 14.43, 14.17, 13.90, 13.64, 13.38, 13.12, 12.89, 12.51, 12.38, 12.18, 11.96, 11.76, 11.52, 11.33, 11.13]

U_4 = [16.00, 15.81, 15.68, 15.49, 15.28, 15.08, 14.71, 14.53, 14.35, 14.20, 14.02, 13.82, 13.65, 13.48, 13.30, 13.12, 12.96, 12.80, 12.62, 12.46, 12.31, 12.16, 12.01, 11.85, 11.68, 11.56, 11.41, 11.26, 11.13, 10.96, 10.83, 10.70, 10.54, 10.40, 10.27, 10.16]

U_5 = [15.40, 15.30, 15.20, 15.03, 14.89, 14.72, 14.58, 14.41, 14.27, 13.99, 13.82, 13.69, 13.54, 13.41, 13.26, 13.14, 13.00, 12.86, 12.70, 12.60, 12.47, 12.33, 12.21, 12.06, 11.99, 11.83, 11.71, 11.58, 11.47, 11.37, 11.26, 11.14, 11.02, 10.88, 10.80, 10.69, 10.57, 10.49, 10.37, 10.26, 10.15, 10.07, 9.96, 9.86, 9.78]

# plt.xlabel('time, s')
# plt.ylabel('voltage, mV')
# plt.title("Time dependence of voltage")
# plt.xlim(0, 450)
# plt.ylim(8, 20)

# изображение точек в обычном масштабе
# plt.errorbar(np.arange(0, 10 * len(U_1), 10), U_1, xerr=1, yerr=0.03, ls='none', label = "1 experiment")
# plt.title("Time dependence of voltage (1 experiment, linear)")
# plt.xlim(0, 100)
# plt.ylim(10, 22)

# plt.errorbar(np.arange(0, 10 * len(U_2), 10), U_2, xerr=1, yerr=0.03, ls='none', label = "2 experiment")
# plt.title("Time dependence of voltage (2 experiment, linear)")
# plt.xlim(0, 250)
# plt.ylim(8, 19)

# plt.errorbar(np.arange(0, 10 * len(U_3), 10), U_3, xerr=1, yerr=0.03, ls='none', label = "3 experiment")
# plt.title("Time dependence of voltage (3 experiment, linear)")
# plt.xlim(0, 200)
# plt.ylim(11, 16)

# plt.errorbar(np.arange(0, 10 * len(U_4), 10), U_4, xerr=1, yerr=0.03, ls='none', label = "4 experiment")
# plt.title("Time dependence of voltage (4 experiment, linear)")
# plt.xlim(0, 350)
# plt.ylim(10, 16)

# plt.errorbar(np.arange(0, 10 * len(U_5), 10), U_5, xerr=1, yerr=0.03, ls='none', label = "5 experiment")
# plt.title("Time dependence of voltage (5 experiment, linear)")
# plt.xlim(0, 450)
# plt.ylim(9, 16)

LN_U_1 = []
for i in range(len(U_1)):
    LN_U_1.append(m.log(U_1[i]))
LN_U_2 = []
for i in range(len(U_2)):
    LN_U_2.append(m.log(U_2[i]))
LN_U_3 = []
for i in range(len(U_3)):
    LN_U_3.append(m.log(U_3[i]))
LN_U_4 = []
for i in range(len(U_4)):
    LN_U_4.append(m.log(U_4[i]))
LN_U_5 = []
for i in range(len(U_5)):
    LN_U_5.append(m.log(U_5[i]))

# plt.xlabel('time, s')
# plt.ylabel('logarithm voltage, ln(mV)')
# plt.title("Time dependence of logarithm voltage")
# plt.xlim(0, 450)
# plt.ylim(2.2, 3.0)

# изображение в логирифмическом масштабе
# plt.errorbar(np.arange(0, 10 * len(U_1), 10), LN_U_1, xerr=1, yerr=0.003, ls='none', label = "1 experiment")
# plt.title("Time dependence of voltage (1 experiment, logarithmic)")
# plt.xlim(0, 100)
# plt.ylim(2.3, 3.1)
# plt.plot(np.arange(0, 100.0, 0.1), np.polyval(np.polyfit(np.arange(0, 10 * len(U_1), 10), LN_U_1, 1), np.arange(0, 100.0, 0.1))) # 1 график
print(np.polyfit(np.arange(0, 10 * len(U_1), 10), LN_U_1, 1)) # параметры прямых
print(3300 * np.polyfit(np.arange(0, 10 * len(U_1), 10), LN_U_1, 1)[0]) # коэф диффузии
# plt.errorbar(np.arange(0, 10 * len(U_2), 10), LN_U_2, xerr=1, yerr=0.003, ls='none', label = "2 experiment")
# plt.title("Time dependence of voltage (2 experiment, logarithmic)")
# plt.xlim(0, 250)
# plt.ylim(2.1, 3)
# plt.plot(np.arange(0, 250.0, 0.1), np.polyval(np.polyfit(np.arange(0, 10 * len(U_2), 10), LN_U_2, 1), np.arange(0, 250.0, 0.1))) # 2 график
print(np.polyfit(np.arange(0, 10 * len(U_2), 10), LN_U_2, 1)) # параметры прямых
print(3300 * np.polyfit(np.arange(0, 10 * len(U_2), 10), LN_U_2, 1)[0]) # коэф диффузии
# plt.errorbar(np.arange(0, 10 * len(U_3), 10), LN_U_3, xerr=1, yerr=0.003, ls='none', label = "3 experiment")
# plt.title("Time dependence of voltage (3 experiment, logarithmic)")
# plt.xlim(0, 200)
# plt.ylim(2.4, 2.8)
# plt.plot(np.arange(0, 200.0, 0.1), np.polyval(np.polyfit(np.arange(0, 10 * len(U_3), 10), LN_U_3, 1), np.arange(0, 200.0, 0.1))) # 3 график
print(np.polyfit(np.arange(0, 10 * len(U_3), 10), LN_U_3, 1)) # параметры прямых
print(3300 * np.polyfit(np.arange(0, 10 * len(U_3), 10), LN_U_3, 1)[0]) # коэф диффузии
# plt.errorbar(np.arange(0, 10 * len(U_4), 10), LN_U_4, xerr=1, yerr=0.003, ls='none', label = "4 experiment")
# plt.title("Time dependence of voltage (4 experiment, logarithmic)")
# plt.xlim(0, 350)
# plt.ylim(2.3, 2.8)
# plt.plot(np.arange(0, 350.0, 0.1), np.polyval(np.polyfit(np.arange(0, 10 * len(U_4), 10), LN_U_4, 1), np.arange(0, 350.0, 0.1))) # 4 график
print(np.polyfit(np.arange(0, 10 * len(U_4), 10), LN_U_4, 1)) # параметры прямых
print(3300 * np.polyfit(np.arange(0, 10 * len(U_4), 10), LN_U_4, 1)[0]) # коэф диффузии
# plt.errorbar(np.arange(0, 10 * len(U_5), 10), LN_U_5, xerr=1, yerr=0.003, ls='none', label = "5 experiment")
# plt.title("Time dependence of voltage (5 experiment, logarithmic)")
# plt.xlim(0, 450)
# plt.ylim(2.2, 2.8)
# plt.plot(np.arange(0, 450.0, 0.1), np.polyval(np.polyfit(np.arange(0, 10 * len(U_5), 10), LN_U_5, 1), np.arange(0, 450.0, 0.1))) # 5 график
print(np.polyfit(np.arange(0, 10 * len(U_5), 10), LN_U_5, 1)) # параметры прямых
print(3300 * np.polyfit(np.arange(0, 10 * len(U_5), 10), LN_U_5, 1)[0]) # коэф диффузии
# Коэффицент диффузии

data = [24.02056437870614, 9.700366611197799, 6.118697561392433, 4.305185977667603, 3.4631245356950893]
error_data = [1.5, 0.3, 0.3, 0.2, 0.1]
pressure = [0.025, 0.01, 0.006, 0.005, 0.004]

plt.plot(np.arange(0, 0.0301, 0.0001), np.polyval(np.polyfit(pressure, data, 1), np.arange(00, 0.0301, 0.0001)))
plt.errorbar(pressure, data, xerr=0, yerr = error_data, ls='none')
plt.xlabel('back pressure, 1/pa')
plt.ylabel('diffusion coefficient, (sm^2)/s')
plt.title("Time dependence of logarithm voltage")
plt.xlim(0, 0.03)
plt.ylim(0, 25)
print(np.polyfit(pressure, data, 1))

# косметика общая

plt.legend()
plt.grid()


plt.show()
