import pickle
import collections
import sys


wcd =  pickle.load(open("./word_count_dict", "rb"))

yuliao_words = pickle.load(open("./yuliao_words", "rb"))


sum_words_count = sum(wcd[key] for key in wcd)

v = len(wcd.keys())

# lapalace

bi_counts = {}

bi_weights= {}

for words in yuliao_words:
    for index, word in enumerate(words[:-1]):
        key = ",".join([word,words[index+1]])
        if not bi_counts.has_key(key):
            bi_counts[key] = 0
        bi_counts[key] += 1

pickle.dump(bi_counts, open("bi_counts", "wb"))
