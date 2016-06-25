
class SpeechCorpus(obj):

    '''
    Main class containing the corpus of speeches 
    '''

    def __init__(self,path,n_topics):
        self.corpus = {}
        self.documents = []
        self.vocabulary = []
        self.tf_idf = None
        self.W = []
        self.H = []
        self.id2word = {}
        self.word2id = {}
        self.n_topics = n_topics
        self.path = path

    def create_corpus(self):
        '''
        Read in speech transcripts and populate corpus
        '''

    def vectorize(self):
        '''
        Perform vectorization of the corpus
        '''

    def gen_topics(self):
        '''
        Generate topics from vectorized corpus
        '''
