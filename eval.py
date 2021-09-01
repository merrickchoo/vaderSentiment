import nltk

import os
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from scipy import stats




gold_dir  = 'additional_resources/hutto_ICWSM_2014/'
gold_file = 'nytEditorialSnippets_GroundTruth.txt'
gold_fh   = open(os.path.join(gold_dir, gold_file)).readlines()

analyzer = SentimentIntensityAnalyzer()
for l in gold_fh:
   id, score, sentence = l.strip().split('\t')
   e_score = analyzer.polarity_scores(sentence)['compound']
#   print(stats.spearmanr(score, e_score, axis=0, nan_policy='propagate', alternative='two-sided'))
   print(id,e_score,score,sentence)




#def eval(model,filename):
#    model=
#    base = open(r'filename').read().split()






















#start with the model, start with the filename
#output the ro
#output all the sentiment scores
