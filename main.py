import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator, CCIIndicator
from ta.volatility import BollingerBands

# Define periods
SHORT_RSI_PERIOD = 14
MIDDLE_RSI_PERIOD = 50
LONG_RSI_PERIOD = 100
SHORT_EMA_PERIOD = 12
LONG_EMA_PERIOD = 26

# Load data
df = pd.read_excel("new_veri_15min.xlsx")

# Calculate all indicators once for the entire DataFrame
df['short_rsi'] = RSIIndicator(df['Close'], SHORT_RSI_PERIOD).rsi()
df['middle_rsi'] = RSIIndicator(df['Close'], MIDDLE_RSI_PERIOD).rsi()
df['long_rsi'] = RSIIndicator(df['Close'], LONG_RSI_PERIOD).rsi()

df['short_EMA'] = EMAIndicator(df['Close'], SHORT_EMA_PERIOD).ema_indicator()
df['long_EMA'] = EMAIndicator(df['Close'], LONG_EMA_PERIOD).ema_indicator()

df['CCI'] = CCIIndicator(df['High'], df['Low'], df['Close'], window=50).cci()

bollinger_bands_50 = BollingerBands(df['Close'], window=50)
bollinger_bands_100 = BollingerBands(df['Close'], window=100)
bollinger_bands_200 = BollingerBands(df['Close'], window=200)

df['slow_MA'] = bollinger_bands_50.bollinger_mavg()
df['middle_MA'] = bollinger_bands_100.bollinger_mavg()
df['long_MA'] = bollinger_bands_200.bollinger_mavg()

# Select the relevant columns
result_df = df[[
    'short_rsi', 'middle_rsi', 'long_rsi',
    'short_EMA', 'long_EMA', 'CCI',
    'slow_MA', 'middle_MA', 'long_MA',
    'Open', 'Close', 'High', 'Low', 'Volume'
]]

# Save to Excel
result_df.to_excel("binance_new_15min.xlsx", index=False)
print("done")




