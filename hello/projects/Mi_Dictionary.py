stocks = {
    'GOOG': 520.54,
    'FM': 76.45,
    'YHOO': 39.28,
    'AMZIN': 306.21,
    'AAPL': 99.76,
    'ADEBOS': 1000
}
#sorting by values
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))
print(min(zip(stocks.values(), stocks.keys())))