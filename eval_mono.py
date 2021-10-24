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


def eval_mono(list, flag):

   mono_data = []
   wscore_list = []
   dscore_list = []
   no_wscore = []
   no_dscore = []
   no_score = []
   prob_score = []
   true_no_wscore = []
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
            xdfn = '; '.join([defn]+sto+hypo+hype+i_hype+i_hypo)
            wscore = analyzer.polarity_scores(str)['compound']
            dscore = analyzer.polarity_scores(xdfn)['compound']
        if wscore == 0:
            no_wscore.append(str)
        if dscore == 0:
            no_dscore.append(str)
        if wscore == 0 and dscore == 0:
            no_score.append(str)
        if (wscore > 0 and dscore < 0) or (wscore < 0 and dscore > 0):
            prob_score.append(str)
        if str in no_wscore not in no_score:
           true_no_wscore.append(str) 
        wscore_list.append(float(wscore))
        dscore_list.append(float(dscore))
        mono_data.append((str,wscore,dscore))
#   print(mono_data, sep='\n') #output sentiment scores
   print(stats.pearsonr(wscore_list, dscore_list))
   print(stats.spearmanr(wscore_list, dscore_list, axis=0, nan_policy='propagate'))
   print(true_no_wscore)
   #print(no_dscore)
   #print(no_score)
   print(prob_score)
    
eval_mono(mono_list)
