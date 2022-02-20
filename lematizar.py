from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
lemmatizer = WordNetLemmatizer()

l = lemmatizer.lemmatize("scarves")

string_for_lemmatizing = "The friends of DeSoto love scarves."

words = word_tokenize(string_for_lemmatizing)

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

print(lemmatized_words)