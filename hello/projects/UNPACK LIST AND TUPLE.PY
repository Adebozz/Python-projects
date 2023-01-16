#unpacking a list into veriables
date, item, price = ['December 23, 2018', 'Shawama', 900]
print(item)


#unpacking variables with diffent sizes
def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([65,76,98,54,21])
