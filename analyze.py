import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

stemmer = SnowballStemmer("english", ignore_stopwords=True)
tokenizer = RegexpTokenizer(r'\w+')

p65ali = nltk.Text(tokenizer.tokenize(open('p65-ali.txt','rU').read()))

nostem = {"accountability"}

stemmed = [[]]

for token in p65ali:
	if len(token) <= 2:
		continue
	if token.isdigit():
		continue
	
	token = token.lower()
	if token in nostem:
		stemmed[0].append(token)
	elif token in stemmer.stopwords:
		pass	
	else:
		stemmed[0].append(stemmer.stem(token))

print(stemmed[0])
