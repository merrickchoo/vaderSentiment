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
        

           



for str in dimi:
    for s in wn.synsets(str):
        if (s.pos() == 'a') or (s.pos() == 'r') or (s.pos() == 's'):
            syn_id = ('{}-{}'.format(f'{s.offset():08}', s.pos()))
            d_syn_ids[syn_id].add(str)

ad_i = []
add_i = open('vaderSentiment\inten-r.txt').readlines()
ad_d = []
add_d = open('vaderSentiment\dimi-r.txt').readlines()

for l in add_i:
    syn_id = l.strip()
    ad_i.append(syn_id)


for l in add_d:
    syn_id = l.strip()
    ad_d.append(syn_id)
print(ad_d)

i_ili_ids = []
d_ili_ids = []
ad_d =[]
base = open('C:\VSC\cili\ili-map-pwn30.tab').readlines()

for l in base:
    ili_id, syn_id = l.strip().split('\t')
    if (syn_id in i_syn_ids) or (syn_id in ad_i):
        i_ili_ids.append(ili_id)
    if syn_id in d_syn_ids:
        d_ili_ids.append(ili_id)
    if syn_id in ad_d: # not in ili_ids
        d_ili_ids.append(ili_id)
print(i_ili_ids)
print(d_ili_ids)