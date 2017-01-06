#!/usr/bin/env python

import pywt
# import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    data = pd.read_table('./sample.txt', header=None, encoding='gb2312', delim_whitespace=True)
    (cA, cD) = pywt.dwt(data[1], 'db1')
    print(type(cA))
    print(cA)
    # plt.plot(cA)
    # plt.plot(data[2])
