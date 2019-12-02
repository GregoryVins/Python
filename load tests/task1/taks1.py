import numpy as np


print('Enter PATH to file:')
PATH = input()
data = np.genfromtxt(PATH, delimiter='\t', dtype=np.int)
print("%.2f" % np.percentile(data, 90))
print("%.2f" % np.median(data))
print("%.2f" % max(data))
print("%.2f" % min(data))
print("%.2f" % np.average(data))
input()


