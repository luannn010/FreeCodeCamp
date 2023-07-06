import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    calculations = {}
    matrix = np.array(list).reshape(3,3)
    # mean
    mean_values = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()]
    calculations['mean'] = mean_values
    # variance
    variance_values = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()]
    calculations['variance'] = variance_values
    # standard deviation
    standard_deviation_values = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()]
    calculations['standard deviation'] = standard_deviation_values
    # max
    max_values = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()]
    calculations['max'] = max_values
    # min
    min_values = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()]
    calculations['min'] = min_values
    # sum
    sum_values = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
    calculations['sum'] = sum_values
    return calculations





