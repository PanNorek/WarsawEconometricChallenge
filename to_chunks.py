import pandas as pd


foo = pd.read_csv("/home/oleh/Рабочий стол/WarsawEconometricChallenge/data/data_merged.csv", iterator=True, chunksize=500_000)


index = 0
for chank in foo:
    index+=1
    chank.to_csv("data/chunks/chank_{0}.csv".format(index))