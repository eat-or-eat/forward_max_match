# 因为短小的预料无法明显的看出不同前相匹配的时间优化效果，本脚本用于生成较长的预料
import random  # random比numpy快


def load_dict(path):
    words, chars = set(), set()
    with open(path, encoding='utf8') as f:
        for line in f:
            word = line.split()[0]
            words.add(word)
            for char in word:
                chars.add(char)
    return words, chars


# words, chars = load_dict('./small_dict.txt')

def generate_corpus(row, col, dict_path='./small_dict.txt', corpus_path='./corpus.txt'):
    words, chars = load_dict(dict_path)
    words = list(words)
    chars = list(chars)
    output = open(corpus_path, 'w', encoding='utf8')
    for i in range(row):
        sentence = ''
        for j in range(col):
            if random.random() > 0.2:
                sentence += random.choice(words)
            else:
                sentence += random.choice(chars)
        output.write(sentence + '\n')
        print(sentence)
    output.close()


if __name__ == '__main__':
    generate_corpus(100, 100)
