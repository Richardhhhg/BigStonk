# TODO:
# 1. Build Thing to get tickers
# 2. Build method to go through tickers and analyze market sentiment via analyst ratings
# 3. Build method to get personal sentiment using other available data (Consult Finance Bros)
import yfinance as yf
import pandas as pd
import numpy as np


class fundamental_analysis:
    """ An object that allows the fundamental analysis of stonks

    Attributes:
    - ticker_list: List of tickers
    - analyst_sentiment: How analysts feel about the tragectory of the stonk, meant to refelct market sentiment
    - personal_sentiment: How our methods feel about tragectory of the stonk
    - net_sentiment: The weighted sentiment score for each stonk
    - ANALYST_SENTIMENT_WEIGHT: how much analyst sentiment is weighted in net sentiment
    - PERSONAL_SENTIMENT_WEIGHT: how much personal sentiment is weighted in net sentiment
    """
    ticker_list: list[yf.Ticker]
    analyst_sentiment: dict[yf.Ticker, float]
    personal_sentiment: dict[yf.Ticker, float]
    net_sentiment: dict[yf.Ticker, float]

    ANALYST_SENTIMENT_WEIGHT = 0.4
    PERSONAL_SENTIMENT_WEIGHT = 0.6

    def __init__(self) -> None:
        self.ticker_list = []
        self.analyst_sentiment = {}
        self.personal_sentiment = {}
        self.net_sentiment = {}

    def __str__(self) -> None:
        """String representation of the fundamental analysis for a given portfolio
        
        Should return each tick wither their analyst, personal, and net sentiment scores
        """
        # TODO: Check whether or not representation correct with the \
        res = "Ticker: Analyst Sentiment/Personal Sentiment/Net Sentiment"
        res += "\n".join([f"{ticker.info['symbol']}: {self.analyst_sentiment[ticker]} \
                          /{self.personal_sentiment[ticker]}/ {self.net_sentiment[ticker]}" \
                          for ticker in self.ticker_list])
        return res

    def get_tickers(self) -> None:
        """ Updates ticker list
        """
        ticker = None
        while ticker.lower() != 'no':
            try:  # assuming input string
                ticker = input("Enter a ticker or Type 'No' to stop")
                t = yf.Ticker(ticker)
                if t not in self.ticker_list:
                    self.ticker_list.append(t)  # Check if typing no breaks it
            except:
                print("Please enter a valid ticker")
    
    def set_analyst_sentiment(self) -> None:
        """Goes through all tickers, returns a value for analyst sentiment of each stonk,
        updates it to self.analyst_sentiment
        """
        # How it works
        # total_sentiment records sum of sentiments of analysts
        # for loop going through each ticker in self.ticker_list
            # each strong buy adds + 1 to total_sentiment
            # each buy adds +0.5 to total sentiment
            # each hold adds +0.0 to total sentiment
            # each sell adds -0.5 to total sentiment
            # each strong sell adds -1 to total sentiment
        # TODO: Decide how many months this should go back, IMPLEMENTT THIS METHOD
        total_sentiment = 0.0
        for ticker in self.ticker_list:
            analyst_scores = ticker.get_recommendations()

    def set_personal_sentiment(self) -> None:
        """Goes through some more relevant information on yfinance 
        and somehow scores that using math
        """
        # TODO: IMPLEMENT THIS
        pass

    def set_net_sentiment(self) -> None:
        """ For each ticker, weights analyst and personal sentiments
        """
        for ticker in self.ticker_list:
            self.net_sentiment[ticker] = fundamental_analysis.ANALYST_SENTIMENT_WEIGHT \
            * self.analyst_sentiment['ticker'] + fundamental_analysis.PERSONAL_SENTIMENT_WEIGHT \
            * self.personal_sentiment['ticker']
        

if __name__ == '__main__':
    import python_ta
    
    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': ['possibly-undefined']
    })



        
            

