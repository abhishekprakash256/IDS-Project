"""
The file to get the data set and do the analysis on the dataset  
to visualize the dataset and understand 
"""

#imports 
import pandas as pd 
import numpy as np



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

		print(head)
		print(info)




if __name__== "__main__":
	handler = Datahandler()
	res = handler.printInfo(df)
	print(res)