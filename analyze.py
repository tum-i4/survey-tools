import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from optparse import OptionParser
import os

nostem = {"accountability"}

def analyze(filename):
    stemmed = []

    stemmer = SnowballStemmer("english", ignore_stopwords=True)
    tokenizer = RegexpTokenizer(r'\w+')

    p65ali = nltk.Text(tokenizer.tokenize(open(filename,'rU').read()))


    for token in p65ali:
        if len(token) <= 2:
            continue
        if token.isdigit():
            continue
            
        token = token.lower()
        if token in nostem:
            stemmed.append(token)
        elif token in stemmer.stopwords:
            pass    
        else:
            stemmed.append(stemmer.stem(token))
    return stemmed

if __name__=='__main__':
    parser = OptionParser("usage: %prog -t {text file} ")
    parser.add_option('-t', '--text', action='store', type='string', dest='text_filename', help='Path to the text file')

    (opts, args) = parser.parse_args()

    text_filename = ''
    if not opts.text_filename=='':
        text_filename = opts.text_filename
    
    if os.path.isfile(text_filename):
        stemmed = analyze(text_filename)
        print(stemmed)
