import math
import pathlib
import pickle

from nltk import ngrams, word_tokenize

#load all pickled files
dict_eng = pickle.load(open('dict.eng', 'rb'))
dict_eng2 = pickle.load(open('dict.eng', 'rb'))
dict_fre = pickle.load(open('dict.fre', 'rb'))
dict_fre2 = pickle.load(open('dict.fre2', 'rb'))
dict_ita = pickle.load(open('dict.ita', 'rb'))
dict_ita2 = pickle.load(open('dict.ita2', 'rb'))


def compute_prob(text, unigram_dict, bigram_dict, V):
    # N is the number of tokens in the training data
    # V is the vocabulary size in the training data (unique tokens)

    unigrams_test = word_tokenize(text)
    bigrams_test = list(ngrams(unigrams_test, 2))

    p_laplace = 1  # calculate p using Laplace smoothing

    for bigram in bigrams_test:
        n = bigram_dict[bigram] if bigram in bigram_dict else 0

        d = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
    #calculate laplace smoothing
        p_laplace = p_laplace * ((n + 1) / (d + V))

    return p_laplace

#open test file
with open(pathlib.Path.cwd().joinpath('LangId.test'), 'r', encoding='utf-8') as f:
    text_in = f.read()
    text = text_in.splitlines()


    #open created solution file
    with open("mysol.txt", 'r+') as file:
        file.truncate(0)
    counter = 0
    #for each line calculate probability and write the language of max probability to file
    for line in text:
        counter = counter + 1
        prob = compute_prob(line, dict_eng, dict_eng2, len(dict_eng))
        prob2 = compute_prob(line, dict_fre, dict_fre2, len(dict_fre))
        prob3 = compute_prob(line, dict_ita, dict_ita2, len(dict_ita))
        print(prob2)
        maxprob = max(prob, prob2, prob3)
        if maxprob == prob:
            with open('mysol.txt', 'a') as r:
                r.write(str(counter) + ' English' + '\n')
        elif maxprob == prob2:
            with open('mysol.txt', 'a') as r:
                r.write(str(counter) + ' French' + '\n')
        else:
            with open('mysol.txt', 'a') as r:
                r.write(str(counter) + ' Italian' + '\n')

    #open solution file
    with open("LangId.sol", 'r') as file:
        text_in = file.read()
        text = text_in.splitlines()
        #open created file
        with open('mysol.txt', 'r') as r:
            text_in2 = r.read()
            text2 = text_in2.splitlines()
            count = 0
            missclassified = []
            counter = 0
            #calculate missclassifications
            for i in range(len(text2)):
                counter = counter + 1
                if text[i] == text2[i]:
                    count = count + 1
                else:
                    missclassified.append(counter)

    #return accuracy
            accuracy = count / len(text2)
            print('Accuracy: ' + str(accuracy))
            print('Lines misclassified: ' + str(missclassified))
