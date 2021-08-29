import nltk
import fileinput
import string
import re
import vaderSentiment
from vaderSentiment import SentimentIntensityAnalyzer
from scipy import stats


base_dict = []
base_file = open(r'D:\VSC\vaderSentiment\additional_resources\hutto_ICWSM_2014\nytEditorialSnippets_GroundTruth.txt').readlines()
analyzer = SentimentIntensityAnalyzer()
for l in base_file:
   id, score, sentence = l.strip().split('\t')
   e_score = analyzer.polarity_scores(sentence)['compound']
   print(stats.spearmanr(score, e_score, axis=0, nan_policy='propagate', alternative='two-sided'))




#def eval(model,filename):
#    model=
#    base = open(r'filename').read().split()






















#start with the model, start with the filename
#output the ro
#output all the sentiment scores
