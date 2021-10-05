import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus.reader import wordnet
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer() 
base_fh = open('vaderSentiment\\baseform.txt')
mono = 0
poly = 0
for l in base_fh:
    w = l.strip()
    lemmas = wn.lemmas(w)
    if len(lemmas) == 1:
        #print(w, lemmas[0])
        mono += 1
        
    else:
        poly += 1
        for l in lemmas:
            defn = l.synset().definition()
            w_score = analyzer.polarity_scores(w)['compound']
            d_score = analyzer.polarity_scores(defn)['compound']
            if (w_score > 0 and d_score < 0) or (w_score < 0 and d_score > 0):
                print('opposite')
            print(abs(w_score - d_score), w_score, d_score, w, defn, sep ='\t')
            
print(mono)
print(poly)