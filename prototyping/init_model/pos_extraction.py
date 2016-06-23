%run nmf_try.py
token_dict[0]
token_dict.keys()
token_dict['20080318.txt']
try_pos = token_dict['20080318.txt']
import nltk
nltk.word_tokenize(try_pos)
pos_text = nltk.word_tokenize(try_pos)
type(pos_text)
pos_text
nltk.positivenaivebayes?
nltk.pos_tag?
pos_text
nltk.pos_tag(pos_text)
try_pos = token_dict['20080318.txt']
from textblob import TextBlob
pos_blob = TextBlob(try_pos)
pos_blob.tags
pos_blob.noun_phrases
pos_blob.sentiment
pos_blob.words
pos_blob.word_counts
pos_blob.sentences
blob_sent = pos_blob.sentences
type(blob_sent)
len(blob_sent)
size(blob_sent)
pos_blob.ngrams
pos_blob.tokenize
pos_blob.detect_language
pos_blob.detect_language()
pos_blob.ngrams(n=2)
pos_blob.ngrams(n=3)
pos_blob.noun_phrases()
pos_blob.noun_phrase
pos_blob.noun_phrases
pos_blob.np_counts
token_dict['20080318.txt']
f = open('onespeech.txt','w')
f.write(token_dict['20080318.txt'])
pwd
token_dict['20080318.txt']
type(token_dict['20080318.txt'])
f.writelines(str)
f.write(str)
g = open('foo.txt','w')
g.write(token_dict['20080318.txt'])
g.close()
from textblob.taggers import NLTKTagger
nltk_tagger = NLTKTagger()
pos_blob.pos_tags
type(pos_blob.pos_tags)
dict(pos_blob.pos_tags)
pos_dict = dict(pos_blob.pos_tags)
sorted(pos_dict.items(), key=operator.itemgetter(1),reverse=True)
srtd_pos_dict = sorted(pos_dict.items(), key=operator.itemgetter(1),reverse=True)
pos_to_workdlist = {}
pos_to_wordlist = {}
for k, v in pos_dict.iteritems():
    pos_to_wordlist.setdefault(v, []).append(k)
pos_to_wordlist
pos_to_wordlist.keys()
pos_to_wordlist[u'JJS']
pos_to_wordlist[u'JJR']
pos_to_wordlist[u'UH']
from textblob.taggers import PatternTagger
history
type(pos_blob)
pt = PatternTagger()
pos_blob.pos_tagger(pt)
from textblob.tokenizers import SentenceTokenizer
tb = Blobber(pos_tagger=PatternTagger(), tokenizer=SentenceTokenizer())
from textblob import Blobber
tb = Blobber(pos_tagger=PatternTagger(), tokenizer=SentenceTokenizer())
oneentry = token_dict['20080318.txt']
type(oneentry)
blob_new = tb(oneentry)
blob_new.pos_tags
tags_from_pattrntagger = blob_new.pos_tags
type(tags_from_pattrntagger)
tags_from_pattrntagger
tags_from_pattrntagger = dict(blob_new.pos_tags)
type(tags_from_pattrntagger)
pos_to_wordlist = {}
for k, v in tags_from_pattrntagger.iteritems():
    pos_to_wordlist.setdefault(v, []).append(k)
pos_to_wordlist
pos_to_wordlist.keys()
pos_to_wordlist[u'JJ']
pos_to_wordlist.keys()
pos_to_wordlist
pos_to_wordlist.keys()
pos_to_wordlist[u'VBG']
pos_to_wordlist[u'VB']
pos_to_wordlist.keys()
history
%history -f /tmp/hist.py
