import csv
import os
# import numpy as np
# import pandas as pd
# import sys
import math


def loadData(str, header=False, sep=','):
    f = open(str, 'r')
    data = []
    IndexName = []
    _, file_extension = os.path.splitext(str)
    if (file_extension == ".csv"):
        reader = csv.reader(f, delimiter=sep)
        if header:
            IndexName.append(next(reader))
        for row in reader:
            data.append(row)
    return data, IndexName


def SeparateData(data):
    X = []
    Y = []
    for row in data:
        X.append(row[0:-1])
        Y.append(row[-1])
    return X, Y


def SeparateDataTrainTest(data, pcSep=0.7):
    xTrain = []
    yTrain = []
    xTest = []
    yTest = []
    sep = math.ceil(pcSep*len(data))
    for row in data[0:sep]:
        xTrain.append(row[0:-1])
        yTrain.append(row[-1])
    for row in data[sep:]:
        xTest.append(row[0:-1])
        yTest.append(row[-1])
    return xTrain, yTrain, xTest, yTest
