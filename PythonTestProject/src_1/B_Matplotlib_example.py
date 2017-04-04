''' Pandas works great with other modules, Matplotlib being one of them. ''' 
''' Let's see! Open your terminal or cmd.exe, and do pip install matplotlib. ''' 
''' You should already have got it I am prety sure with your pandas installation, ''' 
''' but we want to make sure. '''

from pandas_datareader import data
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

''' This pulls data for Exxon from the Yahoo Finance API '''
ticker = 'XOM'  

start = dt.datetime(2010, 1, 1)
end = dt.datetime(2015, 8, 22)
data1 = data.DataReader(ticker,'yahoo',start,end)

style.use('fivethirtyeight')

data1['High'].plot()
plt.legend()
plt.show()