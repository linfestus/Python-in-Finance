#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 01:23:49 2018

@author: bikramjeetsingh
"""

import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import beginning.py 

def compute_daily_returns(df):
    daily_returns = df.copy()
    daily_returns = (df/df.shift(1)) - 1
    daily_returns.ix[0,:] = 0
    return daily_returns



def test_run():
    dates = pd.date_range('2009-01-01','2012-12-31')
    symbols = ['SPY','XOM','GLD']
    df = get_data(symbols,dates)
    plot_data(df)
    
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title = "Daily returns")
    daily_returns.hist(bins = 20)
    
    mean = daily_returns['SPY'].mean()
    print "mean=",mean
    std = daily_returns['SPY'].std()
    print "std=",std
    
    plt.axvline(mean,color='w',linestyle='dashed',linewidth=2)
    plt.axvline(std,color='r',linestyle='dashed',linewidth=2)
    plt.axvline(-std,color='r',linestyle='dashed',linewidth=2)
    plt.show()
    
    print daily_returns.kurtosis()
    
    daily_returns.plot(kind='scatter',x='SPY',y='XOM')
    beta_xom,alpha_xom = np.polyfit(daily_returns['SPY'],daily_returns['XOM'],1)
    plt.plot(daily_returns['SPY'],beta_xom*daily_returns['SPY'] + alpha_xom,'-',color='r')
    plt.show()
    
    daily_returns.plot(kind='scatter',x='SPY',y='GLD')
    beta_gld,alpha_gld = np.polyfit(daily_returns['SPY'],daily_returns['GLD'],1)
    plt.plot(daily_returns['SPY'],beta_gld*daily_returns['SPY'] + alpha_gld,'-',color='r')
    plt.show()
    
    print daily_returns.corr(method="pearson")


    
    
if __name__ == "__main__":
    test_run()
