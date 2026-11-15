import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')
text="data visualizaton is way to express your data in visualize in context so that patter"
words=word_tokenize(text)
unigram=list(ngrams(words,1))
print(unigram)
bigram=list(ngrams(words,2))
print(bigram)
trigram=list(ngrams(words,3))
print(trigram)
