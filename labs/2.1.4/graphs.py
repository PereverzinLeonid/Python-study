import matplotlib.pyplot as plt
import numpy as np

# Empty calorimeter (тут выкинул 2 помойные точки, первые точки, они содержали большую ошибку)

R_0 = [18.327, 18.377, 18.427, 18.477, 18.527, 18.577, 18.627, 18.677, 18.727, 18.777] # resistance
T_0 = [75, 118, 164, 210, 259, 308, 359, 411, 465, 520] # time
dR_dt_0 = [] #dR/dt
for i in range(len(R_0) - 1):
    dR_dt_0.append( (R_0[i+1] - R_0[i]) / (T_0[i+1] - T_0[i]) )

# Empty calorimeter and aluminum (выкинул 1, 4 и 5 точки сначала и 1, 2 с конца)

R_1 = [18.019, 18.069, 18.190, 18.269, 18.319, 18.369, 18.419, 18.469, 18.519, 18.569, 18.619, 18.669, 18.719, 18.769, 18.819] # resistance
T_1 = [25, 76, 257, 321, 385, 452, 520, 590, 663, 736, 811, 888, 967, 1045, 1125] # time
dR_dt_1 = [] #dR/dt
for i in range(len(R_1) - 1):
    dR_dt_1.append( (R_1[i+1] - R_1[i]) / (T_1[i+1] - T_1[i]) )

# Empty calorimeter and iron  (выкинул 1, 2, 3 и 4 сначала точки)

R_2 = [18.352, 18.402, 18.452, 18.502, 18.552, 18.602, 18.652, 18.702, 18.752, 18.802, 18.852, 18.902, 18.952] # resistance
T_2 = [203, 274, 348, 423, 502, 582, 663, 748, 835, 923, 1013, 1106, 1206] # time
dR_dt_2 = [] #dR/dt
for i in range(len(R_2) - 1):
    dR_dt_2.append((R_2[i+1] - R_2[i]) / (T_2[i+1] - T_2[i]))

# Empty calorimeter and brass (выкинул 1 и 2 сначала точки)

R_3 = [18.378, 18.428, 18.478, 18.528, 18.578, 18.628, 18.678, 18.728, 18.778, 18.828, 18.878, 18.928, 18.978, 19.028, 19.078] # resistance
T_3 = [101, 167, 235, 306, 379, 455, 532, 611, 693, 776, 863, 951, 1044, 1136, 1232] # time
dR_dt_3 = [] #dR/dt
for i in range(len(R_3) - 1):
    dR_dt_3.append( (R_3[i+1] - R_3[i]) / (T_3[i+1] - T_3[i]) )

# R(t)

# # изображение точек R(t)
# plt.errorbar(T_0, R_0, xerr=2, yerr=0.005, ls='none', label = "Empty calorimeter")
# plt.errorbar(T_1, R_1, xerr=2, yerr=0.005, ls='none', label = "Empty calorimeter and aluminum")
# plt.errorbar(T_2, R_2, xerr=2, yerr=0.005, ls='none', label = "Empty calorimeter and iron")
# plt.errorbar(T_3, R_3, xerr=2, yerr=0.005, ls='none', label = "Empty calorimeter and brass")

# изображение точек dR/dt

# plt.errorbar(R_0[1:], dR_dt_0, xerr=0, yerr=0.00001, ls='none')
# plt.errorbar(R_1[1:], dR_dt_1, xerr=0, yerr=0.00001, ls='none')
# plt.errorbar(R_2[1:], dR_dt_2, xerr=0, yerr=0.00001, ls='none')
# plt.errorbar(R_3[1:], dR_dt_3, xerr=0, yerr=0.00001, ls='none')

# косметика R(t)
# plt.legend()
# plt.grid()
# plt.xlabel('time, s')
# plt.ylabel('resistance, ohm')
# plt.title("Time dependence of resistivity")
# plt.ylim(18, 19.2)
# plt.xlim(0, 1300)

# косметика dR/dt
# plt.grid()
# plt.xlabel('resistance, ohm')
# plt.ylabel('dR/dt, ohm/s')
# plt.title("Dependence of the rate of change of resistance on the resistance \n Empty calorimeter")
# plt.title("Dependence of the rate of change of resistance on the resistance \n Empty calorimeter and aluminum")
# plt.title("Dependence of the rate of change of resistance on the resistance \n Empty calorimeter and iron")
# plt.title("Dependence of the rate of change of resistance on the resistance \n Empty calorimeter and brass")
# plt.xlim() # 1 график
# plt.ylim(0.0008, 0.0013)
# plt.xlim(18.0, 18.9) # 2 график
# plt.ylim(0.0006, 0.001)
# plt.xlim(18.4, 19.0) # 3 график
# plt.ylim(0.0005, 0.0007)
# plt.xlim(18.4, 19.1) # 1 график
# plt.ylim(0.0005, 0.0008)

# апроксимация dR/dt(R)
# plt.plot(np.arange(18.30, 18.81, 0.01), np.polyval(np.polyfit(R_0[1:], dR_dt_0, 2), np.arange(18.30, 18.81, 0.01))) # 1 график
# plt.plot(np.arange(18.0, 18.91, 0.01), np.polyval(np.polyfit(R_1[1:], dR_dt_1, 2), np.arange(18.0, 18.91, 0.01))) # 1 график
# plt.plot(np.arange(18.2, 19.01, 0.01), np.polyval(np.polyfit(R_2[1:], dR_dt_2, 2), np.arange(18.2, 19.01, 0.01))) # 3 график
# plt.plot(np.arange(18.3, 19.11, 0.01), np.polyval(np.polyfit(R_3[1:], dR_dt_3, 2), np.arange(18.3, 19.11, 0.01))) # 4 график

print(np.polyval(np.polyfit(R_0[1:], dR_dt_0, 2), 18.105)) # 1 график (результат экстраполяции)
print(np.polyval(np.polyfit(R_1[1:], dR_dt_1, 2), 18.105)) # 2 график (результат экстраполяции)
print(np.polyval(np.polyfit(R_2[1:], dR_dt_2, 2), 18.105)) # 3 график (результат экстраполяции)
print(np.polyval(np.polyfit(R_3[1:], dR_dt_3, 2), 18.105)) # 4 график (результат экстраполяции)


plt.show()
