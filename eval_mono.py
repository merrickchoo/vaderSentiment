import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus.reader import wordnet
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from scipy import stats


analyzer = SentimentIntensityAnalyzer() 
base_fh = open('vaderSentiment\\baseform.txt')
mono = 0
mono_list = []
poly = 0
poly_list = []
for l in base_fh:
    w = l.strip()
    lemmas = wn.lemmas(w)
    if len(lemmas) == 1:
        mono += 1
        mono_list.append(w)

print(mono_list, sep='\n')

def eval_mono(list):
   mono_data = []
   word_score_list = []
   defn_score_list = []
   analyzer = SentimentIntensityAnalyzer()
   for str in list:
        for s in wn.synsets(str):
            defn = s.definition()
            word_score = analyzer.polarity_scores(str)['compound']
            defn_score = analyzer.polarity_scores(defn)['compound']
        word_score_list.append(float(word_score))
        defn_score_list.append(float(defn_score))
        mono_data.append((str,word_score,defn_score))
   print(mono_data, sep='\n') #output sentiment scores
   #print(evalfile)
   print(stats.pearsonr(word_score_list, defn_score_list))
   print(stats.spearmanr(word_score_list, defn_score_list, axis=0, nan_policy='propagate'))	

eval_mono(mono_list)