import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

ap = pd.read_excel('Abbott_probes.xlsx')
print('Input a probe (f.e. SpectrumGold). ATTENTION!!! Probe have to be within Abbott_probes')
fc_name = str(input())
def current_parameters(fc_name):
    parameters = {}
    parameters['ex_peak'] = int(ap[ap.probes == fc_name].ex_peak)
    parameters['ex_width'] = int(ap[ap.probes == fc_name].ex_width)
    parameters['em_peak'] = int(ap[ap.probes == fc_name].em_peak)
    parameters['em_width'] = int(ap[ap.probes == fc_name].em_width)
    return parameters

def spectrums(parameters, fc_name):
    f = pd.read_excel('filters.xlsx')
    peaks = list(f['cwl'])
    current_peak = 0
    for peak in peaks:
        if (parameters.get('em_peak') - peak) < (parameters.get('em_peak') - current_peak) and (parameters.get('em_peak') - peak) > 0:
            current_peak = peak
    best_filter_p = f[f.cwl == current_peak]
    filt_peak = int(best_filter_p.cwl)
    filt_width = int(best_filter_p.fwhm)

    x_phot_min = 300
    x_phot_max = 800
    x_filt_min = 300
    x_filt_max = 800
    ex_peak = parameters.get('ex_peak')
    ex_width = parameters.get('ex_width')
    em_peak = parameters.get('em_peak')
    em_width = parameters.get('em_width')
    x_phot = np.linspace(x_phot_min, x_phot_max, 1000)
    x_filt = np.linspace(x_filt_min, x_filt_max, 1000)

    y_ex = scipy.stats.norm.pdf(x_phot,ex_peak,ex_width)
    y_em = scipy.stats.norm.pdf(x_phot,em_peak,em_width)
    y_filt = scipy.stats.norm.pdf(x_filt,filt_peak,filt_width)

    plt.plot(x_phot, y_ex, color='blue', label=f'ex_peak = {ex_peak}')
    # plt.plot([ex_peak for i in range(len(x_phot))], [i for i in range(len(x_phot))], linestyle='--', color='blue')
    plt.plot(x_phot, y_em, color='red', label=f'em_peak = {em_peak}')
    # plt.plot([em_peak for i in range(len(x_phot))], [i for i in range(len(x_phot))], linestyle='--', color='red')
    plt.plot(x_phot, y_filt, color='black', label=f'filter with peak in {filt_peak}')
    # plt.plot([filt_peak for i in range(len(x_phot))], [i for i in range(len(x_phot))], linestyle='--', color='black')

    plt.grid()

    plt.xlim(400, 800)
    plt.ylim(0,0.02)

    plt.title(fc_name,fontsize=10)

    plt.xlabel('Wavelenght')
    plt.ylabel('I')
    legend = plt.legend(loc='best', shadow=True, fontsize='small')
    plt.show()
    return(plt.savefig(f"{fc_name}.png"))

parameters = current_parameters(fc_name)
spectrums(parameters, fc_name)