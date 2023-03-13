import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import pearsonr


def normalDistr(Data, classes, corr_dict_sorted):
    variables = list(corr_dict_sorted.keys())[:3] + list(corr_dict_sorted.keys())[-3:]
    y = Data[variables].values  # select the columns corresponding to the variables
    acceptable = []
    unacceptable = []

    for i, x in enumerate(y):
        if classes[i] == 1:
            acceptable.append(x)
        else:
            unacceptable.append(x)

    # Create a figure with 6 subplots
    fig, axs = plt.subplots(2, 6, figsize=(15, 10))

    # Create a histogram with 20 bins for each of the 3 top variables
    for i in range(3):
        axs[0, i].hist([sublist[i] for sublist in acceptable], bins=20, color='blue', alpha=0.5)
        axs[0, i].hist([sublist[i] for sublist in unacceptable], bins=20, color='red', alpha=0.5)
        axs[0, i].set_xlabel('Range')
        axs[0, i].set_ylabel('Number')
        axs[0, i].set_title(variables[i])
        axs[0, i].legend(['Acceptable', 'Unacceptable'])

    # Create a kde plot for each of the 3 top variables
    for i in range(3):
        sns.kdeplot([sublist[i] for sublist in acceptable], ax=axs[1, i], color='blue')
        sns.kdeplot([sublist[i] for sublist in unacceptable], ax=axs[1, i], color='red')
        axs[1, i].set_xlabel('Range')
        axs[1, i].set_ylabel('Number')
        axs[1, i].set_title(variables[i])
        axs[1, i].legend(['Acceptable', 'Unacceptable'])

    # Create a histogram with 20 bins for each of the 3 bottom variables
    for i in range(3):
        axs[0, i + 3].hist([sublist[-(i + 1)] for sublist in acceptable], bins=20, color='blue', alpha=0.5)
        axs[0, i + 3].hist([sublist[-(i + 1)] for sublist in unacceptable], bins=20, color='red', alpha=0.5)
        axs[0, i + 3].set_xlabel('Range')
        axs[0, i + 3].set_ylabel('Number')
        axs[0, i + 3].set_title(variables[-(i + 1)])
        axs[0, i + 3].legend(['Acceptable', 'Unacceptable'])

    # Create a kde plot for each of the 3 bottom variables
    for i in range(3):
        sns.kdeplot([sublist[-(i + 1)] for sublist in acceptable], ax=axs[1, i + 3], color='blue')
        sns.kdeplot([sublist[-(i + 1)] for sublist in unacceptable], ax=axs[1, i + 3], color='red')
        axs[1, i + 3].set_xlabel('Range')
        axs[1, i + 3].set_ylabel('Number')
        axs[1, i + 3].set_title(variables[-(i + 1)])
        axs[1, i + 3].legend(['Acceptable', 'Unacceptable'])

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Show the plot
    plt.show()
