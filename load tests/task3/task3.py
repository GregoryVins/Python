import os
import numpy as np

print('Введите путь к каталогу с файлами:')
path = input()
summ = []
files = os.listdir(path)

data1 = np.genfromtxt(path + r'\\' + files[0], delimiter='\t', dtype=np.float)
data2 = np.genfromtxt(path + r'\\' + files[1], delimiter='\t', dtype=np.float)
data3 = np.genfromtxt(path + r'\\' + files[2], delimiter='\t', dtype=np.float)
data4 = np.genfromtxt(path + r'\\' + files[3], delimiter='\t', dtype=np.float)
data5 = np.genfromtxt(path + r'\\' + files[4], delimiter='\t', dtype=np.float)

i = 0
while i != 16:
    summ.append("%.2f" % (data1[i] + data2[i] + data3[i] + data3[i] + data4[i] + data5[i]))
    i += 1

print(summ.index(max(summ)) + 1)

input()
