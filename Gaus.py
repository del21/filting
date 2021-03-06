import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import pandas as pd


ap = pd.read_excel('Abbott_probes.xlsx')
print('Choose the range of visible wavelenght')
rofw = str(input())
print(ap)

# For SpectrumRed 
x_phot_min = 300
x_phot_max = 800
x_filt_min = 300
x_filt_max = 800
current_row = ap[ap.probes.isin([rofw])]
print(ap['ex_width'])
ex_peak = current_row
print(ex_peak)
ex_width = 39
em_peak = 675
em_width = 39
filt_peak = 647
filt_width = 70

def spectrums(ex_peak,ex_width,em_peak,em_width,rofw):
    x_phot = np.linspace(x_phot_min, x_phot_max, 1000)
    x_filt = np.linspace(x_filt_min, x_filt_max, 1000)

    y_ex = scipy.stats.norm.pdf(x_phot,ex_peak,ex_width)
    y_em = scipy.stats.norm.pdf(x_phot,em_peak,em_width)
    y_filt = scipy.stats.norm.pdf(x_filt,filt_peak,filt_width)

    plt.plot(x_phot, y_ex, color='blue')
    plt.plot([ex_peak for i in range(len(x_phot))], [i for i in range(len(x_phot))], linestyle='--', color='blue')
    plt.plot(x_phot, y_em, color='red')
    plt.plot([em_peak for i in range(len(x_phot))], [i for i in range(len(x_phot))], linestyle='--', color='red')
    plt.plot(x_phot, y_filt, color='black')
    plt.plot([filt_peak for i in range(len(x_phot))], [i for i in range(len(x_phot))], linestyle='--', color='black')

    plt.grid()

    plt.xlim(400, 800)
    plt.ylim(0,0.012)

    plt.title('SpectrumRed',fontsize=10)

    plt.xlabel('Wavelenght')
    plt.ylabel('I')
    plt.show()
    return(plt.savefig(f"Spectrum{rofw}.png"))