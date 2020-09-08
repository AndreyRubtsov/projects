from nltk.corpus import treebank

file_id = input()
print(treebank.tagged_words(file_id)[0])
