import pandas as pd
from scipy.stats import pearsonr


def extractData():
    data = pd.read_excel('DataExcel.xlsx', sheet_name='Data')
    binaryResponse = pd.read_excel('DataExcel.xlsx', sheet_name='Binary response')
    classes = binaryResponse[binaryResponse.columns[0]].tolist()

    return (data, binaryResponse, classes)

def calculatePearsonCoefficient(data,binaryResponse):
    corr_dict = {}
    for col in data.columns:
        corr, _ = pearsonr(data[col], binaryResponse.iloc[:, 0])
        corr_dict[col] = {'corr_abs': abs(corr), 'corr_signed': corr}
        corr_dict_sorted = dict(sorted(corr_dict.items(), key=lambda x: x[1]['corr_abs'], reverse=True))
    return corr_dict_sorted
    d