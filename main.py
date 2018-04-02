import DataAux as dt

path = r"C:\Users\marce\Documents\GitHub\DataVisualization\data\\"
file = "train.csv"
source = path + file

data, indexName = dt.loadData(source, header=True)
X, Y = dt.SeparateData(data)
