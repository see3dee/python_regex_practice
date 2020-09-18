import re

# match = re.search('iiiig', 'called piiig and iiig')


def find(pat, text):
    match = re.search(pat, text)
    if match:
        print(match)
        print(match.group())
    else:
        print('no match')


find('iig', 'pig')

