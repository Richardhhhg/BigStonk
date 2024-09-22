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
    - portfolio_analyst_sent: total analyst sentiment for the portfolio
    - portfolio_personal_sent: total personal sentiment for the portfolio
    - portfolio_net_sent: total net sentiment for the portfolio

    Constants:
    - ANALYST_SENTIMENT_WEIGHT: how much analyst sentiment is weighted in net sentiment
    - PERSONAL_SENTIMENT_WEIGHT: how much personal sentiment is weighted in net sentiment
    - ANALYST_SELF_WEIGHT: weighting for total analyst sentiments depending on period. Each period 
    increases weight exponentially
    """
    ticker_list: list[yf.Ticker]
    analyst_sentiment: dict[yf.Ticker, float]
    personal_sentiment: dict[yf.Ticker, float]
    net_sentiment: dict[yf.Ticker, float]

    ANALYST_SENTIMENT_WEIGHT = 0.4
    PERSONAL_SENTIMENT_WEIGHT = 0.6
    ANALYST_SELF_WEIGHT = 0.5187901

    def __init__(self) -> None:
        self.ticker_list = []
        self.analyst_sentiment = {}
        self.personal_sentiment = {}
        self.net_sentiment = {}
        self.portfolio_analyst_sent = 0.0
        self.portfolio_personal_sent = 0.0
        self.protfolio_net_sent = 0.0

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

    def set_tickers_from_list(self, list) -> None:
        """ Updates ticker list
        """
        self.ticker_list = list
    
    def _set_analyst_scores(self, row, df) -> float:
        """Takes in row of dataframe and the actual dataframe, returns weighted analyst
        sentiment for the given row"""
        ticker_sent = 0.0
        ticker_sent += df.loc[row, 'strongBuy'] + df.loc[row, 'buy'] * 0.5 \
                + df.loc[row, 'hold'] * 0.0 + df.loc[row, 'sell'] * -0.5 \
                + df.loc[row, 'strongSell'] * -1
        ticker_sent *= self.ANALYST_SELF_WEIGHT ** (row + 1)
        return ticker_sent


    def set_analyst_sentiment(self) -> None:
        """Goes through all tickers, returns a value for analyst sentiment of each stonk,
        updates it to self.analyst_sentiment
        """
        # How it works
        # total_sentiment records sum of sentiments of analysts
        # for loop going through each ticker in self.ticker_list
        #   each strong buy adds + 1 to total_sentiment
        #   each buy adds +0.5 to total sentiment
        #   each hold adds +0.0 to total sentiment
        #   each sell adds -0.5 to total sentiment
        #   each strong sell adds -1 to total sentiment
        # Then divides based on total amount of recommendations
        # TODO: Maybe include bootstrap for samples with small amount of recommendations
        total_sentiment = 0.0
        for ticker in self.ticker_list:
            analyst_scores = ticker.get_recommendations()
            ticker_sent = 0.0
            scores_count = 0
            for i in analyst_scores.index:
                analyst_scores['count'] = analyst_scores.sum(axis = 1, numeric_only= True)
                ticker_sent += self._set_analyst_scores(i, analyst_scores)
                score_count += analyst_scores.loc[i, 'count']
            ticker_sent /= scores_count
            self.analyst_sentiment[ticker] = ticker_sent
            total_sentiment += ticker_sent
        total_sentiment /= len(self.ticker_list)
                

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
    
    def create_dataframe(self) -> pd.DataFrame:
        """Turns data stored inside to a pandas dataframe for future use
        """
        df = pd.DataFrame(columns=['Ticker', 'NetSentScore'])
        for ticker, score in self.net_sentiment.items():
            pass
        return df

if __name__ == '__main__':
    import python_ta
    
    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': ['possibly-undefined']
    })



        
            

