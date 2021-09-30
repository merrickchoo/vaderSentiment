import emoji
from emoji import unicode_codes

EMOJI_UNICODE = unicode_codes.EMOJI_UNICODE['en']
emojis = sorted(EMOJI_UNICODE.values(), key=len, reverse=True)

fh = open('vaderSentiment/data/emojis.txt', 'w')
for e in emojis:
    print(e, file = fh)

fh.close()
