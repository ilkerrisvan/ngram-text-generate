"""
Author:İlker RİŞVAN
Date:04/11/2020

In this study, the sample corpus (data) is taken and creates Unigram, Bigram and Trigram sentences.
"""

import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.util import ngrams
import string
import sys

loc = sys.argv[1] ## location of your input
data = sys.argv[2] ## your data as input

##read corpus and tokenize it
newcorpus = PlaintextCorpusReader(loc,data)
newcorpus.raw(data)
newcorpus.sents(data)
enwords = newcorpus.words(data)  ## words
entext = newcorpus.raw(data)  ## text
entokens = nltk.word_tokenize(entext)

puncs = set(string.punctuation)
entokens = [word for word in entokens if word not in puncs] ##remove punctuation marks from corpus

## gen_txt method for bigrams and trigrams
## it finds the most common words in the data and starts with it
## and then generate a text,assume a,b is the most common words
## text starts with a,b so next word should begin with b
## (a,b) (b,c) (c,d) (e,f) -> a,b,c,d,e,f can be a text for bigram
## (a,b,c) (c,z,d) (d,y,w) -> a,b,c,z,d,y,w  can be a text for trigram
def gen_text(w,v,l,n): ## words,values,length,ngram's n
    max_val = max(v)   ## for find most common words
    first = w[max_val][0]
    next_word = w[max_val][1]
    next_word_temp =next_word ## used temp because keep safe "next_word" so it will be use
    words_to_text = []

    ## for find following words
    ## there might be a question why we use same indexes for bigram and trigram
    ## should use the second index for the trigram ? no.
    for i in w:
        if next_word_temp == i[0]:
           next_word_temp = i[1]
           words_to_text.append(i[1])

    words_to_text = words_to_text[:l] ## length of text
    words_to_text.insert(0,first)     ## add most common first
    words_to_text.insert(1,next_word) ## add most common second
    del(words_to_text[l+1])           ## if we add 2 elements so we need delete 2
    del(words_to_text[l])

    ##text outputs
    if n == 2: ##bigram = 2
        f = open("bigram_output.txt", "a")
        with open('bigram_output.txt', 'r+') as f :
            for i in words_to_text :
                f.write(str(i) + ' ')

    if n == 3: ##trigram = 3
        f = open("trigram_output.txt", "a")
        with open('trigram_output.txt', 'r+') as f :
            for i in words_to_text :
                f.write(str(i) + ' ')

##there is only one word
##so used most common words
def gen_text_unigram(w,v,l):
    values_to_text = []
    words_to_text = []

    ##add all words values
    for i in v:
         values_to_text.append(i)

    ##sort them the biggest -> smallest
    values_to_text.sort(reverse=True)

    ##add to an array these values words
    for i in values_to_text:
        words_to_text.append(w[i])

    words_to_text = words_to_text[:l] ##length of text

    f = open("unigram_output.txt", "a")
    with open('unigram_output.txt', 'r+') as f :
        for i in words_to_text :
            f.write(str(i[0]) + ' ')

##ngrams with using nltk
unigram = ngrams(entokens,1)
bigrams = nltk.bigrams(entokens)
trigrams = nltk.trigrams(entokens)

##freq for each gram
##ore detailed information can be viewed with .items() .keys() .values()
unigram_freq = nltk.FreqDist(unigram)
bigrams_freq = nltk.FreqDist(bigrams)
trigrams_freq = nltk.FreqDist(trigrams)

words_unigram  = []
values_unigram = []
words_bigrams  = []
values_bigrams = []
words_trigrams = []
values_trigrams = []

for items in unigram_freq.items():
        words_unigram.append(items[0])
        values_unigram.append(items[1])

for items in bigrams_freq.items():
        words_bigrams.append(items[0])
        values_bigrams.append(items[1])

for items in trigrams_freq.items():
        words_trigrams.append(items[0])
        values_trigrams.append(items[1])

##usermanual for terminal
def terminal_gui():
    n_gram = int(input("Please enter your choose.\n(1)Unigram\n(2)Bigram\n(3)Trigram\n"))
    len = int(input("How many words of text do you want to see?\n"))

    if n_gram == 1 :
        gen_text_unigram(words_unigram,values_unigram,len)
        print("You got your result as unigram_output.txt.Please check the directory.")
        ngram_text_program()
    if n_gram == 2 :
        gen_text(words_bigrams,values_bigrams,len,n_gram)
        print("You got your result as bigram_output.txt.Please check the directory.")
        ngram_text_program()
    if n_gram == 3 :
        gen_text(words_trigrams, values_trigrams,len,n_gram)
        print("You got your result as trigram_output.txt.Please check the directory.")
        ngram_text_program()
    else:
        print(n_gram)
        print("Please choose again.")
        terminal_gui()

## if need other n-grams select run and exit option
def run_choice():
    run_choice = int(input("(1) Run. (2) Exit. \n"))
    return run_choice

def ngram_text_program():
    while run_choice() == 1:
        terminal_gui()
    print("Goodbye.")
    exit()

ngram_text_program()