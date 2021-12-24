import re
import json
import random

name = str(input('whats your name? :'))

patern = '^[A-Z][a-z]+\s[A-Z][a-z]+$'

if re.namesearch(name, patern):
    full_name = name.lower()
    re.sub('\s', '_', full_name)
else:
    print('the mistake')
    
ID = random.randint(1000, 9999)

