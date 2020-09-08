from nltk.corpus import gutenberg


file_id = input()
print(len(gutenberg.sents(file_id)))