'''
Created on Feb 17, 2021

@author: Alejandro 
'''

from numpy.lib.shape_base import _split_dispatcher, split
from parte1 import procesa_archivos
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
class analisis(procesa_archivos):
    def __init__(self, filePath, countries):
        self.countries = countries
        self.filePath = filePath


    def getter(self):
       self.filePath = self.get_dataframe()
       return self.filePath

    def split_df(self):
        self.filePath = self.filePath.diff()
        self.filePath = self.filePath.drop(index='1/22/20')
        months = pd.DatetimeIndex(self.filePath.index).month
        tdf = self.filePath.assign(month_x = months)
        annos = pd.DatetimeIndex(self.filePath.index).year
        tdf = tdf.assign(year_x = annos)
        covid = tdf.groupby(['month_x', 'year_x']).sum()
        covid1 = tdf.groupby(['month_x', 'year_x']).median()
        covidstd = tdf.groupby(['month_x', 'year_x']).std()
        covidquart = tdf.groupby(['month_x', 'year_x']).quantile(0.25)
        covidq1 = tdf.groupby(['month_x', 'year_x']).quantile(0.50)
        covidq2 = tdf.groupby(['month_x', 'year_x']).quantile(0.75)
        heat = sns.heatmap(covid.corr(),annot=True)
        plt.show()
        plt.close()
        
        return tdf, covid, covid1, covidstd, covidquart, covidq1, covidq2, heat


    def get_file(self):
        return self.filePath

        
countries = ['Costa Rica', 'Guatemala', 'Ecuador', 'Brazil', 'Germany']
confirmed = analisis('../datos/time_series_covid19_confirmed_global.csv' , countries )
print(confirmed.getter())
tdf1, c1, c2, c3, c4, c5, c6, h = confirmed.split_df()
months = pd.DatetimeIndex(tdf1.index).month
tdf1 = tdf1.assign(month_x = months)
annos = pd.DatetimeIndex(tdf1.index).year
tdf1 = tdf1.assign(year_x = annos)
tdf1 = tdf1.set_index(['month_x','year_x'])
covid = tdf1.groupby(['month_x', 'year_x']).sum()
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(h)
box = covid.boxplot(column=['Costa Rica', 'Guatemala', 'France' , 'Ecuador', 'Brazil', 'Germany'])     
plt.show()
plt.close()