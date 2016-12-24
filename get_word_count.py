import pickle

words = pickle.load(open("words", "rb"))
yuliao_lines = pickle.load(open("yuliao_lines", "rb"))
word_count = {word: 0 for word in words}
yuliao_words = []
for line in yuliao_lines:
    words_this_line = []
    line = line.strip()
    def split_word(line):
        pre_line = line
        if len(line) == 0:
            return 
        while line not in words:
            line = line[:-1]
            if len(line) == 0:
                break
        if len(line) == 0:
            return
        else:
            word_count[line] += 1
            words_this_line.append(line)
            split_word(pre_line[len(line):])
    split_word(line)
    yuliao_words.append(words_this_line)

for key in word_count:
    print key.encode("utf-8"), word_count[key]

pickle.dump(word_count, open("word_count_dict", "wb"))
pickle.dump(yuliao_words, open("yuliao_words", "wb"))


