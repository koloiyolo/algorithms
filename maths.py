import numpy as np
import math

def getmin(data):
    min = list(data[0])
    for elem in data:
        for i, value in enumerate(elem):
            if min[i] > value:
                min[i] = math.floor(elem[i])
    return min


def getmax(data):
    max = list(data[0])
    for elem in data:
        for i, value in enumerate(elem):
            if max[i] < value:
                max[i] = math.ceil(elem[i])
    return max

def euclidean_distance(point1, point2):
    sum = 0
    for val1, val2 in zip(point1, point2):
        dif = val1 - val2
        sum += dif * dif
    return np.sqrt(sum)

def means(data):
    sum = 0
    count = 0
    for elem in data:
        count = count + 1
        sum += elem

    return sum / count

# -------------------------------------------

# ReLU function

def relu(x):
    if x > 0:
        return x 
    
    return 0
    
def relu_deriative(x):
    if x > 0:
        return 1
    
    return 0
        
# Sigmoid function        

def sigmoid(x):
    return 1 / 1 + np.exp(x)

def sigmoid_deriative(x):
    return sigmoid(x) * (1 - sigmoid(x))