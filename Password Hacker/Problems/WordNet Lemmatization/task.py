from nltk.stem import WordNetLemmatizer

sent = input()

lancaster = WordNetLemmatizer()
print(lancaster.lemmatize(sent, pos='n'))
print(lancaster.lemmatize(sent, pos='a'))
print(lancaster.lemmatize(sent, pos='v'))
