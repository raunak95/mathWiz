import time, glob, os
import pandas as pd
from random import randint

x = int(input('Time in seconds: '))

nTotal = 0
nCorrect = 0
incorrect = []
st = time.time()

while((time.time() - st) < x):
    a = randint(15, 40)
    b = randint(15, 40)
    c = a*b
    cInput = int(input('{} x {} = '.format(a, b)))
    if cInput == c:
        nCorrect += 1
    else:
        incorrect.append({'a': a, 'b': b, 'cIncorrect': cInput, 'cCorrect': c})
    nTotal += 1

accuracy = nCorrect/nTotal
speed = nTotal/((time.time()-st)/60)

resDir = '/home/nerdvana/Projects/mathWiz/results'
fs = glob.glob(os.path.join(resDir,'*.txt'))
if len(fs) == 0:
    newFile = os.path.join(resDir, '1.txt')
else:
    newFile = str(max([int(f.split('/')[-1].split('.')[0]) for f in fs])) + '.txt'
    newFile = os.path.join(resDir, newFile)

results = [str(f) for f in [nCorrect, accuracy, speed]]
with open(newFile, 'w') as f:
    f.write('\n'.join(results))

print('\nIncorrect answers: \n')
if len(incorrect) == 0:
    print('None :)\n')
else:
    print(pd.DataFrame(incorrect))
