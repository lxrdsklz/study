fruits = {}

fruits['apples'] = 10
# print(fruits)

# if 'apples' in fruits:
#     print('True')

#fruits['bananas'] = 1

if 'bananas' in fruits:
    fruits['bananas'] += 1
else:
    fruits['bananas'] = 1

print(fruits)

# if 'pears' not in fruits:
#     fruits['pears'] = 0
#
# print(fruits)

fruits.setdefault('pears', 0)
fruits['pears'] += 1
print(fruits)