
import vaderSentiment
from vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()

eng_sent = ["VADER is smart, handsome, and funny.",  # positive sentence example
                 "VADER is smart, handsome, and funny!",
                 # punctuation emphasis handled correctly (sentiment intensity adjusted)
                 "VADER is very smart, handsome, and funny.",
                 # booster words handled correctly (sentiment intensity adjusted)
                 "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
                 "VADER is VERY SMART, handsome, and FUNNY!!!",
                 # combination of signals - VADER appropriately adjusts intensity
                 "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!",
                 # booster words & punctuation make this close to ceiling for score
                 "VADER is not smart, handsome, nor funny.",  # negation sentence example
                 "The book was good.",  # positive sentence
                 "At least it isn't a horrible book.",  # negated negative sentence with contraction
                 "The book was only kind of good.",
                 # qualified positive sentence is handled correctly (intensity adjusted)
                 "The plot was good, but the characters are uncompelling and the dialog is not great.",
                 # mixed negation sentence
                 "Today SUX!",  # negative slang with capitalization emphasis
                 "Today only kinda sux! But I'll get by, lol",
                 # mixed sentiment example with slang and constrastive conjunction "but"
                 "Make sure you :) or :D today!",  # emoticons handled
                 "Catch utf-8 emoji such as 💘 and 💋 and 😁",  # emojis handled
                 "Not bad at all"  # Capitalized negation
                 ]
#for str in eng_sent:
    #print(analyzer.polarity_scores(str))

jap_sent = ["VADERは賢く、ハンサムで、面白いです.",  # positive sentence example
                "VADERは賢く、ハンサムで、面白いです。!",
                # punctuation emphasis handled correctly (sentiment intensity adjusted)
                "VADERはとても賢くで、ハンサムで、面白いです。",
                # booster words handled correctly (sentiment intensity adjusted)
                "VADERは賢くもなく、ハンサムでも、面白くもありません。",  # negation sentence example
                "この本は良かった.",  # positive sentence
                "少なくともこれはとんだの本ではありません.",  # negated negative sentence with contraction
                "その本はちょっと良かっただけだった。",
                # qualified positive sentence is handled correctly (intensity adjusted)
                "プロットは良かったが、キャラクターは説得力がなく、ダイアログは素晴らしいものではありません。",
                # mixed negation sentence
                ]

for str in jap_sent:
    print(analyzer.polarity_scores(str))

chn_sent = ["VADER聪明、英俊与风趣.",  # positive sentence example
                "VADER聪明、英俊与风趣!",
                # punctuation emphasis handled correctly (sentiment intensity adjusted)
                "VADER非常聪明、英俊与风趣.",
                # booster words handled correctly (sentiment intensity adjusted)
                "VADER不聪明、不英俊也不风趣.",  # negation sentence example
                "这本书不错.",  # positive sentence
                "至少这本书不是特别的不好看.",  # negated negative sentence with contraction
                "这本书只是有点好看而已.",
                # qualified positive sentence is handled correctly (intensity adjusted)
                "这本书的情节很好，但人物没有吸引力，对话也不是很好.",
                # mixed negation sentence
                ]

for str in chn_sent:
    print(analyzer.polarity_scores(str))

mly_sent = ["VADER pintar, kacak, dan lucu.",  # positive sentence example
                 "VADER pintar, kacak, dan lucu!",
                 # punctuation emphasis handled correctly (sentiment intensity adjusted)
                 "VADER sangat pintar, kacak, dan lucuv.",
                 # booster words handled correctly (sentiment intensity adjusted)
                 "VADER SANGAT CERAH, tampan, dan SENANG.",  # emphasis for ALLCAPS handled
                 "VADER SANGAT CERAH, tampan, dan SENANG!!!",
                 # combination of signals - VADER appropriately adjusts intensity
                 "VADER SANGAT SMART, tampan uber, dan FRIGGIN FUNNY!!!",
                 # booster words & punctuation make this close to ceiling for score
                 "VADER tidak pintar, kacak, dan tidak lucu.",  # negation sentence example
                 "Buku itu bagus.",  # positive sentence
                 "Sekurang-kurangnya ia bukan buku yang mengerikan.",  # negated negative sentence with contraction
                 "Buku itu hanya bagus.",
                 # qualified positive sentence is handled correctly (intensity adjusted)
                 "Plotnya bagus, tetapi wataknya tidak menarik dan dialognya tidak bagus.",
                 # mixed negation sentence
                 "Hari ini SUX!",  # negative slang with capitalization emphasis
                 "Hari ini hanya sux! Tapi saya akan sampai, lol",
                 # mixed sentiment example with slang and constrastive conjunction "but"
                 "Tidaklah teruk sangat"  # Capitalized negation
                 ]


for str in mly_sent:
    print(analyzer.polarity_scores(str))

