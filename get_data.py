# This code fetch stock data using yfinance, process it, and save it to CSV files
# Here you will have to delete second header from csv file manually

import yfinance as yf
import pandas as pd

# Tickers list
ticker_list = ['RELIANCE.NS', 'HDFCBANK.NS', 'TCS.NS']

# Define date range
start_date = '2019-10-25'
end_date = '2024-10-25'

# Fetching and saving data
for ticker in ticker_list:
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Reset index to make 'Date' a column
    data.reset_index(inplace=True)

    # Convert 'Date' column (remove timezone)
    data['Date'] = data['Date'].dt.tz_localize(None)
    
    # Reorder columns as desired
    data = data[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
    
    # Save to CSV
    data.to_csv(f'./stockdatas/{ticker}.csv', index=False)
    print(f"Data for {ticker} saved in desired format.")

# read and display the first few rows of saved data
for ticker in ticker_list:
    df = pd.read_csv(f'./stockdatas/{ticker}.csv')
    print(df.head())
