import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

f = pd.read_excel('filters.xlsx')
peaks = list(f['cwl'])
em_peak = 369
current_peak = 0
for peak in peaks:
    if abs(em_peak - peak) < abs(em_peak - current_peak):
        current_peak = peak
best_filter_p = f[f.cwl == current_peak]
filt_peak = int(best_filter_p.cwl)
filt_width = int(best_filter_p.fwhm)
print(best_filter_p)