from pandas_datareader import data
import datetime as dt

''' This pulls data for Exxon from the Yahoo Finance API '''
ticker = 'XOM'  

start = dt.datetime(2010, 1, 1)
end = dt.datetime(2015, 8, 22)
data1 = data.DataReader(ticker,'yahoo',start,end)

print(data1)
print(data1.head())