import numpy as np

def my_transpose(m:list) -> list:
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def numpy_transpose(m:list) -> list:
    return np.array(m)