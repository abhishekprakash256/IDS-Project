"""
The file to get the data set and do the analysis on the dataset  
to visualize the dataset and understand 
"""

#imports 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt



#file path 
filePath = "../dataSet/archive2/CovidData.csv"

#read the dataset
df = pd.read_csv(filePath)


#get the dataset info

class Datahandler:
	def printInfo(self,data):
		"""
		The function to print the dataset info
		Args:
			data : the pandas dataset frame

		"""

		#data informations
		head = data.head()
		info = data.info()
		tail = data.tail()
		describe = data.describe()
		unique = data.nunique()
		issum = data.isna().sum()
		#groupby = data.groupby('Column').agg(['mean', 'median', 'std'])

		print("The head of the dataset")
		print(head)

		print("The info of the dataset")
		print(info)

		print("The tail of the dataset")
		print(tail)

		print("The descripotion of the dataset")
		print(describe)

		print("The unique values in the dataset")
		print(unique)

		print("The null sum in the datset")
		print(issum)
		#print(groupby)

	def visualization(self,data):
		"""
		The function to visualize the data set 
		Args:
			data : the pandas dataframe 
		"""

		#the data visulaization
		pass



if __name__== "__main__":
	handler = Datahandler()
	information = handler.printInfo(df)
	visuals = handler.visualization(df)
	print(information)
	print(visuals)