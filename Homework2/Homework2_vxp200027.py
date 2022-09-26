# import libraries
import pathlib
import sys
import re
import pickle
from random import seed
from random import randint
import nltk
from nltk import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# main function
def main(filepath):
    with open(pathlib.Path.cwd().joinpath(filepath), 'r') as f:
        # read file
        text = f.read()

        # get number of nouns and tokens
        nouns, tokens = my_function(text)
        print(len(nouns))
        dict_nouns = {}

        # add nouns, count of nouns to dictionary
        for x in nouns:
            dict_nouns[x] = tokens.count(x)

        # sort nouns by count
        sorted_keys = sorted(dict_nouns.items(), key=lambda item: item[1], reverse=True)
        game_list = []
        # append top 50 nouns to game_list list
        for i in range(50):
            print(sorted_keys[i])
            game_list.append(sorted_keys[i][0])

        # pass game_list to guessing game
        guessing_game(game_list)


def guessing_game(game_list):
    seed(1234)
    # initialize user points
    user_points = 5

    if user_points < 0:
        exit()

    # select random word from game list
    guess_word = game_list[(randint(0, 49))]
    new_word = []

    # append _ to list
    for i in range(len(guess_word)):
        new_word.append("_")

    # add _ to string (number of _ is equal to number of letters in word)
    new_words = ""
    for i in range(len(guess_word)):
        new_words += "_"

    # call guess passing in parameters
    guess(guess_word, user_points, new_word, new_words, game_list)


# function to play game
def guess(guess_word, user_points, new_word, new_words, game_list):
    # prints string containing current progress on word
    print(new_words)

    # if negative points game over
    if user_points < 0:
        print("Sorry. Game Over")
        exit()

    # if word guessed allow user to guess another word
    if new_words == guess_word:
        print("You solved it!")
        print("Current score: " + str(user_points))
        print("Guess another word: ")
        guessword = game_list[(randint(0, 49))]
        new_word = []
        for i in range(len(guessword)):
            new_word.append("_")

        new_words = ""
        for i in range(len(guessword)):
            new_words += "_"
        guess(guessword, user_points, new_word, new_words, game_list)

    # ask for a letter guess
    guess1 = input("Guess a letter: ")

    # exit if guess = '!'
    if guess1 == "!":
        exit()

    # if letter is in word
    if guess1 in guess_word:
        new_words = ""
        # add 1 to score
        user_points = user_points + 1
        print("Right! Score is " + str(user_points))

        for i in range(len(guess_word)):
            # if letter in word is equal to guess add letter to current progress string
            if guess_word[i] == guess1:
                new_words += guess_word[i]

            else:
                # add current progress to string
                new_words += new_word[i]

    else:
        # subtract user points by 1
        user_points = user_points - 1
        print("Sorry, guess again. Score is " + str(user_points))

    # save current progress into list
    new_word = list(new_words)

    # call guess again with updated parameters
    guess(guess_word, user_points, new_word, new_words, game_list)


def my_function(text):
    # tokenize text
    tokens = word_tokenize(text)

    # lexical diversity
    print("\nLexical diversity: %.2f" % (len(set(tokens)) / len(tokens)))

    # lowercase tokens
    tokens = [t.lower() for t in tokens]

    # get tokens that are alpha and are not stopwords
    tokens = [t for t in tokens if t.isalpha() and
              t not in stopwords.words('english')]

    # get tokens that have a length greater than 5
    tokens = [t for t in tokens if len(t) > 5]

    # use lemmatizer
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens]
    # make unique
    lemmas_unique = list(set(lemmas))

    # attaching pos taggers
    tags = nltk.pos_tag(lemmas_unique)

    # first 20 tags
    for i in range(20):
        print(tags[i])

    # if the pos starts with n
    nouns = [token for token, pos in tags if pos.startswith('N')]

    # print len of nouns and tokens list
    print(len(nouns))
    print(len(tokens))
    return nouns, tokens


# if there is no filename as parameter ask for parameter
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
        exit()
    else:
        fp = sys.argv[1]

        main(fp)
