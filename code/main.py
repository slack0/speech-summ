
from summextract import SummaryExtractor
from speechbuilder import SpeechBuilder

def main():
    '''
    INPUT:  None
    OUTPUT: Summary sentences extracted from every speech

    This wrapper uses Corpus and SummaryExtractor classes to:
    - build a corpus and
    - extract summaries from it
    '''

    speeches = Speches(name)
    speeches.build_corpus(path_to_corpus)

    extractor = SummaryExtractor()
    extractor.gen_summaries()

if __name__ =='__main__':
    main()

