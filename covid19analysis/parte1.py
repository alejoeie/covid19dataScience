'''
Created on Feb 17, 2021

@author: Alejandro
'''
import pandas as pd
class procesa_archivos():

    def __init__(self, filePath):
        self.filePath = filePath
        
        
    def obtiene_csv(self):
        self.filePath = pd.read_csv(self.filePath) 
        return self.filePath
    
    def set_dataframe(self):
        self.filePath = pd.DataFrame(self.filePath)

        return self.filePath
    
    def delete_elements(self):

        self.filePath = self.filePath.drop(['Lat', 'Long'], axis = 1)  
        self.filePath = self.filePath.drop(['Province/State'], axis = 1) 
        return self.filePath
    
    def set_new_params(self):

        data = ['Costa Rica', 'Guatemala', 'France', 'Ecuador', 'Brazil', 'Germany']   
        column_name = 'Country/Region'
        self.filePath = self.set_init_index(column_name)
        self.filePath = self.filePath.groupby(self.filePath.index).agg(lambda m: sum(m))
        self.filePath  = self.filePath.loc[data]
        return self.filePath

    def set_init_index(self, column_name):

        self.filePath = self.filePath.set_index(column_name)
        return self.filePath
        
    
    def setList(self):
        '''Gets a column and gets its date amount'''

        counter = 0 
        linear = []
        for i in range(self.filePath.shape[1]-1):
            counter += i
            linear.append(i)
        return linear


    def get_dataframe(self):
        self.filePath = self.obtiene_csv()
        self.filePath  = self.set_dataframe()
        self.filePath  = self.delete_elements()
        self.filePath  = self.set_new_params()
        self.filePath = self.filePath.T
        return self.filePath 



# confirmed = procesa_archivos('../datos/time_series_covid19_confirmed_global.csv')
# print(confirmed.get_dataframe())
# print(confirmed.get_dataframe())