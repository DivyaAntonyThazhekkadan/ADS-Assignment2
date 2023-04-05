# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:39:06 2023

@author: user
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors
from scipy import stats

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
    # print(df_Transpose.index)
    return df_SCountries,df_Transpose     

def BarPlot(df,xlbl='',ylbl='',title='',filename='',color='vlag'):
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
    # Create a diverging palette-coolwarm,Spectral,icefire
    # , 1 vlag,YlOrBr,Blues,ch:s=-.2,r=.6,magma,"hls", 8
    # ,viridis,mako,Paired,
    palette = sns.color_palette(color)#sns.diverging_palette(220, 10, n=7,center='light')

    # Convert the seaborn palette to a matplotlib colormap
    cmap = mcolors.LinearSegmentedColormap.from_list('my_colormap', palette)
    #plot bar graph,
    df_plot.plot(kind='bar',title=title,xlabel=xlbl,ylabel=ylbl,colormap=cmap,width=0.8)
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
    ax=df_plot.plot(kind='line',title=title,xlabel=xlbl,ylabel=ylbl)
    ax.legend(bbox_to_anchor=(1.5,1),loc='upper right')
    plt.savefig(filepath+filename+".png",bbox_inches = "tight",dpi=100)
    plt.show()

def statsDescribe(df,mode =0):
    """
    

    Parameters
    ----------
    df : TYPE -dataframe, mode = 0-countrywise ,1- yearwise
        DESCRIPTION.

    Returns ;
    -------
    None.

    """
    lst_Rqurd_Colms = ['Country Name','1990','1995','2000','2005','2010','2015']
    if mode == 0 :
        lst_Rqurd_Colms = ['Country Name','1990','1995','2000','2005','2010','2015']
    else:
        lst_Rqurd_Colms = ['1990','1995','2000','2005','2010','2015']
        
    df_stats=df[df.columns[df.columns.isin(lst_Rqurd_Colms)]]
    df_stats['Country Name'] = pd.to_numeric(df['Country Name'], errors='coerce')
    
    print("Describe")
    print(stats.describe(df_stats))
    print("Median ")
    print(df_stats.median())
    print("Mode ")
    print(df_stats.mode())
    
    return 
# def PiPlot(country='Country Name'):
#     """   

#     Parameters
#     ----------
#     'Country Name' : TYPE
#         DESCRIPTION.

#     Returns
#     -------
#     None.

#     """
#     lst_indicators=['Population growth (annual %)'
#                     ,'Urban population (% of total population)'
#                     ,'CO2 emissions (kt)'
#                     ,'Energy use (kg of oil equivalent per capita)'
#                     ,'Forest area (% of land area)'
#                     ,'Agricultural land (% of land area)'
#                     ,'Droughts, floods, extreme temperatures (% of population, average 1990-2009)'
#                     ,'Total greenhouse gas emissions (% change from 1990)']
    
#     filename ='API_All.xlsx'
#     filepath='C:\\Divya UH Academics\\Divya Canvas\\ADS\\Assignments\\April 2nd- Assignment 2\\'
#     file=filepath+filename
#     df = pd.read_excel(file)
#     df_country=df.loc[df['Country Name']==country]
#     df_selected=df_country.loc[df['Indicator Name'].isin(lst_indicators)]
#     # print(df_selected)
#     df_selected.drop(labels='Country Code',axis=1,inplace=True)
#     # df_selected.drop(labels='Indicator Name',axis=1,inplace=True)
#     # df_selected.drop(labels='Indicator Code',axis=1,inplace=True)
    
#     lst_Rqurd_Colms = ['Indicator Name','1990','1995','2000','2005','2010','2015']#,
#     df_rqrd = df_selected[df_selected.columns[df_selected.columns.isin(lst_Rqurd_Colms)]]
#     # df_melt=pd.melt(df_rqrd,id_vars=['Indicator Name'],var_name=['Year']
#     #         ,value_name='Value')
#     # df_melt.drop(labels='Year',axis=1,inplace=True)
   
#     df_t=df_rqrd.transpose()
#     cor=df_t.corr()
#     sns.heatmap(data=cor,annot=True)
    
#     return

def HeatMap(filename,country):
    """
    

    Parameters
    ----------
    filename : TYPE
        DESCRIPTION.
    country : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    filepath='C:\\Divya UH Academics\\Divya Canvas\\ADS\\Assignments\\April 2nd- Assignment 2\\'
    file = filepath+filename
    df=pd.read_excel(file)
    pear_corr = df.corr(method='pearson')
    fig,ax = plt.subplots(figsize=(6,6))
    im=ax.imshow(pear_corr,interpolation='nearest')
    fig.colorbar(im,orientation='vertical',fraction = 0.05)
    ax.set_xticks([0,1,2,3,4,5,6])
    ax.set_xticklabels(df.columns,rotation=90,fontsize=15)
    ax.set_yticks([0,1,2,3,4,5,6])
    ax.set_yticklabels(df.columns,rotation=0,fontsize=15)
    
    for i in range(len(df.columns)):
        for j in range(len(df.columns)):
            text = ax.text(j,i,round(pear_corr.to_numpy()[i,j],2)
                           ,ha="center",va="center",color="green")
    plt.savefig(filepath+' '+country+" heatmap.png",bbox_inches = "tight")
    plt.show()       
    
    return
    
#read co2 emission data file
filename ='API_EN.ATM.CO2E.KT_DS2_en_excel_v2_5178991.xlsx'
filepath='C:\\Divya UH Academics\\Divya Canvas\\ADS\\Assignments\\April 2nd- Assignment 2\\'
file=filepath+filename
df_CO2_CountryWise,df_CO2_Yearwise = fn_read_Excel(file)
# print(df_CO2_CountryWise)
# print(df_CO2_Yearwise)
print("Describe CO2 \n")
print(df_CO2_CountryWise.describe())


print("Stastical properties of CO2 emission ")
statsDescribe(df_CO2_CountryWise)

BarPlot(df_CO2_CountryWise,'Country Name','CO2 emissions (kt)'
        ,'Carbon dioxide emissions Summary','co2 bar'
        ,color='coolwarm')


# read Energy use (kg of oil equivalent per capita
filename ='API_EG.USE.PCAP.KG.OE_DS2_en_excel_v2_5180803.xlsx'
file=filepath+filename
df_EnergyUse_CountryWise,df_EnergyUse_Yearwise = fn_read_Excel(file)


BarPlot(df_EnergyUse_CountryWise,'Country Name'
        ,'Energy use (kg of oil equivalent per capita)'
        ,'Energy use (kg of oil equivalent per capita) Summary'
        ,'Energy Usage bar'
        ,color='Spectral')

print("Stastical properties of Energy Use ")
statsDescribe(df_EnergyUse_CountryWise)


#read Urban population (% of total population)
filename ='API_SP.URB.TOTL.IN.ZS_DS2_en_excel_v2_5178990.xlsx'
file=filepath+filename
df_UrbanPop_CountryWise,df_UrbanPop_Yearwise = fn_read_Excel(file)

LinePlot(df_UrbanPop_CountryWise,'Year','Urban population (% of total population)'
        ,'Urban population Summary','UrbanPOp line')


print("Describe Urban population \n")
print(df_UrbanPop_CountryWise.describe())


print("Stastical properties of Urban population ")
statsDescribe(df_UrbanPop_CountryWise)

#Agriculture land
filename ='API_AG.LND.AGRI.ZS_DS2_en_excel_v2_5172055.xlsx'
file=filepath+filename
df_Agri_CountryWise,df_Agri_Yearwise = fn_read_Excel(file)

LinePlot(df_Agri_CountryWise,'Year','Agricultural land (% of land area)'
         ,'Agricultural land Summary','Agri line')


print("Describe Agricultural land \n")
print(df_Agri_CountryWise.describe())


print("Stastical properties of Agricultural land ")
statsDescribe(df_Agri_CountryWise)

#heatmap of India
# PiPlot('India')
HeatMap(filename = 'India Heatmap Indicators.xlsx', country= 'India')

    