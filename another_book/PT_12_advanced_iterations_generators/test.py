data = [1,2,3,4,5,6,7,8]
evens = []
for num in data:
    if not num % 2:
        evens.append(num)
print(evens)

data_generator = [num for num in data if not num % 2]
print(evens)


data = [1,'one',2,'two',3,'three',4,'four']
words = []
for num in data:
    if isinstance(num, str):
        words.append(num)
print(words)

dgen = [num for num in data if isinstance(num, str)]
print(words)

data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
    title.append(word.title())
print(title)

ddgen = [word.title() for word in data]
print(title)

vowels = {'a','e','i','o','u'}
message = "Don't forget to pack your towel."

found = set()
for v in vowels:
    if v in message:
        found.add(v)

found = {v for v in vowels if v in message}

import requests

urls = ('https://google.com', 'https://vk.com', 'https://twitter.com')

for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '->', resp.status_code, '->', resp.url)


from url_utils import gen_from_urls

for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, status, url)