# filename: company_performance.py

import pandas as pd

# Read the data from the provided table
data = pd.DataFrame({
    'Date': ['2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-22', '2024-01-23', '2024-01-24', '2024-01-25', '2024-01-26', '2024-01-29', '2024-01-30', '2024-01-31', '2024-02-01', '2024-02-02', '2024-02-05', '2024-02-06', '2024-02-07', '2024-02-08', '2024-02-09', '2024-02-12', '2024-02-13', '2024-02-14', '2024-02-15', '2024-02-16', '2024-02-20', '2024-02-21', '2024-02-22', '2024-02-23', '2024-02-26', '2024-02-27', '2024-02-28', '2024-02-29', '2024-03-01'],
    'META': [346.2900085449219, 344.4700012207031, 347.1199951171875, 351.95001220703125, 358.6600036621094, 357.42999267578125, 370.4700012207031, 369.6700134277344, 374.489990234375, 367.4599914550781, 368.3699951171875, 376.1300048828125, 383.45001220703125, 381.7799987792969, 385.20001220703125, 390.70001220703125, 393.17999267578125, 394.1400146484375, 401.0199890136719, 400.05999755859375, 390.1400146484375, 394.7799987792969, 474.989990234375, 459.4100036621094, 454.7200012207031, 469.5899963378906, 470.0, 468.1099853515625, 468.8999938964844, 460.1199951171875, 473.2799987792969, 484.0299987792969, 473.32000732421875, 471.75, 468.0299987792969, 486.1300048828125, 484.0299987792969, 481.739990234375, 487.04998779296875, 484.0199890136719, 490.1300048828125, 502.29998779296875],
    'TSLA': [248.4199981689453, 238.4499969482422, 237.92999267578125, 237.49000549316406, 240.4499969482422, 234.9600067138672, 233.94000244140625, 227.22000122070312, 218.88999938964844, 219.91000366210938, 215.5500030517578, 211.8800048828125, 212.19000244140625, 208.8000030517578, 209.13999938964844, 207.8300018310547, 182.6300048828125, 183.25, 190.92999267578125, 191.58999633789062, 187.2899932861328, 188.86000061035156, 187.91000366210938, 181.05999755859375, 185.10000610351562, 187.5800018310547, 189.55999755859375, 193.57000732421875, 188.1300048828125, 184.02000427246094, 188.7100067138672, 200.4499969482422, 199.9499969482422, 193.75999450683594, 194.77000427246094, 197.41000366210938, 191.97000122070312, 199.39999389648438, 199.72999572753906, 202.0399932861328, 201.8800048828125, 202.63999938964844]
})

# Extract the closing prices for META and TSLA
meta_closing_prices = data['META']
tesla_closing_prices = data['TSLA']

# Compare the closing prices to determine which company is doing better
if meta_closing_prices.iloc[-1] > tesla_closing_prices.iloc[-1]:
    better_company = 'META'
else:
    better_company = 'TSLA'

# Explain the reason for the better performance
explanation = "The company {} is doing better because it has a higher closing price.".format(better_company)

explanation