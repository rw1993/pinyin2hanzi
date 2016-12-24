import pickle
print "loading"
bi_counts = pickle.load(open("bi_counts", "rb"))

word_counts = pickle.load(open("./word_count_dict", "rb"))

word_weights = pickle.load(open("./word_weights", "rb"))

pinyin_hanzi_map = pickle.load(open("./pinyin_hanzi_map", "rb"))

v = len([key for key in word_counts])
print "loading complete"

def bi_weight(key1, key2):
    key1_count = word_counts.get(key1, 0)
    key = ",".join([key1, key2])
    bi_count = bi_counts.get(key, 0)
    rt = float(bi_count + 1) / (key1_count + v) #lapalace
    return rt

if __name__ == "__main__":
    keys = word_counts.keys()
    print bi_weight(keys[0], keys[1])
