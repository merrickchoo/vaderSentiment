from typing import ValuesView
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus.reader import wordnet
import string
from collections import defaultdict as dd

# also read intensifeiers , diminishers, negators (VADER)

base = open('C:\VSC\SO-CAL\Resources\dictionaries\English\int_dictionary1.11.txt').readlines()
vader_I = open('vaderSentiment\intensifiers.txt').readlines()
vader_D = open('vaderSentiment\diminishers.txt').readlines()
inten = []
dimi = []


for l in base:
    word, score = l.strip().split('\t')
    if float(score) < 0:
        dimi.append(word)
    if float(score) > 0:
        inten.append(word)



for l in vader_I:
    w = l.strip('\n')
    if w in inten:
        pass
    else:
        inten.append(w)

for l in vader_D:
    w = l.strip('\n')
    if w in dimi:
        pass
    else:
        dimi.append(w)




i_syn_ids = dd(set)

d_syn_ids = dd(set)


for str in inten:
    for s in wn.synsets(str):
        if (s.pos() == 'r'):
            syn_id = ('{}-{}'.format(f'{s.offset():08}', s.pos()))
            i_syn_ids[syn_id].add(str)
            #print(str,syn_id,s.definition(),s.lemma_names()) # go through definitiion


           



for str in dimi:
    for s in wn.synsets(str):
        if (s.pos() == 'a') or (s.pos() == 'r') or (s.pos() == 's'):
            syn_id = ('{}-{}'.format(f'{s.offset():08}', s.pos()))
            d_syn_ids[syn_id].add(str)
            print(str,syn_id,s.definition()) # go through definitiion




i_ili_ids = []
d_ili_ids = []
base = open('C:\VSC\cili\ili-map-pwn30.tab').readlines()
for l in base:
    ili_id, syn_id = l.strip().split('\t')
    if syn_id in i_syn_ids:
        i_ili_ids.append(ili_id)
    if syn_id in d_syn_ids:
        d_ili_ids.append(ili_id)
#print(i_ili_ids)
#print(d_ili_ids)