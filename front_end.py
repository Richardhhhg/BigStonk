# run using "streamlit run front_end.py"
from fa import fundamental_analysis
from mv_opt import mean_var_optimizer
import yfinance as yf
import streamlit as st
import yfinance as yf

def get_tickers() -> tuple[dict, list, str]:
    # Initialize or get the dictionary from session state to persist data across reruns
    if 'ticker_dict' not in st.session_state:
        st.session_state.ticker_dict = {}
    if 'ticker_list' not in st.session_state:
        st.session_state.ticker_list = []
    if 'status' not in st.session_state:
        st.session_state.status = "OFF"

    # User input for stock ticker and expected return
    ticker = st.text_input("Enter stock ticker:")
    ticker = ticker.upper()
    expected_return = st.number_input("Enter expected return")

    # Button to save the inputs
    if st.button("Add Stock"):
        if ticker and expected_return:
            # Save the ticker and expected return to the dictionary
            st.session_state.ticker_dict[ticker] = expected_return
            st.session_state.ticker_list.append(ticker)
            st.success(f"Added {ticker} with expected return of {expected_return:.2f}")
        elif ticker:
            st.session_state.ticker_list.append(ticker)
            st.success(f"Added {ticker}!")
        else:
            st.error("Please input ticker, expected return, and confidence")

    # Display the dictionary of saved stock data
    st.write("Current Stocks and Expected Returns:")
    st.write(st.session_state.ticker_dict)
    st.write("All Stonks")
    st.write(st.session_state.ticker_list)

    # ending the inputs
    if st.button("KEEL"):
        st.session_state.status = "ON"

    return st.session_state.ticker_list, st.session_state.ticker_dict, st.session_state.status

if __name__ == '__main__':
    # fa = fundamental_analysis()

    st.title('Mean Variance Optimization!')
    ticker_list, ticker_dict, status = get_tickers()

    if status == "ON":
        mvo = mean_var_optimizer(ticker_list, ticker_dict)
        mvo.set_ticker_prices()
        mvo.optimal_portfolio()
        st.write(mvo)