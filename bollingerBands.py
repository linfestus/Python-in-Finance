#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 22:56:51 2018

@author: bikramjeetsingh
"""

#Lesson 5

import os
import pandas as pd
#import numpy as np
import matplotlib as plt


def symbol_to_path(symbol, base_dir=""):
    """Return CSV file path for give ticker symbol."""
    return os.path.join(base_dir,"{}.csv".format(str(symbol)))


def get_data(symbols,dates):
    """Read Stock data for given symbols from CSV files"""
    df= pd.DataFrame(index=dates)
    
    if 'SPY' not in symbols:
        symbols.insert(0,'SPY')
        
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol),index_col = "Date",parse_dates = True,
                             usecols=['Date','Adj Close'],na_values = ['nan'])
        df_temp= df_temp.rename(columns = {'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol=='SPY':
            df=df.dropna(subset=["SPY"])
    return df
    
def get_rolling_mean(values,window):
    return pd.rolling_mean(values,window=window)

def get_rolling_std(values,window):
    return pd.rolling_std(values,window=window)

def get_bollinger_bands(rm,rstd):
    upper_band = rm + rstd*2
    lower_band = rm - rstd*2
    return upper_band, lower_band


def test_run():
    dates = pd.date_range('2012-01-01','2012-12-31')
    symbols = ['SP']
    df = get_data(symbols,dates)
    rm_SPY = get_rolling_mean(df['^GSPC1'],window= 20)
    rstd_SPY = get_rolling_std(df['^GSPC1'],window= 20)
    
    upper_band,lower_band = get_bollinger_bands(rm_SPY,rstd_SPY)
    
    
    
    ax = df['SPY'].plot(title="Bollinger Bands", label='SPY')
    rm_SPY.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()
    
    
if __name__ == "__main__":
    test_run()
