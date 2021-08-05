import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus.reader import wordnet
nltk.download('words')
import vaderSentiment
from vaderSentiment import SentimentIntensityAnalyzer



f = open(r'D:\VSC\Coding\vaderSentiment\vaderSentiment\vader_text.txt').read().split()
nltkcorp = nltk.corpus.words.words()
wordlist2 = []
baseform = []
notinWN = []
for word in f:
    x = wn.morphy(word)
    if x == None:
        wordlist2.append(word)
    else:
        baseform.append(x)

for word in wordlist2:
    if word in nltkcorp:
        continue
    else:
        notinWN.append(word)

        
#print(wordlist4)

notinWN = list(set(notinWN))
with open('notinWN.txt', 'w') as f:
    print("\n".join(sorted(notinWN)), file=f)

baseform = list(set(baseform))
with open('baseform.txt', 'w') as f:
   print("\n".join(sorted(baseform)), file=f)


analyzer = SentimentIntensityAnalyzer()
for word in baseform:
    for s in wn.synsets(word):
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
    print(analyzer.polarity_scores(word)['compound'])



