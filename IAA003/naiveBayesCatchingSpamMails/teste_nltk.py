from importlib import import_module
import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')

ps = PorterStemmer()

texto = '''ter teria tem amar amou amam amei'''

tokens = nltk.word_tokenize(texto)
#print(tokens)

radicais = ps.stem(texto)
print(radicais)