import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

citacao = "Uma vez flamengo, sempre flamengo. Uma vez Palmeiras, sempre Palmeiras"

citacaoPorPalavra = word_tokenize(citacao)

palavrasParada = set(stopwords.words("portuguese"))

listaFiltro = []

for palavra in citacaoPorPalavra:
    if palavra.casefold() not in palavrasParada:
        listaFiltro.append(palavra)
        
print(listaFiltro)
