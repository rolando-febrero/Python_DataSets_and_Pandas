
''' In this Data analysis with Python and Pandas tutorial, 
we're going to clear some of the Pandas basics. Data prior to 
being loaded into a Pandas Dataframe can take multiple forms, 
but generally it needs to be a dataset that can form to rows and columns. 
So maybe a dictionary like this:

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]} '''

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

''' We can turn this dictionary to a dataframe by doing the following: '''
web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)

print(' --> Now what can we do? As seen before, you can call for a quick initial snippit by doing:\n')
print(df.head())
print('\n')

print('------------------------------------------------------------------------------------------------------------------\n')

print(' --> You may also want the last few lines instead. For this, you can do something like:\n')
print(df.tail())
print('\n')

print('------------------------------------------------------------------------------------------------------------------\n')

print(' --> Finally, you can also put the number of the head or tail you want, like so:\n')
print(df.tail(2))
print('\n')



print('------------------------------------------------------------------------------------------------------------------\n')
text ="""       You can see here how there are these numbers on the left, 0,1,2,3,4,5 and so on, like line numbers. 
       These numbers are actually your "index." The index of a dataframe is what the data is related by, 
       ordered by...etc. Generally, it is going to be the variable that connects all of the data. 
       In this case, we never defined anything for this purpose, and it would be a challenge for Pandas 
       to just somehow "know" what that variable was. Thus, when you do not define an index, 
       Pandas will just make one for you like this. Looking at the data set right now, 
       do you see a column that connects the others?

       The "Day" column fits that bill! Generally, if you have any dated data, the date will be the 
       "index" as this is how all of the data points relate. There are many ways to identify the index, 
       change the index, and so on. We'll cover a couple here. First, on any existing dataframe, 
       we can set a new index like so: """

print(text + '\n')

df.set_index('Day', inplace=True)
print(df.head())
print('\n')

print('------------------------------------------------------------------------------------------------------------------\n')

print(' --> You can also reference parts of the dataframe like an object, so long as there arent any spaces, so you can do something like this:\n')
print(df.Visitors)
print('\n')

print('------------------------------------------------------------------------------------------------------------------\n')

print('So we can plot a single column like this:')
df['Visitors'].plot()
plt.title('Visitors')
plt.show()
print('\n')

print('------------------------------------------------------------------------------------------------------------------\n')

print('We can also plot the entire dataframe. So long as the data is normalized or on the same scale, this will work just fine. Heres an example:')
df.plot()
plt.title('Entire dataframe')
plt.show()
print('\n')