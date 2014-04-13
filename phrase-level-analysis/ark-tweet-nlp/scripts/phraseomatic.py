# reproduction of Mike Heilman's Phrase-o-matric
import sys

is_noun = lambda t: t=='N' or t=='^'
is_na = lambda t: is_noun(t) or t=='A'

def get_nps(tags):
    for i in reversed(range(N)):
        if is_noun(tags[i]):
            j = i-1
            while j>=0:
                if not is_na(tags[j]): break
                yield j,i+1
                j -= 1


for line in sys.stdin:
    tokens,tags = line.split('\t')[:2]
    tokens = tokens.split()
    tags = tags.split()
    N = len(tokens)
    for s,e in get_nps(tags):
        # print tokens[s:e], tags[s:e]
        print '{}\t{}'.format(' '.join(tokens[s:e]), ' '.join(tags[s:e]))
