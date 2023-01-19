import heapq

grades = [32,54,78,98,132,66,9, 532]

print(heapq.nlargest(3, grades))
print(heapq.nsmallest(3, grades))

stocks = [
    {'ticker': 'AAPL', 'price': 201},
    {'ticker': 'GOOG', 'price': 800},
    {'ticker': 'R', 'price': 54},
    {'ticker': 'MSFT', 'price': 313},
    {'ticker': 'TESLA', 'price': 268},
    {'ticker': 'ADBOS', 'price': 1000}
]

print(heapq.nsmallest(2, stocks, key=lambda stock:stock['price']))


#finding most frequent items
from collections import Counter
text = "we hope one day become the world leader in free, education resources."\
    "we hope one day become the world leader in free, education resources."\
    "we hope one day become the world leader in free, education resources."\
    "we hope one day become the world leader in free, education resources."\
    "we hope one day become the world leader in free, education resources."\
    "solution the problem."

words = text.split()
counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)

