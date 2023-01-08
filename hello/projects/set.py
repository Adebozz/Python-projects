groceries = {'cereal', 'milk',  'beer', 'duct tape', 'lotion', 'beer'}
print(groceries)

if 'milk' in groceries:
    print('You already have it boss!')
else:
    print('oh yeah, you need milk')


# Dictionaries and keys

classmates = {'Terry': ' cool but smells',
              'timi': ' fun but dumb', 'Lucy': ' asks too many questions'}


for x, y in classmates.items():
    print(x + y)
