import vaderSentiment
from vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def test_sentences():
    sentences = [["VADER is smart, handsome, and funny.",
                  (0.0, 0.254, 0.746, 0.8316)],
                 ["I have a bad feeling about this.",
                  (0.35, 0.5, 0.15, -0.4588)],
                 ["I feel good about this.",
                  (0.0, 0.58, 0.42, 0.4404)],
                 ["Not such a badass after all.",
                  (0.289, 0.711, 0.0, -0.2584)],
    ]
    for (s,r) in sentences:
        vs = analyzer.polarity_scores(s)
        assert vs['neg'] == r[0]
        assert vs['neu'] == r[1]
        assert vs['pos'] == r[2]
        assert vs['compound'] == r[3]
                
