# Natural-Language-Processing
Contains assignments for CS 4395 - Human Language Technologies

## Assignment 0

This is an overview of NLP

[pdf here](OverviewofNLP.pdf)


## Assignment 1

This is an assignment 1. The program takes in text from a file and formats it using regex to the required format. It runs in pycharm after a system argument is manually inputted. 

[code here](Homework1/Homework1_vxp200027.py)


Strengths of python in text processing is that there are lots of libraries, dynamic typing, 
and lots of built-in string methods to work with strings. A weakness could be that a large program could be slower to run compared to C++ or Java since it is interpreted. 

I learned about pickling and and system arguments in python. The syntax of Python and using regular expressions and classes was a review for me since I had experience with it. 


## Assignment 2
This is an assignment tht uses google colabs to utilize the functions in NLTK API. 

[pdf here](vxp200027-Assignment2.pdf)


## Assignment 3- Guessing Game

This is an assignment 3. The program takes in text from a file and first calculates the lexical diversity. It then tokenizes the text and  get alphas, lowercases the tokens, and find the tokens with length > 5. 
It then finds the lemmas and attaches pos taggers to them. It then selects all the nouns and puts them in a list. It then returns the list of nouns and tokens to the main function. The 50 most common nouns are selected
and used to implement a guessing game similar to hangman.

[code here](Homework2/Homework2_vxp200027.py)

## Assignment 4
This is an assignment that demonstrates ability to use Wordnet. 

[pdf here](vxp200027-wordnetassignment.pdf)

## Assignment 5

Instructions: Program 1: Build separate language models for 3 languages as follows. 
a. create a function with a filename as argument
b. read in the text and remove newlines
c. tokenize the text
d. use nltk to create a bigrams list
e. use nltk to create a unigrams list
f. use the bigram list to create a bigram dictionary of bigrams and counts, [token1 token2] -> 
count
g. use the unigram list to create a unigram dictionary of unigrams and counts, [token ] -> 
count
h. return the unigram dictionary and bigram dictionary from the function
i. in the main body of code, call the function 3 times for each training file, pickle the 6 
dictionaries, and save to files with appropriate names. The reason we are pickling them in 
one program and unpickling them in another is that NLTK ngrams is slow and if you put this 
all in one program, you may waste a lot of time waiting for ngrams() to finish.

[code here](Homework3\program1.py)



Program 2. 
a. Read in your pickled dictionaries. 
b. For each line in the test file, calculate a probability for each language (see note below) and 
write the language with the highest probability to a file.
c. Compute and output your accuracy as the percentage of correctly classified instances in the 
test set. The file LangId.sol holds the correct classifications.
d. output your accuracy, as well as the line numbers of the incorrectly classified items
3. Narrative. Write a one-page or more narrative about Ngrams:
a. what are n-grams and how are they used to build a language model
b. list a few applications where n-grams could be used
c. a description of how probabilities are calculated for unigrams and bigrams
d. the importance of the source text in building a language model
e. the importance of smoothing, and describe a simple approach to smoothing
f. describe how language models can be used for text generation, and the limitations of this 
approach
g. describe how language models can be evaluated
h. give a quick introduction to Google’s n-gram viewer and show an example 

[code here](Homework3\program2.py) [pdf here](Homework3\vxp200027-narrative.pdf)


