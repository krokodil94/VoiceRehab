import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import getData
import scatterPlot
from scipy.stats import pearsonr, rv_histogram
import normalDist

data,binaryResponse,classes = getData.extractData()
corr_dict_sorted = getData.calculatePearsonCoefficient(data,binaryResponse)
scatterPlot = scatterPlot.scatterPlot(data,binaryResponse,corr_dict_sorted)
normalDistribution = normalDist.normalDistr(data,classes,corr_dict_sorted)
print(corr_dict_sorted)
print(data,binaryResponse)

"""# Calculate Pearson correlation coefficients and store in a dictionary
corr_dict = {}
for col in Data.columns:
    corr, _ = pearsonr(Data[col], BinaryResponse.iloc[:, 0])
    corr_dict[col] = abs(corr)

# Sort correlation coefficients by absolute value
sorted_corr = sorted(corr_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_corr)
# Choose the column with the highest absolute correlation coefficient
highest_corr_col = sorted_corr[0][0]

# Get every (1+n) where n is a multiple of 3, starting from 0
indices_1 = np.arange(0, len(Data), step=4)
indices_2 = np.arange(1, len(Data), step=4)
indices_3 = np.arange(2, len(Data), step=4)

# Select the values from the chosen column at the selected indices
values_1 = Data[highest_corr_col].iloc[indices_1]
values_2 = Data[highest_corr_col].iloc[indices_2]
values_3 = Data[highest_corr_col].iloc[indices_3]
# Calculate the PDFs of the selected values using normal distributions
mu_1, std_1 = norm.fit(values_1)
mu_2, std_2 = norm.fit(values_2)
mu_3, std_3 = norm.fit(values_3)

xmin, xmax = min(values_1.min(), values_2.min(), values_3.min()), max(values_1.max(), values_2.max(), values_3.max())
x = np.linspace(xmin, xmax, 100)
p_1 = norm.pdf(x, mu_1, std_1)
p_2 = norm.pdf(x, mu_2, std_2)
p_3 = norm.pdf(x, mu_3, std_3)

# Plot the PDFs on the same graph
plt.plot(x, p_1, 'r', linewidth=2, label='(1+n)')
plt.plot(x, p_2, 'g', linewidth=2, label='(2+n)')
plt.plot(x, p_3, 'b', linewidth=2, label='(3+n)')
plt.xlabel(highest_corr_col)
plt.ylabel('PDF')
plt.legend()
plt.show()

"""