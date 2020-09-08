from nltk.corpus import movie_reviews

file_id = input()
print(movie_reviews.words(file_id)[:6])