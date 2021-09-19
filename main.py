import numpy as np
import matplotlib.pyplot as plt
import csv

plt.rcParams.update({'font.size':18})
coefficient = 0.75
with open('fake_fingerprint_mean.csv','r')as f:
    f_csv = csv.reader(f)
    for row1 in f_csv:
        row1 = [float(i) for i in row1]
with open('fake_fingerprint_std.csv','r')as f:
    f_csv = csv.reader(f)
    for row2 in f_csv:
        row2 = [float(i) for i in row2]
with open('real_fingerprint_mean.csv','r')as f:
    f_csv = csv.reader(f)
    for row3 in f_csv:
        row3 = [float(i) for i in row3]
with open('real_fingerprint_std.csv','r')as f:
    f_csv = csv.reader(f)
    for row4 in f_csv:
        row4 = [float(i) for i in row4]
xf = np.arange(start=0,stop=128,step=1)
row_numpy1 = np.array(row1)
row_numpy2 = np.array(row2)
row_numpy3 = np.array(row3)
row_numpy4 = np.array(row4)
plt.plot(xf,row_numpy1,color='green',linewidth=1.5,label='fake')
plt.plot(xf,row_numpy3,color='darkred',linewidth=1.5,label='real')
plt.legend(title='fingerprint')
plt.fill_between(xf,row_numpy1-coefficient*row_numpy2,row_numpy1+coefficient*row_numpy2,color='lime',alpha=0.35)
plt.fill_between(xf,row_numpy3-coefficient*row_numpy4,row_numpy3+coefficient*row_numpy4,color='red',alpha=0.35)
plt.show()