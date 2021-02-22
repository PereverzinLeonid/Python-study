import numpy as np

x = float(input())

y = np.log( ( np.e ** ( 1 / ( 1 + np.sin(x) ) ) ) / ( 1.25 + 1 / (5 * x) ) ) / np.log(1 + x ** 2)

print(y)
