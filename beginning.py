# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

def plot_adj_close(symbol):
    df = pd.read_csv("{}.csv".format(symbol))
    print "Adj Close"
    df['Adj Close'].plot()
    plt.show()

def get_mean_volume(symbol):
    
    df = pd.read_csv("{}.csv".format(symbol))
    
    return df['Volume'].mean() 

def get_max_close(symbol):
    
    df = pd.read_csv("{}.csv".format(symbol))
    
    print df['Close'].max() 

def test_run():
    for symbol in ['AAPL','IBM']:
        print "Mean Volume"
        print symbol,get_mean_volume(symbol)
        print "Max Close"
        print symbol, get_max_close(symbol)
        plot_adj_close(symbol)
        
        

if __name__ == "__main__":
    test_run()
