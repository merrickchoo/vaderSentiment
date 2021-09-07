import nltk
import fileinput
import string
import re
import vaderSentiment
from vaderSentiment import SentimentIntensityAnalyzer
from scipy import stats

def eval(modpath):
   base_data = []
   score_list = []
   e_score_list = []
   base_file = open(modpath).readlines()
   analyzer = SentimentIntensityAnalyzer()
   for l in base_file:
      id, score, sentence = l.strip().split('\t')
      e_score = analyzer.polarity_scores(sentence)['compound']
      score_list.append(score)
      e_score_list.append(e_score)
      base_data.append(id,score,sentence,e_score)
   print(base_data) #output sentiment scores
   print(stats.spearmanr(score_list, e_score_list, axis=0, nan_policy='propagate', alternative='two-sided'))

eval(r'additional_resources\hutto_ICWSM_2014\nytEditorialSnippets_GroundTruth.txt') 

#def eval(model,filename):
#    model=
#    base = open(r'filename').read().split()
