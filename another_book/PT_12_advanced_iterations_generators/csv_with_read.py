"""чтение csv и вывод в консоль построчно"""

#import os
#os.chdir('/Chapter12_advanced_iterations_generators')

with open('buzzers.csv') as raw_data:
    print(raw_data.read())

"""чтение csv и вывод в виде списков"""

print('\n')

import csv

with open('buzzers.csv') as data:
    for line in csv.reader(data):
        print(line)

print('\n')

"""чтение csv и вывод в словарь"""

with open('buzzers.csv') as data:
    for line in csv.DictReader(data):
        print(line)

print('\n')

import os
os.chdir('C:/Users/lords/PycharmProjects/pythonProject/Chapter12_advanced_iterations_generators')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

import pprint

pprint.pprint(flights)