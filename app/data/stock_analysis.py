# filename: stock_analysis.py
import pandas as pd

# Read the data into a DataFrame
data = pd.read_csv('stock_data.csv')

# Calculate the average stock prices for each company
meta_avg = data['META'].mean()
tsla_avg = data['TSLA'].mean()

# Compare the average stock prices
if meta_avg > tsla_avg:
    print("META is doing better.")
elif meta_avg < tsla_avg:
    print("TSLA is doing better.")
else:
    print("Both companies have the same average stock price.")
