import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def extract_real_imag(l_c):
    l_real = []
    l_imag = []
    for c in l_c:
        l_real.append(c.real)
        l_imag.append(c.imag)

    return l_real, l_imag


if __name__ == '__main__':
    m = 0
    nu = 0.1
    siz = 1024

    visu = False

    # 1 compute array of 1000 eleent with normal distribution
    in_data = np.random.normal(m, nu, siz)
    # 2 compute FFT on data
    fft_data = np.fft.fft(in_data)
    # 3 export data in Pandas
    fft_real, fft_imag = extract_real_imag(fft_data)
    df = pd.DataFrame()
    df['input'] = in_data
    df['fft_real'] = fft_real
    df['fft_imag'] = fft_imag
    df.to_csv('data_fft.csv')

    if visu is True:
        plt.figure(0)
        plt.plot(in_data)
        plt.plot(fft_data)
        plt.show()
