# run using "streamlit run front_end.py"
from fa import fundamental_analysis
from mv_opt import mean_var_optimizer
import yfinance as yf
import streamlit as st
import yfinance as yf

def get_tickers() -> tuple[dict, list]:
    # Initialize or get the dictionary from session state to persist data across reruns
    if 'ticker_dict' not in st.session_state:
        st.session_state.ticker_dict = {}
    if 'ticker_list' not in st.session_state:
        st.session_state.ticker_list = []

    # User input for stock ticker and expected return
    ticker = st.text_input("Enter stock ticker:")
    ticker = ticker.upper()
    expected_return = st.number_input("Enter expected return (%)")

    # Button to save the inputs
    if st.button("Add Stock"):
        if ticker and expected_return:
            # Save the ticker and expected return to the dictionary
            st.session_state.ticker_dict[ticker] = expected_return
            st.session_state.ticker_list.append(ticker)
            st.success(f"Added {ticker} with expected return of {expected_return:.2f}")
        elif ticker:
            st.session_state.ticker_list.append(ticker)
        else:
            st.error("Please input ticker, expected return, and confidence")

    # Display the dictionary of saved stock data
    st.write("Current stock data:")
    st.write(st.session_state.ticker_dict)
    st.write(st.session_state.ticker_list)

    # ending the inputs
    if st.button("KEEL"):
        return st.session_state.ticker_list, st.session_state.ticker_dict


if __name__ == '__main__':
    fa = fundamental_analysis()

    st.title('BIG STONKS GO BONK')
    ticker_list, ticker_dict = get_tickers()
    # ticker_list = get_tickers()

    if ticker_list and ticker_dict:
        # fa.set_tickers_from_list(ticker_list)
        # fa.set_analyst_sentiment()
        # fa.set_personal_sentiment()
        # fa.set_net_sentiment()
        # st.write(fa)
        # ticker_list = fa.get_tickers_as_str()
        mvo = mean_var_optimizer(ticker_list, ticker_dict)
        mvo.set_ticker_prices()
        mvo.optimal_portfolio()
        st.write(mvo)
