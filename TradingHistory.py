import yfinance as yf
import pandas as pd

dataF = yf.download("EURUSD=X", start="2024-02-1", end="2024-02-2", interval='15m')
dataF.iloc[:,:]
dataF.Open.iloc
print(dataF.iloc[:, :])  # Print the entire DataFrame
selected_open = dataF.Open.iloc[:]  # Select Open column and store in a variable