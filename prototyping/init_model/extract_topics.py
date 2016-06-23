
'''
Speech Transcript processing / cleaning to feed the NLP pipeline
'''

import nltk
import string
import os
import re

import unidecode
import operator
import pprint


from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.decomposition import NMF


path = '/Users/smuddu/galvanize/capstone/data/Speeches/Obama'
token_dict = {}
stemmer = PorterStemmer()

pp = pprint.PrettyPrinter(indent=2)

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))

    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    #stems = stem_tokens(tokens, stemmer)
    return tokens

for subdir, dirs, files in os.walk(path):
    for file in files:
        if (file != 'links'):
            pp.pprint("-- processing: {}".format(file))
            file_path = subdir + os.path.sep + file
            shakes = open(file_path, 'r')
            _raw_input = shakes.read()
            text = unidecode.unidecode_expect_nonascii(_raw_input)
            re.sub("[\W\d]", " ", text.lower().strip())
            lowers = text.replace('\n',' ').replace('\r',' ')
            while "  " in lowers:
                lowers = lowers.replace('  ',' ')
            no_punctuation = lowers.translate(None, string.punctuation)
            token_dict[file] = no_punctuation


tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
tfs = tfidf.fit_transform(token_dict.values())


num_topics = 20
model = NMF(n_components=num_topics, init='random', random_state=0)
model.fit(tfs)

id2word = {}
for k in tfidf.vocabulary_.keys():
    id2word[tfidf.vocabulary_[k]] = k

for topic_index in xrange(num_topics):
    print ""
    pp.pprint("-- Top words in topic:")
    topic_importance = dict(zip(id2word.values(),list(model.components_[topic_index])))
    sorted_topic_imp = sorted(topic_importance.items(), key=operator.itemgetter(1),reverse=True)
    pp.pprint([i[0] for i in sorted_topic_imp[:19]])
