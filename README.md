# Python_DataSets_and_Pandas
 
 <b>This tutorial was developed using Eclipse IDE.</b> <br />
 In order to run Python in Eclipse, go to Help -> Install new Software ... -> and use: 'Pydev p2 Repository - http://pydev.sf.net/updates/'
 
 <b>This tutorial was developed using Python 3.6.1 </b>  <br />
 To Download Python: <br />
 https://www.python.org/downloads/
 
 <b>Installing packages (Pandas) : </b><br />
 Next, go to your terminal or cmd.exe, and type:pip install pandas. Did you get a "pip is not a recognized command" or something similar? No problem, this means pip is not on your PATH. Pip is a program, but your machine doesn't just simply know where it is unless it is on your PATH. You can look up how to add something to your path if you like, but you can always just explicitly give the path to the program you want to execute. On Windows, for example, Python's pip is located in C:/Python34/Scripts/pip. Python34 means Python 3.4. If you have Python 3.6, then you would use Python36, and so on.

Thus, if regular pip install pandas didn't work, then you can do <br />
C:/Python34/Scripts/pip install pandas <br /><br />

Matplotlib library:<br />
C:/Python34/Scripts/pip install matplotlib

 
 -------------------------------------------------------------------------------------------------------------------<br />
 
What is going on everyone, welcome to a Data Analysis with Python and Pandas tutorial series. 
Pandas is a Python module, and Python is the programming language that we're going to use. 
The Pandas module is a high performance, highly efficient, and high level data analysis library.

At its core, it is very much like operating a headless version of a spreadsheet, like Excel. 
Most of the datasets you work with will be what are called dataframes. You may be familiar with 
this term already, it is used across other languages, but, if not, a dataframe is most often just 
like a spreadsheet. Columns and rows, that's all there is to it! From here, we can utilize Pandas 
to perform operations on our data sets at lightning speeds.

Pandas is also compatible with many of the other data analysis libraries, like Scikit-Learn 
for machine learning, Matplotlib for Graphing, NumPy, since it uses NumPy, and more. It's incredibly 
powerful and valuable to know. If you're someone who finds themselves using Excel, or general spreadsheets, 
for various computational tasks, where they might take a minute, or an hour, to run, Pandas is going to 
change your life. I've even seen versions of Machine learning like K-Means clustering being done on Excel. 
That's really cool, but my Python is going to do that for you way faster, which will also allow you to be a 
bit more stringent on parameters, have larger datasets and just plain get more done.

Another bit of good news? You can easily load in, and output out in the xls or xlsx format quickly, so, 
even if your boss wants to view things the old way, they can. Pandas is also compatible with text files, 
csv, hdf files, xml, html, and more with its incredibly powerful IO.
