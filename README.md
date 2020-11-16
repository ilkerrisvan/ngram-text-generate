# ngram_text_generate

if you don't have nltk 

sudo pip3 install -U nltk 

unigram : a,b,c,d,e,f,g -> e,f,b,g,e,c,a
bigram : a,b b,c c,d, d,e, e,x x,y -> abcdexy
trigram : a,b,c c,d,e e,f,x, x,y,z -> abcdefxyz

To run the code, write:
python3 ngram.py directory corpus

ngram.py is name of python file , directory is directory of the corpus , corpus is
name of corpus and this argument must be .txt

e.g.: python3 ngram.py /home/ilker/Desktop/ tech_corpus.txt

you can get corpus:

http://www.kemik.yildiz.edu.tr/veri_kumelerimiz.html (TR)
https://uclnlp.github.io/ai4exams/data.html (EN)
