import pickle

lexicon_lines = pickle.load(open("lexicon_lines", "rb"))

words = set()

for line in lexicon_lines:
    word = line.split()[0]
    words.add(word)
    print word

pickle.dump(words, open("words", "wb"))
