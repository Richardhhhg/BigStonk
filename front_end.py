# run using "streamlit run front_end.py"
from fa import fundamental_analysis
from mv_opt import mean_var_optimizer
import yfinance as yf
import streamlit as st
import yfinance as yf

# Initialize session state if it doesn't exist
def get_tickers() -> list[str]:
    if "ticker_list" not in st.session_state:
        st.session_state.ticker_list = []
    if "ticker_list_str" not in st.session_state:
        st.session_state.ticker_list_str = []

    # Get user input
    user_input = st.chat_input('Enter a Ticker or Enter "No" to Stop')

    # Reset button
    if st.button("Reset"):
        st.session_state.ticker_list_str = []
        st.session_state.ticker_list = []
        st.success("Ticker lists have been reset.")

    if user_input:
        user_input = user_input.upper().strip()
        
        if user_input == "NO":
            res = "Tickers to be Analyzed:"
            for ticker in st.session_state.ticker_list_str:
                res += f" {ticker}"
            st.write(res)
            return st.session_state.ticker_list_str
        else:
            try:
                # Append user input to session state lists
                st.session_state.ticker_list_str.append(user_input)
                t = yf.Ticker(user_input)
                st.session_state.ticker_list.append(t)
            except:
                st.write("Enter a valid Ticker NERD")

    # Display current tickers
    portfolio_str = "Current Tickers to be Analyzed:"
    for ticker in st.session_state.ticker_list_str:
        portfolio_str += f" {ticker}"
    st.write(portfolio_str)

if __name__ == '__main__':
    fa = fundamental_analysis()

    st.title('BIG STONKS GO BONK')
    ticker_list = get_tickers()

    if ticker_list:
        # fa.set_tickers_from_list(ticker_list)
        # fa.set_analyst_sentiment()
        # fa.set_personal_sentiment()
        # fa.set_net_sentiment()
        # st.write(fa)
        # ticker_list = fa.get_tickers_as_str()
        mvo = mean_var_optimizer(ticker_list)
        mvo.set_ticker_prices()
        mvo.optimal_portfolio()
        st.write(mvo)
