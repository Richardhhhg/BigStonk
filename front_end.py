import streamlit as st
# run using "streamlit run front_end.py"
from fa import fundamental_analysis
import yfinance as yf

import streamlit as st
import yfinance as yf

def get_tickers() -> list[yf.Ticker]:
    """ Gets input for list of tickers
    """
    # Initialize session state variables if not already done
    if "ticker_list" not in st.session_state:
        st.session_state.ticker_list = []
    if "ticker_list_str" not in st.session_state:
        st.session_state.ticker_list_str = []

    # Get user input
    user_input = st.chat_input('Enter a Ticker or Enter "No" to Stop')

    if user_input:
        user_input = user_input.upper()

        st.write(user_input)
        if user_input == "NO":
            res = "Tickers to be Analyzed:"
            for ticker in st.session_state.ticker_list_str:
                res += f" {ticker}"
            st.write(res)
            return st.session_state.ticker_list
        
        try:
            # Append user input to session state lists
            st.session_state.ticker_list_str.append(user_input)
            t = yf.Ticker(user_input)
            st.session_state.ticker_list.append(t)
        except ValueError: # yfinance does not check whether or not ticker exists right away
            st.write("Enter a valid Ticker NERD")
    

if __name__ == '__main__':
    fa = fundamental_analysis()

    st.title('BIG STONKS GO BONK')
    ticker_list = get_tickers()

    if ticker_list:
        fa.set_tickers_from_list(ticker_list)
        fa.set_analyst_sentiment()
        fa.set_personal_sentiment()
        fa.set_net_sentiment()
        st.write(fa)
