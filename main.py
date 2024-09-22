from fa import fundamental_analysis
import yfinance as yf

def get_tickers() -> list[yf.Ticker]:
    """ Gets input for list of tickers
    """
    ticker_list = []
    ticker = None
    while ticker.lower() != 'no':
        try:  # assuming input string
            ticker = input("Enter a ticker or Type 'No' to stop")
            t = yf.Ticker(ticker)
            if t not in ticker_list:
                ticker_list.append(t)  # Check if typing no breaks it
        except:
            print("Please enter a valid ticker")
    return ticker_list

if __name__ == '__main__':
    fa = fundamental_analysis()
    ticker_list = get_tickers()
    fa.set_tickers_from_list(ticker_list)
    fa.set_analyst_sentiment()
    fa.set_personal_sentiment()
    fa.set_net_sentiment()
    print(fa)

    # Some ML and logistic regression stuff here
