from nltk.corpus import brown

file_id = input()
print(brown.fileids(categories=file_id)[:3])