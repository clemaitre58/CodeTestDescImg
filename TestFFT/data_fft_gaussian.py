import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    m = 0
    nu = 0.1
    siz = 1024

    visu = True

    # 1 compute array of 1000 eleent with normal distribution
    in_data = np.random.normal(m, nu, siz)
    # 2 compute FFT on data
    fft_data = np.fft.fft(in_data)

    if visu is True:
        plt.figure(0)
        plt.plot(in_data)
        plt.plot(fft_data)
        plt.show()

