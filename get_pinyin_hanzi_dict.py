import pickle

lexicon_lines = pickle.load(open("./lexicon_lines", "rb"))

pinyin_hanzi_map = {}

for line in lexicon_lines:
    lines = line.split()
    print lines
    hanzi = lines[0]
    pinyins = lines[1:]
    pinyins = map(lambda x: x[:-1], pinyins)
    pinyins = tuple(pinyins)
    if not pinyin_hanzi_map.has_key(pinyins):
        pinyin_hanzi_map[pinyins] = []
    pinyin_hanzi_map[pinyins].append(hanzi)

pickle.dump(pinyin_hanzi_map, open("pinyin_hanzi_map", "wb"))
