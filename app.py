import streamlit as st
import pandas as pd
import sharpecal
import datetime

title = st.text_input('input ticker', 'AAPL')
start = st.date_input('input start date', datetime.date(2023, 1, 1))
end = st.date_input('input end date', datetime.date(2023, 8, 31))
risk_free_rate = st.number_input('input risk free rate', 0.02)
try:
  sharperatio, stock_data, ticker_info = sharpecal.calculate_annualized_sharpe_ratio(title, start, end, risk_free_rate)
  st.title(ticker_info['longName'])

  st.header(f"Annualized Sharpe Ratio for {title}: {sharperatio:.2f} :sunglasses:")
  st.subheader(f'Comparing {title} buy and hold performance with SPY:')
  SPYsharperatio, SPYstock_data, SPYticker_info = sharpecal.calculate_annualized_sharpe_ratio('SPY', start, end, risk_free_rate)
  init_investment = 100
  SPYstock_data['Wealth'] = init_investment * (1 + SPYstock_data['Daily_Return']).cumprod()
  stock_data['Wealth'] = init_investment * (1 + stock_data['Daily_Return']).cumprod()


  comparedf = pd.DataFrame({'SPY': SPYstock_data['Wealth'], title: stock_data['Wealth']})
  st.line_chart(comparedf, use_container_width=True)
except:
  st.header('Please input a valid ticker')