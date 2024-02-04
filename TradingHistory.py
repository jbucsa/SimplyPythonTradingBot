#Run pip yfinance
# Import from Yahoo Finance
import yfinance as yf

#Run pip pandas
import pandas as pd

dataF = yf.download("EURUSD=X", start="2024-02-1", end="2024-02-05", interval='15m')
dataF.iloc[:,:]
dataF.Open.iloc

# Print the entire DataFrame
print(dataF.iloc[:,:])

# Select Open column and store in a variable
selected_open = dataF.Open.iloc[:] 