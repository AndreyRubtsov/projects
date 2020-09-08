from nltk.stem import PorterStemmer


sent = input().split()

lancaster = PorterStemmer()
for word in sent:
    print(lancaster.stem(word))