#Realizando tokenização por palavra e por frase.
from nltk.tokenize import sent_tokenize, word_tokenize

exemplo = """Uma vez que realizamos uma ação,
não saberemos ao certo o que pode acontecer. 
O universo acaba sendo um ambiente totalmente totalmente
imprevisível."""

#Tokenizando texto por sentença
exemplo_sentenca = sent_tokenize(exemplo)

#Tokenizando texto por palavras
exemplo_palavra = word_tokenize(exemplo)
print(exemplo_palavra)