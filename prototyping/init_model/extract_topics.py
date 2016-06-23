
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

from collections import defaultdict

from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.decomposition import NMF


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))

    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    #stems = stem_tokens(tokens, stemmer)
    return tokens


def extract_topics(corpus_path, num_topics):

    ### construct a token dictionary
    for subdir, dirs, files in os.walk(corpus_path):
        for file in files:
            pp.pprint("-- processing: {}".format(file))
            file_path = subdir + os.path.sep + file
            shakes = open(file_path, 'r')
            _raw_input = shakes.read()
            text = unidecode.unidecode_expect_nonascii(_raw_input)
            re.sub("[\W\d]", " ", text.lower().strip())
            lowers = text.replace('\n',' ').replace('\r',' ')
            while "  " in lowers:
                lowers = lowers.replace('  ',' ')

            ''' store raw text -- for sentence extraction '''
            raw_text[file] = lowers

            ''' store no_punctuation for NMF '''
            no_punctuation = lowers.translate(None, string.punctuation)
            token_dict[file] = no_punctuation

    ### TF-IDF
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfs = tfidf.fit_transform(token_dict.values())

    model = NMF(n_components=num_topics, init='random', random_state=0)
    Wmat = model.fit_transform(tfs)

    id2word = {}
    for k in tfidf.vocabulary_.keys():
        id2word[tfidf.vocabulary_[k]] = k

    for topic_index in xrange(num_topics):
        print ""
        pp.pprint("-- Top words in topic:")
        topic_importance = dict(zip(id2word.values(),list(model.components_[topic_index])))
        sorted_topic_imp = sorted(topic_importance.items(), key=operator.itemgetter(1),reverse=True)
        pp.pprint([i[0] for i in sorted_topic_imp[:10]])


    ### For each document/speech -- extract the top sentences based on their cosine similarity to topics discovered

    speech_hash = defaultdict(dict)
    for doc in token_dict.iterkeys():
        doc_blob = TextBlob(raw_text[doc])
        sentence_count = 0
        for sentence in doc_blob.sentences:
            speech_hash[doc][sentence_count] = sentence
            sentence_count += 1

        #print 'KEYS: ', speech_hash[doc].keys()








if __name__ == '__main__':
    token_dict = {}
    raw_text = {}

    stemmer = PorterStemmer()
    pp = pprint.PrettyPrinter(indent=2)

    path = '/Users/smuddu/galvanize/capstone/data/Speeches/Obama'
    extract_topics(path,20)
    print len(token_dict)
