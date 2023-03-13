import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def scatterPlot(data, binary_response, corr_dict_sorted):
    # Select the three variables with highest absolute correlation coefficients
    high_abs_corr_vars = [k for k, v in corr_dict_sorted.items() if v['corr_signed'] > 0][:3]
    # Select the three variables with lowest absolute correlation coefficients
    low_abs_corr_vars = [k for k, v in corr_dict_sorted.items() if v['corr_signed'] < 0][:3]

    # Plot scatter plots with regression lines for each variable
    fig, axs = plt.subplots(nrows=2, ncols=3)
    for i, var in enumerate(high_abs_corr_vars + low_abs_corr_vars):
        row_idx = i // 3
        col_idx = i % 3
        ax = axs[row_idx, col_idx]

        x = binary_response.iloc[:, 0]
        y = data[var]

        # scatter plot
        ax.scatter(x, y)

        # linear regression line
        slope, intercept = np.polyfit(x, y, 1)
        line_x = np.array([x.min(), x.max()])
        line_y = slope * line_x + intercept
        ax.plot(line_x, line_y, color='red')

        # set title
        corr_abs = corr_dict_sorted[var]['corr_abs']
        corr_signed = corr_dict_sorted[var]['corr_signed']
        ax.set_title(f"{var}\n signed_corr={corr_signed:.2f}")

    plt.tight_layout()
    plt.show()