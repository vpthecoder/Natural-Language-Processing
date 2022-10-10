import string

# imports used in project
from bs4 import BeautifulSoup
import requests
from nltk import *

from collections import Counter

from nltk.corpus import stopwords


# crawl function
def crawl(url2):
    starter_url = url2
    url = requests.get(starter_url)

    data = url.text
    soup = BeautifulSoup(data)

    counter3 = 0
    # write urls to a file
    with open('urls.txt', 'w') as f:
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))
            # checks if climate or global is in url
            if re.search("^.*climate.*$", link_str) or re.search("^.*global.*$", link_str):
                if '/url?=' in link_str:
                    link_str = link_str[7:]
                    print('MOD:', link_str)
                if '&' in link_str:
                    i = link_str.find('&')
                    link_str = link_str[:i]
                # if link starts with http and does not contain wiki,politic, or web that write it to file
                if link_str.startswith('https') and 'wiki' not in link_str and 'snap' not in link_str and 'web' not \
                        in link_str and 'qa' not in link_str:
                    f.write(link_str + '\n')
                    counter3 = counter3 + 1
                    if counter3 > 15:
                        break





with open('urls.txt', 'r') as f:
    urls50 = f.read().splitlines()

# call crawl with starter url
crawl("https://en.wikipedia.org/wiki/Climate_change")


# checking if an element is visible
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True


# get text from an url
def gettext(my_url):
    html = requests.get(my_url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})

    soup = BeautifulSoup(html.text)
    data = soup.findAll(text=True)
    result = filter(visible, data)
    temp_list = list(result)  # list from filter
    temp_str = ' '.join(temp_list)
    #return text
    return temp_str

#initialize counter
counter = 0
with open('urls.txt', 'r') as f:
    urls = f.read().splitlines()

#for each url in file get its text
for u in urls:
    url = gettext(str(u))
    #write text to new file for each url
    with open('data' + str(counter), 'w', encoding='utf-8') as f:
        urls = f.write(url)
    #increment counter
    counter = counter + 1
counter = 0


#fuction to clean up the text
def clean():
    #initialize counter
    counter = 0
    newlist = []
    for i in range(len(urls50)):
        #open each text file for each url
        with open('data' + str(counter), 'r', encoding='utf-8') as f:
            u = f.read()
            #remove newlines and tabs
            url3 = re.sub(r"[\n\t]*", "", u)
            #sentence tokenize
            sents = sent_tokenize(url3)
            with open('outfile' + str(counter), 'w', encoding="utf-8") as r:
                #write all sentences into file
                for sent in sents:
                    r.write(sent)

            newlist.append(f)
        #increment counter
        counter = counter + 1
    return newlist

#clean text
urlList = clean()

#find most inportant terms
def removeIrr():
    list_dict = []
    counter = 0
    for i in range(len(urls50)):
        with open('outfile' + str(counter), 'r', encoding="utf-8") as f:
            text2 = f.read()
            tokens = word_tokenize(text2)
            # lowercase tokens
            tokens = [t.lower() for t in tokens]

            # get tokens that are not stopwords
            tokens = [t for t in tokens if t.isalpha() and t not in stopwords.words('english')]

            tokens = [word.translate(string.punctuation) for word in tokens]

            dict_tokens = {}

            #for each word, count occurences of word and append word, count to dict
            for x in tokens:
                if len(x) > 2:
                    dict_tokens[x] = tokens.count(x)

                    list_dict.append(dict_tokens)

        counter = counter + 1
    return list_dict



orderedList = removeIrr()
#make a counter object
dict1 = Counter({})
for diction in orderedList:
    #add counter object to each dictionary cast as a counter object
    dict1 = dict1 + Counter(diction)

# 40 most common words
print(dict(dict1.most_common(40)))

# hardcoded top 10
top_10 = ['climate', 'global', 'warming', 'change', 'ocean', 'ice', 'carbon', 'emissions', 'temperature',
          'science']
dict_str = {}
for str2 in top_10:
    counter = 0

    list_sent = []
    for i in range(len(urls50)):
        # open file
        with open('data' + str(counter), 'r', encoding="utf-8") as f:
            text = f.read().splitlines()
            for line in text:
                text2 = sent_tokenize(line)
                # check if string is in sentence, if it is, add it to list
                for sent in text2:
                    if str2 in sent:
                        list_sent.append(sent)
            #increment counter
            counter = counter + 1

    #dict: key=word in top10, value=list of sentences with the word
    dict_str[str2] = list_sent

# knowledge base
for value, key in zip(dict_str.values(), dict_str.keys()):
    print(key + ':')
    print(value)
