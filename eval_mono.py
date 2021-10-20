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


def eval_mono(list):
   mono_data = []
   wscore_list = []
   dscore_list = []
   no_wscore = []
   no_dscore = []
   no_score = []
   prob_score = []
   analyzer = SentimentIntensityAnalyzer()
   for str in list:
        for s in wn.synsets(str):
            defn = s.definition()
            sto = []
            hypo = []
            hype = []
            i_hypo = []
            i_hype = []
            for sh in s.similar_tos():
                sto += sh.lemma_names()
            for sh in s.hyponyms():
                hypo += sh.lemma_names()
            for sh in s.hypernyms():
                hype += sh.lemma_names()
            for sh in s.instance_hyponyms():
                i_hypo += sh.lemma_names()
            for sh in s.instance_hypernyms():
                i_hype += sh.lemma_names()
            wscore = analyzer.polarity_scores(str)['compound']
            dscore = analyzer.polarity_scores(defn)['compound'] + analyzer.polarity_scores(sto)['compound'] + analyzer.polarity_scores(hypo)['compound'] + analyzer.polarity_scores(hype)['compound'] + analyzer.polarity_scores(i_hypo)['compound']+ analyzer.polarity_scores(i_hype)['compound']
        if wscore == 0:
            no_wscore.append(str)
        if dscore == 0:
            no_dscore.append(str)
        if wscore == 0 and dscore == 0:
            no_score.append(str)
        if (wscore > 0 and dscore < 0) or (wscore < 0 and dscore > 0):
            prob_score.append(str)
        wscore_list.append(float(wscore))
        dscore_list.append(float(dscore))
        mono_data.append((str,wscore,dscore))
   print(mono_data, sep='\n') #output sentiment scores
   print(stats.pearsonr(wscore_list, dscore_list))
   print(stats.spearmanr(wscore_list, dscore_list, axis=0, nan_policy='propagate'))
    #print(no_wscore)
    #print(no_dscore)
    #print(no_score)
   print(prob_score)

def eval_mono2(list):
   mono_data = []
   wscore_list = []
   dscore_list = []
   no_wscore = []
   no_dscore = []
   no_score = []
   analyzer = SentimentIntensityAnalyzer()
   for str in list:
        for s in wn.synsets(str):
            defn = s.definition()
            wscore = analyzer.polarity_scores(str)['compound']
            dscore = analyzer.polarity_scores(defn)['compound']
            if wscore == 0:
                no_wscore.append(str)
            if dscore == 0:
                no_dscore.append(str)
            if wscore == 0 and dscore == 0:
                no_score.append(str)
        wscore_list.append(float(wscore))
        dscore_list.append(float(dscore))
        mono_data.append((str,wscore,dscore))
   #print(mono_data, sep='\n') #output sentiment scores
   #print(evalfile)
   print(stats.pearsonr(wscore_list, dscore_list))
   print(stats.spearmanr(wscore_list, dscore_list, axis=0, nan_policy='propagate'))
   #print(no_wscore)
   #print(no_dscore)
   #print(no_score)
    
eval_mono(mono_list)
eval_mono2(mono_list)