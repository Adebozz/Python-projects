# flexible numbers of arguments
def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(3,32,54,67,78)
add_numbers(3,43,54,87,97,8765)

# unpacking arguments
def health_calculator(age, apples_ate,cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

frank_data = [27, 20,0]

health_calculator(frank_data[0], frank_data[1], frank_data[2])
health_calculator(*frank_data)