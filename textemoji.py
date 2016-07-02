import emoji
import random
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
		self._emoji_list = self._read_emoji()

	def _pre_processing(self, text):
		tokenized = word_tokenize(text)
		tokenized = [word for word in tokenized if word not in stopwords.words('english')]
		tagged = pos_tag(tokenized)
		return tagged

	def _read_emoji(self, path='list.txt'):
		''' 
			reading list of emoji
		'''

		return [line.rstrip('\n') for line in open(path)]

	def word2vec_processing(self, corpora='treebank'):
		self.t = Word2Vec(movie_reviews.sents())

	def _word2vec_fit(self, word):
		''' classification with word2vec. Experimental
		'''
		try:
			print(self.t)
			if self.t is not None:
				return self.t.most_similar(word, topn=5)[0][0]
		except Exception:
			return ''

	def nltk_similar(self, word):
		text = Text(word.lower() for word in brown.words())
		print(text.similar(word))

	def text_emoji(self, text):
		tags = self._pre_processing(text)
		words = [word for (word, tag) in tags]
		counter = Counter(words).most_common()
		common = [key for key, value in counter if len(key) > 3 and value > 1]
		all_words = []
		all_words.extend(common)
		for comm in common:
			all_words.append(self._word2vec_fit(comm))
		#print(self.nltk_similar(tea))
		#print(self._word2vec_fit('tea'))
		random.shuffle(all_words)
		# find any words on emoji list
		print(text)
		print(emoji.emojize(' '.join([':'+item+':' for item in set(self._emoji_list).intersection(all_words)])))
