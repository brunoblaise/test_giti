import os
from random import randint

for i in range(1, 10065):
    for j in range(0, randint(1, 20)):
     d = str(i) + ' days ago'
     with open('file.txt', 'a') as File:
            File.write(d)
    os.system('git commit -am "commit" ')

os.system('git push -u origin main')
