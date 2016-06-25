
import pandas as pd

from string import punctuation
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class SpeechBuilder():
    '''
    Build a speech corpus to contain documents (speeches)
    Add helper methods to manipulate documents/sentences and to access information

    Store all the information in a dataframe to maintain associations between
    documents, sentences and their related information
    '''

    def __init__(self,name):
        self.name = name
        self.df = None

        ''' tfidf vectorizer for the corpus '''
        self.tfidf = None

        ''' dict containing the vocabulary - index mapping '''
        self.vocabulary = None

        ''' topic-to-vocabulary vectors '''
        self.topic_vector = None


    def build_corpus(self, path):
        '''
        parse the files pointed by 'path' and populate the speech dataframe
        '''

        files_to_contents = parse_files(path)
        self.df = pd.DataFrame.from_dict(files_to_contents)




    def stringify_speech(self, raw_content):
        Given raw contents read from files, clean up and return a string
        '''

    def cleanup_raw(self, raw_content):
        '''
        '''
        Given raw content read from files, just do basic cleanup and return a string
        Do not remove carriage returns and newlines
        '''

    def get_sentences(self):
        '''
        Given the speech data, populate sentences from it
        '''

    def compute_tfidf(self):
        '''
        Given the entire corpus, compute tf-idf
        Return corpus's tfidf and vocabulary
        '''

    def generate_topics_nmf(self):
        '''
        Given the entire corpus, generate topics by running NMF
        '''

    def parse_files(folder_path):

        for subdir, dirs, files in os.walk(folder_path):
            for file in files:
                pp.pprint("-- processing: {}".format(file))
                file_path = subdir + os.path.sep + file
                f = open(file_path, 'r')
                _raw_input = f.read()
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


