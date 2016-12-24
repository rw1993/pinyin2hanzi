import tool
import sys
import copy
pinyins = sys.argv[1:]

print pinyins

possible_splits = []


def all_possible_split(pys, already):
    if len(pys) == 0:
        possible_splits.append(already)
        return
    for index, py in enumerate(pys):
        all_possible_split(pys[index+1:], already+[pys[:index+1]])

all_possible_split(pinyins, [])
print possible_splits


def possible_word(pinyin):
    try:
        return tool.pinyin_hanzi_map[tuple(pinyin)]
    except:
        return []




def answer_from_split(split):
    answer = []
    words_list = map(possible_word, split)
    tmp_answer = []
    def reduce_get_answer(words_list, index, tmp_answer):
        new_answer = set()
        if index == 0:
            for w in words_list[0]:
                new_answer.add(w)
        else:
            for w in words_list[index]:
                for answer in tmp_answer:
                    new_answer.add(answer+" "+w)
        return new_answer

    tmp_answer = set()
    for index in range(len(words_list)):
        tmp_answer = reduce_get_answer(words_list, index, tmp_answer)
    return tmp_answer


all_possible_answers = reduce(lambda x,y: x.union(y),
                              map(answer_from_split,
                                  possible_splits))



def get_answer_weights(answer):
    words = answer.split()
    w = 1.0
    for index, word in enumerate(words[:-1]):
        if index == 0:
            w *= tool.word_weights[word]
        w *= tool.bi_weight(word, words[index+1])
    return w

sorted_answers = sorted(all_possible_answers, key=get_answer_weights,
                        reverse=True)

print "\n".join(sorted_answers[:20])
