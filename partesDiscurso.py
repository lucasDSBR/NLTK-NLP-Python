import nltk
from nltk.tokenize import word_tokenize

sagan_quete = """
If you wish to make an apple pie from scratch,
you must first invent the universe."""

words_in_sagan_quote = word_tokenize(sagan_quete)

teste = nltk.pos_tag(words_in_sagan_quote)

print(teste)

