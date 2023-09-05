import pandas as pd
import numpy as np
import yfinance as yf

def calculate_annualized_sharpe_ratio(stock_ticker, start_date, end_date, r):
    # Fetch stock data from Yahoo Finance
    ticker_info = yf.Ticker(stock_ticker)
    ticker_info = ticker_info.info
    stock_data = yf.download(stock_ticker, start=start_date, end=end_date)

    # Calculate daily returns
    stock_data['Daily_Return'] = stock_data['Adj Close'].pct_change()

    # Calculate average daily return and standard deviation of daily returns
    avg_daily_return = stock_data['Daily_Return'].mean()
    std_dev_daily_return = stock_data['Daily_Return'].std()

    # Calculate annualized Sharpe ratio
    trading_days_per_year = 252  # Assuming 252 trading days in a year
    annualized_avg_return = avg_daily_return * trading_days_per_year
    annualized_std_dev_return = std_dev_daily_return * np.sqrt(trading_days_per_year)

    risk_free_rate = r  # You can set an appropriate risk-free rate
    return (annualized_avg_return - risk_free_rate) / annualized_std_dev_return, stock_data, ticker_info

if __name__ == "__main__":    
  ticker = "AAPL"
  start_date = "2023-01-01"
  end_date = "2023-08-31"

  sharpe_ratio = calculate_annualized_sharpe_ratio(ticker, start_date, end_date, 0.02)[0]
  stock_data = calculate_annualized_sharpe_ratio(ticker, start_date, end_date, 0.02)[1]
  ticker_info = calculate_annualized_sharpe_ratio(ticker, start_date, end_date, 0.02)[2]
  print(f"Annualized Sharpe Ratio for {ticker}: {sharpe_ratio:.2f}")
  print(stock_data)
  print(ticker_info['longName'])
