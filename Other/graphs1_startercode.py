# -*- coding: utf-8 -*-
"""
Created on Tue May 11 01:55:54 2021

@author: Administrator
"""

# working from starter code

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from statsmodels.nonparametric.smoothers_lowess import lowess
from pandas.plotting import autocorrelation_plot
import numpy as np

def monthlyweekly(df):
    # df.Date.duplicated().sum() = 0
    df = df[(df.index > '2020-01-01') & (df.index <= '2021-05-01')]
    df_monthly = df.Rate.resample('M').mean()
    df_weekly = df.Rate.resample('W').mean().reset_index()
    
    df_weekly.plot.line('Date', 'Rate')
    df_monthly.plot.line('Date', 'Rate')
    
    
def lowess(df):
    span = 0.025  # What happens when you change this?

    lowess_025 = lowess(df['Rate'], 
                    df.index)

def decomposition(df):
    import statsmodels.api as sm
    df = df[(df.index > '2020-01-01') & (df.index <= '2021-05-01')]
    df_monthly = df.Rate.resample('M').mean()

    print(df.head())
    
    sm.graphics.tsa.plot_acf(df_monthly, lags=10);

def seasonality(df):    
    df['Rate365'] = df['Rate'].shift(365)
    df['Ratediff365'] = df['Rate'] - df['Rate365']

    df['Rate31'] = df['Rate'].shift(31)
    df['Ratediff31'] = df['Rate'] - df['Rate31']
    
    df = df[(df.index > '2017-01-01') & (df.index <= '2021-05-01')]
    df.reset_index(inplace=True)
    print(df.head())
    plt.plot( 'Date', 'Rate', data=df, marker='', color='blue', linewidth=1)
    plt.plot( 'Date', 'Rate31', data=df, marker='', color='green', linewidth=1,linestyle='dashed')
    plt.plot( 'Date', 'Rate365', data=df, marker='', color='olive', linewidth=1, linestyle='dashed')
    plt.xlabel("Date")    
    plt.ylabel("EUR/USD Exchange Rate")
    plt.legend()
    
def correlationchart(df):    
    df['Rate365'] = df['Rate'].shift(365)
    df['Ratediff365'] = df['Rate'] - df['Rate365']

    df['Rate31'] = df['Rate'].shift(31)
    df['Ratediff31'] = df['Rate'] - df['Rate31']
    
    df = df[(df.index > '2017-01-01') & (df.index <= '2021-05-01')]
    df.reset_index(inplace=True)
    
    corr = df.corr()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = np.arange(0,len(df.columns),1)
    ax.set_xticks(ticks)
    plt.xticks(rotation=90)
    ax.set_yticks(ticks)
    ax.set_xticklabels(df.columns)
    ax.set_yticklabels(df.columns)
    plt.show()
    print(df.corr(method ='pearson'))

def arima(df):
    df = df[(df.index > '2017-01-01') & (df.index <= '2021-05-01')] 
    autocorrelation_plot(df)

if __name__ == "__main__":
    forex_df = pd.read_csv('forexscrape.csv')
    forex_df = forex_df.iloc[: , 1:]
    forex_df['Date']= pd.to_datetime(forex_df['Date'])
    forex_df = forex_df.set_index('Date')
    forex_df.sort_index(inplace=True)
    #monthlyweekly(forex_df)
    #lowess(forex_df) #this doesnt work
    decomposition(forex_df) #i don't know how to interpret this
    #seasonality(forex_df)
    #arima(forex_df)
    #correlationchart(forex_df)