import nltk
import fileinput
#import string
#import re
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from scipy import stats

#os.path

def eval(evalfile):
   base_data = []
   score_list = []
   e_score_list = []
   base_file = open(evalfile).readlines()
   analyzer = SentimentIntensityAnalyzer()
   for l in base_file:
      p_score, n_score, sentence = l.strip().split('\t')
      e_score = analyzer.polarity_scores(sentence)['compound']
      score = (int(p_score) - int(n_score))/5
      score_list.append(float(score))
      e_score_list.append(e_score)
      base_data.append((score, e_score, sentence))
   #print(base_data) #output sentiment scores
   print(evalfile, stats.pearsonr(score_list, e_score_list), stats.spearmanr(score_list, e_score_list, axis=0, nan_policy='propagate'))	


eval('6humanCodedDataSets\SS_1041MySpace.txt')
#eval('6humanCodedDataSets\SS_bbc1000.txt')
#eval('6humanCodedDataSets\SS_digg1084.txt')
#eval('6humanCodedDataSets\SS_rw1046.txt')
eval('6humanCodedDataSets\SS_twitter4242.txt')
eval('6humanCodedDataSets\YouTube3407.txt')


   
#eval('additional_resources/hutto_ICWSM_2014/nytEditorialSnippets_GroundTruth.txt') 
#eval('additional_resources/hutto_ICWSM_2014/amazonReviewSnippets_GroundTruth.txt')
#eval('additional_resources/hutto_ICWSM_2014/movieReviewSnippets_GroundTruth.txt')
#eval('additional_resources/hutto_ICWSM_2014/tweets_GroundTruth.txt')

#def eval(model,filename):
#    model=
#    base = open(r'filename').read().split()
