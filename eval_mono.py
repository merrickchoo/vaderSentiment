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
            defn = [s.definition()]
            words = []

            if 'sto' in flag:
                for sh in s.similar_tos():
                    words += sh.lemma_names()
            if 'sto_def' in flag:
                for sh in s.similar_tos():
                    defn.append(sh.definition())
            if 'sto_ex' in flag:      #hurts the accuracy
                for sh in s.similar_tos():
                    words += sh.examples()

            if 'hypo' in flag:
                for sh in s.hyponyms():
                    words += sh.lemma_names()
            if 'hypo_def' in flag:
                for sh in s.hyponyms():
                    defn.append(sh.definition())
            if 'hypo_ex' in flag:      #hurts the accuracy
                for sh in s.hyponyms():
                    words += sh.examples()

            if 'hype' in flag:
                for sh in s.hypernyms():
                    words += sh.lemma_names()
            if 'hype_def' in flag:      #hurts the accuracy
                for sh in s.hypernyms():
                    defn.append(sh.definition()) 
            if 'hype_ex' in flag:      #hurts the accuracy
                for sh in s.hypernyms():
                    words += sh.examples()    
    
            if 'i_hypo' in flag:        #not as important
                for sh in s.instance_hyponyms():
                    words += sh.lemma_names()
            if 'i_hype' in flag:        #not as important
                for sh in s.instance_hypernyms():
                    words += sh.lemma_names()

            if 'also' in flag:
               for sh in s.also_sees():
                  words += sh.lemma_names()
            if 'also_def' in flag:      #hurts the accuracy
                for sh in s.also_sees():
                    defn.append(sh.definition())
            if 'also_ex' in flag:       #hurts the accuracy      
                for sh in s.also_sees():
                    words += sh.examples()

            if 'att' in flag:
               for sh in s.attributes():
                  words += sh.lemma_names() 
            if 'att_def' in flag:       #hurts the accuracy
                for sh in s.attributes():
                    defn.append(sh.definition())
            if 'att_ex' in flag:        #hurts the accuracy      
                for sh in s.attributes():
                    words += sh.examples()

            if 'ex' in flag:
                words += s.examples()
            xdfn = '; '.join(defn+words)
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
   #print(true_no_wscore)
   #print(no_dscore)
   #print(no_score)
   #print(prob_score)

for flag in [[],['sto', 'sto_def', 'hypo', 'hypo_def', 'hype', 'also', 'att', 'ex']]:
    print(flag)
    eval_mono(mono_list, flag)

