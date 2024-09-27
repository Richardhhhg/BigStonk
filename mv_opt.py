import pypfopt as opt
import pandas as pd
import yfinance as yf

class mean_var_optimizer:
    """ Class for object that is to perform mean variance optimization

    Attributes:
    - ticker_list: Tickers in portfolio to be analyzed
    - ticker_prices: Prices of all the tickers (1 year)
    - optimal_weights: optimal weights for each ticker
    - expected_returns: CAPM expected returns for the stocks
    - covar_mat: Covariance of the prices of the stonks
    - portfolio_stats: Sharpe Ratio, Volatility, and expected returns of portfolio
    """
    ticker_list: list[str]
    ticker_prices: pd.DataFrame
    # optimal_weights: OrderedDict
    # expected_returns: OrderedDict
    # covar_mat: idk
    # portfolio_stats: tuple


    def __init__(self, ticker_list: list[str]) -> None:
        self.ticker_list = ticker_list
        self.ticker_prices = None
        self.optimal_weights = None
        self.expected_returns = None
        self.covar_mat = None
        self.portfolio_stats = None

    def __str__(self) -> str:
        """ Return Info about the Portfolio

        >>> mvo = mean_var_optimizer(cool_ticker_list)
        >>> mvo.set_ticker_prices()
        >>> mvo.minimize_risk()
        >>> print(mvo)
        ############## Portfolio Weights #################
        BigChonkCorp: 0.25
        SmolDingo: 0.30
        BigPotato: 0.10
        BigDinosaur: 0.35
        ############## Portfolio Stats ###################
        Sharpe Ratio: 3.55
        Beta: 0.01
        alpha: 0.80
        """
        # TODO: Implement This
        res = "############## Portfolio Weights ################# \n"
        res += "\n".join([f"{ticker}: {weight}" for ticker, weight in 
                          self.optimal_weights.items()])
        res += "\n############## Portfolio Stats ###################"
        res += f"""
        Sharpe Ratio: {self.portfolio_stats[2]}
        Expected Annual Return: {self.portfolio_stats[0]}
        Annual Volaility: {self.portfolio_stats[1]}
        """
        return res


    def optimal_portfolio(self) -> None:
        """ Creates the portfolio that Minimizes Risk for a Given Return

        This uses Critical Line Algorithm, Essentially finds the market Portfolio
        Not using any other algorithm that would adjust for risk and return is
        mostly due to the idea that balancing the market portfolio and fixed assets
        is for later
        WARNING: THIS MAY SET WEIGHTS TO 0
        """
        ef = opt.CLA(self.expected_returns, self.covar_mat)
        ef.max_sharpe()
        self.optimal_weights = ef.clean_weights()
        self.portfolio_stats = ef.portfolio_performance(verbose = False)

    def set_ticker_prices(self):
        """ Initializes a lot of stuff outside of the Initializer 
        Purely for asthetic purposes
        """
        ohlc = yf.download(self.ticker_list, period = "1y")
        self.ticker_prices = ohlc["Adj Close"].dropna(how = "all")
        self.expected_returns = opt.expected_returns.capm_return(self.ticker_prices)
        self.covar_mat = opt.risk_models.CovarianceShrinkage(self.ticker_prices).ledoit_wolf()
    