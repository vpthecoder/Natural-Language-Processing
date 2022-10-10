# import libraries
import pathlib
import sys
import re
import pickle
import nltk
from nltk import *







# main function
def main(filepath):
    with open(pathlib.Path.cwd().joinpath(filepath), 'r', encoding='utf-8') as f:

        # read file
        text_in = f.read()
        # no new lines
        text_in.replace("\n", "")
        #tokenize text
        tokens = word_tokenize(text_in)

        bigrams = list(ngrams(tokens, 2))
        unigrams = tokens

        #unigram dictionary
        unigram_dict = {t: unigrams.count(t) for t in set(unigrams)}

        #bigram dictionary
        bigram_dict = {b: bigrams.count(b) for b in set(bigrams)}

        return unigram_dict, bigram_dict







# if there is no filename as parameter ask for parameter
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
        exit()
    else:

        eng = sys.argv[1]
        fre = sys.argv[2]
        ita = sys.argv[3]
        eng_dict, eng_dict2 = main(eng)
        fre_dict, fre_dict2 = main(fre)
        ita_dict, ita_dict2 = main(ita)

        pickle.dump(eng_dict, open('dict.eng', 'wb'))
        pickle.dump(eng_dict2, open('dict.eng2', 'wb'))
        pickle.dump(fre_dict, open('dict.fre', 'wb'))
        pickle.dump(fre_dict2, open('dict.fre2', 'wb'))
        pickle.dump(ita_dict, open('dict.ita', 'wb'))
        pickle.dump(ita_dict2, open('dict.ita2', 'wb'))
