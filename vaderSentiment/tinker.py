import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus.reader import wordnet
nltk.download('words')
import vaderSentiment
from vaderSentiment import SentimentIntensityAnalyzer



f = open(r'D:\VSC\Coding\vaderSentiment\vaderSentiment\vader_text.txt').read().split()
wordlist1 = nltk.corpus.words.words()
wordlist2 = []
wordlist3 = []
wordlist4 = []
for word in f:
    x = wn.morphy(word)
    if x == None:
        wordlist2.append(word)
    else:
        wordlist3.append(x)

for word in wordlist2:
    if word in wordlist1:
        continue
    else:
        wordlist4.append(word)
        
#print(wordlist4)


#with open('notinWN.txt', 'w') as f:
#    print(wordlist4, file=f)

#with open('baseform.txt', 'w') as f:
#    print(wordlist3, file=f)


analyzer = SentimentIntensityAnalyzer()
for word in wordlist3:
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



