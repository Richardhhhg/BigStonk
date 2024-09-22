# Purpose of this file is just to generate a train.csv file for the machine learning model to train on
# meant to be run once and never again
# Purpose of this file is just to generate a train.csv file for the machine learning model to train on
# meant to be run once and never again
import yfinance as yf
import pandas as pd
from fa import fundamental_analysis

if __name__ == '__main__':
    fa = fundamental_analysis()
    ticker_list = ['INSERT LARGE ASS LIST OF TICKERS HERE']
    fa.set_tickers_from_list(ticker_list)
    fa.set_analyst_sentiment()
    fa.set_personal_sentiment()
    fa.set_net_sentiment()