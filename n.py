import os
import datetime
from random import randint
date = datetime.datetime.now()
for i in range(1, 10065):
    for j in range(0, randint(1, 20)):
     d =f'{str(i)} days ago \n'
     with open('file.txt', 'a') as File:
            File.write(d)
    os.system('git add .')
    os.system(f'git commit -m "commit" ')

#os.system('git add .')
os.system('git push -u origin main')
