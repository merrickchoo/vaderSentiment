import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus.reader import wordnet
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()
w = 'astonish'
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
    hype = []
    for sh in s.hypernyms():
        hype += sh.lemma_names()
        print(hype)
    i_hypo = []
    for sh in s.instance_hyponyms():
        i_hypo += sh.lemma_names()
        print(i_hypo)
    i_hype = []
    for sh in s.instance_hypernyms():
        i_hype += sh.lemma_names()
        print(i_hype)
    es = []
    #for sh in s.eq_synonym():
    #    es += sh/lemma_names()
    #    print(es)
    xdfn = '; '.join([defn]+sto+hypo+hype+i_hype+i_hypo)
    print(xdfn)
    print(analyzer.polarity_scores(xdfn)['compound'])
    print(analyzer.polarity_scores(defn)['compound'])
    print(analyzer.polarity_scores(w))



 # differentiate by POS to find the right lemma?
 # using ntlk.pos_tag






