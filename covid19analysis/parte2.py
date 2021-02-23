'''
Created on Feb 17, 2021

@author: Alejandro 
'''

from parte1 import procesa_archivos
import numpy as np
import pandas as pd
class analisis(procesa_archivos):
    def __init__(self, filePath, countries):
        self.countries = countries
        self.filePath = filePath


    def getter(self):
       self.filePath = self.get_dataframe()
       return self.filePath

    def statistics_std(self):
        l = []
        covid = self.filePath
        print(covid.shape[1])
        l.append(np.mean(covid.loc[:,'Germany']))
        return l

    def print_file(self):
        print(self.filePath)
        
    def split_df(self):
        months = pd.DatetimeIndex(self.filePath.index).month
        tdf = self.filePath.assign(month_x = months)
        annos = pd.DatetimeIndex(self.filePath.index).year
        tdf = tdf.assign(year_x = annos)
        norm = tdf.groupby(['month_x', 'year_x']).sum()
        return norm


      

            
       

        # return covid
        
        
        


countries = ['Costa Rica', 'Guatemala', 'Ecuador', 'Brazil', 'Germany']
confirmed = analisis('../datos/time_series_covid19_confirmed_global.csv' , countries )
print(confirmed.getter())
confirmed.print_file()
print(confirmed.statistics_std())
# print(prom)
# print(quartil)
print(confirmed.split_df())