# coding: utf-8
import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import defaultdict as dd

sent = dd(list)


### values for the original vader model
sent['en_vader'] = [["VADER is smart, handsome, and funny.",
                     (0.0, 0.254, 0.746, 0.8316)],
                    ["I have a bad feeling about this.",
                     (0.35, 0.5, 0.15, -0.4588)],
                    ["I feel good about this.",
                     (0.0, 0.58, 0.42, 0.4404)],
                    ["Not such a badass after all.",
                     (0.289, 0.711, 0.0, -0.2584)],
]
### values for GerVader
sent['de_vader'] = [["VADER ist klug, gutaussehend und lustig. ",
                     (0.0, 0.617, 0.383, 0.4767) ],
                    ["Nicht so krass letztlich.",
                     (0.459, 0.541, 0.0, -0.3713)],
                    ["Ich bin überrascht zu sehen, nur wie erstaunlich nützlich VADER!",
  (0.459, 0.541, 0.0, -0.3713)]
]


def test_meta():
    analyzer =  SentimentIntensityAnalyzer('en_vader')
    meta = analyzer.meta
    assert meta['lang'] == 'en'
    assert meta['url']  ==  "https://github.com/cjhutto/vaderSentiment"


def test_models():
    for model in sent:
        analyzer = SentimentIntensityAnalyzer(model)

        sentences = sent[model]

        for (s,r) in sentences:
            vs = analyzer.polarity_scores(s)
            msg = "{}: {}".format(model, s)
            assert vs['neg'] == r[0], msg
            assert vs['neu'] == r[1], msg
            assert vs['pos'] == r[2], msg
            assert vs['compound'] == r[3], msg
                
