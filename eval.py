import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus.reader import wordnet
import fileinput
#import string
#import re

import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from scipy import stats

#os.path

def eval_senti(evalfile):
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


#eval_senti('6humanCodedDataSets\SS_1041MySpace.txt')
#eval_senti('6humanCodedDataSets\SS_twitter4242.txt')
#eval_senti('6humanCodedDataSets\YouTube3407.txt')

def eval_vader(evalfile):
   base_data = []
   score_list = []
   e_score_list = []
   d_score_list = []
   base_file = open(evalfile).readlines()
   analyzer = SentimentIntensityAnalyzer()
   for l in base_file:
      index, score, sentence = l.strip().split('\t')
      for w in sentence:
        for s in wn.synsets(w):
            defn = [s.definition()]
            words = []
            for sh in s.similar_tos():
               words += sh.lemma_names()
            for sh in s.similar_tos():
               defn.append(sh.definition())
            for sh in s.hyponyms():
               words += sh.lemma_names()
            for sh in s.hyponyms():
               defn.append(sh.definition())
            for sh in s.hypernyms():
               words += sh.lemma_names()
            for sh in s.also_sees():
               words += sh.lemma_names()
            for sh in s.attributes():
               words += sh.lemma_names() 
            words += s.examples()
            xdfn = '; '.join(defn+words)
      d_score = analyzer.polarity_scores(xdfn)['compound']
      e_score = analyzer.polarity_scores(sentence)['compound']
      score_list.append(float(score))
      e_score_list.append(e_score)
      d_score_list.append(float(d_score))
      base_data.append((score, e_score, sentence))
   #print(base_data) #output sentiment scores
   print(evalfile, stats.pearsonr(score_list, e_score_list), stats.spearmanr(score_list, e_score_list, axis=0, nan_policy='propagate'))	
   print(evalfile, stats.pearsonr(d_score_list, e_score_list), stats.spearmanr(d_score_list, e_score_list, axis=0, nan_policy='propagate'))	
   
eval_vader('vaderSentiment\_additional_resources\hutto_ICWSM_2014\_amazonReviewSnippets_GroundTruth.txt') 
eval_vader('vaderSentiment\_additional_resources\hutto_ICWSM_2014\movieReviewSnippets_GroundTruth.txt')
eval_vader('vaderSentiment\_additional_resources\hutto_ICWSM_2014\_nytEditorialSnippets_GroundTruth.txt')
eval_vader('vaderSentiment\_additional_resources\hutto_ICWSM_2014\_tweets_GroundTruth.txt')


