from fa import fundamental_analysis

if __name__ == '__main__':
    fa = fundamental_analysis()
    fa.get_tickers()
    fa.set_analyst_sentiment()
    fa.set_personal_sentiment()
    fa.set_net_sentiment()
    print(fa)

    # Some ML and logistic regression stuff here