# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:39:06 2023

@author: user
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def fn_read_Excel(fileName):
    """
    

    Parameters
    ----------
    fileName : TYPE - string
        DESCRIPTION. - excelfile name + the path

    Returns
    -------
    dataframes one with years as column and one with countries as columns

    """
    df = pd.read_excel(fileName)
    # print(df)
    list_drop_columns=['Country Code','Indicator Name','Indicator Code']
    df.drop(labels='Country Code',axis=1,inplace=True)
    df.drop(labels='Indicator Name',axis=1,inplace=True)
    df.drop(labels='Indicator Code',axis=1,inplace=True)
    # print(df)
    list_Selected_Countries = ['Australia','Japan','United Kingdom',
                                'United Arab Emirates','Canada','United States',
                                'China','Georgia','Brazil','India','Zimbabwe',
                                'Yemen','Sudan']
    # select data for the selected Coutries
    df_SCountries=df.loc[df['Country Name'].isin(list_Selected_Countries)]
    # print(df_SCountries)
    #remove columns with no data
    df_SCountries.dropna(axis=1,how='all', thresh=None, subset=None, \
                          inplace=True)
    df_SCountries.set_index('Country Name')
    
    df_Transpose=df_SCountries.transpose()
    df_Transpose.rename(columns={'Country Name':'Year'},inplace=True)
    # df_Transpose.set_index('Year')
    print(df_Transpose.index)
    return df_SCountries,df_Transpose     

def BarPlot(df,xlbl='',ylbl='',title='',filename=''):
    """   
    Parameters
    ----------
    df : TYPE
        DESCRIPTION.-- plots a grouped bar plot based on df
    Returns
    -------
    None.

    """
    filepath='C:\\Divya UH Academics\\Divya Canvas\\ADS\\Assignments\\April 2nd- Assignment 2\\'
    #lst_years=['1990','1995','2000','2005','2010','2015']
    lst_Rqurd_Colms = ['Country Name','1990','1995','2000','2005','2010','2015']
    df_plot = df[df.columns[df.columns.isin(lst_Rqurd_Colms)]]
   
    df_plot.set_index('Country Name',inplace=True)
    df_plot.replace('United Arab Emirates','UAE',inplace = True,regex = True)
    df_plot.replace('United Kingdom','UK',inplace = True,regex = True)    
    #plot bar graph,
    df_plot.plot(kind='bar',title=title,xlabel=xlbl,ylabel=ylbl)
    # if(xlbl!=''):
    #     plt.xlabel(xlabel=xlbl,fontsize=20)
    # if(ylbl!=''):
    #     plt.ylabel(ylabel=ylbl,fontsize=20)
    # plt.title(title,fontsize=20)
    
    # plt.legend(fontsize='10',loc='upper right')
    # plt.xticks(rotation=90)
    plt.savefig(filepath+filename+".png",bbox_inches = "tight",dpi=100)
    plt.show()

def LinePlot(df,xlbl='',ylbl='',title='',filename=''):
    """   

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    filepath='C:\\Divya UH Academics\\Divya Canvas\\ADS\\Assignments\\April 2nd- Assignment 2\\'
    lst_years=['1990','1995','2000','2005','2010','2015']
    lst_Rqurd_Colms = ['Country Name','1990','1995','2000','2005','2010','2015']
    df_selected = df[df.columns[df.columns.isin(lst_Rqurd_Colms)]]
    df_melt=pd.melt(df_selected,id_vars=['Country Name'],var_name=['Year']
            ,value_name='Value')
    df_plot = df_melt.pivot(index='Year',columns='Country Name',values='Value')
       
    # #plot line graph,
    df_plot.plot(kind='line',title=title,xlabel=xlbl,ylabel=ylbl)
    plt.savefig(filepath+filename+".png",bbox_inches = "tight",dpi=100)
    plt.show()


#read co2 emission data file
filename ='API_EN.ATM.CO2E.KT_DS2_en_excel_v2_5178991.xlsx'
filepath='C:\\Divya UH Academics\\Divya Canvas\\ADS\\Assignments\\April 2nd- Assignment 2\\'
# file=filepath+filename
# df_CO2_CountryWise,df_CO2_Yearwise = fn_read_Excel(file)
# # print(df_CO2_CountryWise)
# # print(df_CO2_Yearwise)
# print(df_CO2_CountryWise.describe())


# BarPlot(df_CO2_CountryWise,'Country Name','CO2 emissions (kt)','Carbon dioxide emissions Summary','co2 bar')

#read Urban population (% of total population)
# filename ='API_SP.URB.TOTL.IN.ZS_DS2_en_excel_v2_5178990.xlsx'
# file=filepath+filename
# df_UrbanPop_CountryWise,df_UrbanPop_Yearwise = fn_read_Excel(file)

# LinePlot(df_UrbanPop_CountryWise,'Year','Urban population (% of total population)','Urban population Summary','UrbanPOp bar')

#Agriculture land
filename ='API_AG.LND.AGRI.ZS_DS2_en_excel_v2_5172055.xlsx'
file=filepath+filename
df_Agri_CountryWise,df_Agri_Yearwise = fn_read_Excel(file)

LinePlot(df_Agri_CountryWise,'Year','Urban population (% of total population)','Urban population Summary','Agri bar')
   
    