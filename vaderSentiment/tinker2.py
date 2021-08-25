import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus.reader import wordnet
import vaderSentiment
from vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()
w = 'well'
for s in wn.synsets(w):
    print(s.lemma_names(),s.definition())
    defn = s.definition()
    sto = []
    for sh in s.similar_tos():
        sto += sh.lemma_names()
        print(sto)
    hypo = []
    for sh in s.hyponyms():
        hypo += sh.lemma_names()
        print(hypo)
    xdfn = '; '.join([defn]+sto+hypo)

    print(xdfn)
    print(analyzer.polarity_scores(xdfn)['compound'])
    print(analyzer.polarity_scores(defn)['compound'])
    print(analyzer.polarity_scores(w))



 similar_tos
 hyponyms
 hypernyms
 instance_hypernyms
 Instance_hyponyms
 eq_synonym
