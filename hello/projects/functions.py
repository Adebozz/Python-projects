# bitcoin to usd converter
def beef():
    print('Dayum, Functions are cool')


def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)


beef()
bitcoin_to_usd(3.85)
bitcoin_to_usd(1)
bitcoin_to_usd(15)

# Girls that a guy can date age calculator


def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age


ades_list = allowed_dating_age(19)
banji_list = allowed_dating_age(20)
print('Ade can date girls', ades_list, 'or older')
print('banji can date girls', banji_list, 'or older')


# Checking gender
def get_gender(sex='Unknown'):
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    print(sex)

get_gender('m')
get_gender('f')
get_gender()

