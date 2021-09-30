##
## make a valence lexicon for emoji based on esr
## python esr2vader.py > vd-emoji-lex.tsv
##
import numpy as np
from pathlib import Path

esrfile = Path(__file__).with_name('Emoji_Sentiment_Data_v1.0.csv')


threshold = 5
maxvalue = 4


fh = open('vaderSentiment/data/esd-lex.txt', 'w')

print('#emoji, mean, std, frequency', file = fh)

for line in open(esrfile):
    if line.startswith('Emoji'):
        continue
    (emoji, codepoint, total, position,
     negative, neutral, positive, name,
     block) = line.strip().split(',')
    scores  =  [maxvalue] * int(positive)
    scores += [-maxvalue] * int(negative)
    scores +=  [0] * int(neutral)
    if int(total) >= threshold:
        print(f'# {name}\t{block}', file = fh)
        print (emoji, np.mean(scores), np.std(scores), total, sep='\t', file = fh)
fh.close()
