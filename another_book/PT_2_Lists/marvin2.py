# # преобразует строку в список и выводит символы срезами из списка с табуляцией \t
#
# paranoid_android = 'Marvin, the Paranoid Android'
# letters = list(paranoid_android)
#
# for char in letters[:6]:
#     print('\t', char)
# for char in letters[-7:]:
#     print('\t' * 2, char)
# for char in letters[12:20]:
#     print('\t' * 3, char)


string = [{'id':0,'role':'hueta'},{'id':1,'role':'zalupa'}]
letters = list(string)

for char in letters[0:1]:
    print('\t', char)
for char in letters[1:]:
    print('\t' * 2, char)