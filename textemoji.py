import emoji
from gensim.models import Word2Vec
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk, Text
from nltk.corpus import brown, movie_reviews, treebank, stopwords
from collections import Counter

text = 'Serving that truth tea Question: when is a polish worker deemed to be an asset? Answer: when his labour is cheap'

class TextEmoji:
	def __init__(self, length=3):
		'''
		length is a default length for empoji result
		'''
		self.length = length

	def _pre_processing(self, text):
		tokenized = word_tokenize(text)
		tokenized = [word for word in tokenized if word not in stopwords.words('english')]
		tagged = pos_tag(tokenized)
		return tagged

	def read_emoji(self, path='list.txt'):
		''' 
			reading list of emoji
		'''
		pass

	def word2vec_processing(self, corpora='treebank'):
		self.t = Word2Vec(movie_reviews.sents())

	def _word2vec_fit(self, word):
		try:
			print(self.t)
			if self.t is not None:
				return self.t.most_similar(word, topn=5)
		except Exception:
			return []

	def nltk_similar(self, word):
		text = Text(word.lower() for word in brown.words())
		print(text.similar(word))

	def text_emoji(self, text):
		tags = self._pre_processing(text)
		words = [word for (word, tag) in tags]
		print(Counter(words))
		#print(self.nltk_similar(tea))
		#print(self._word2vec_fit('tea'))
		print(tags)