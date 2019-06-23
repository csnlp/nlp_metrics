from itertools import chain

from utils import generate_ngrams

def distinct(lines, N):
    ngrams = [generate_ngrams(line, N) for line in lines]
    ngrams_set = set(chain.from_iterable(ngrams))

    return float(len(ngrams_set)) / sum(len(ngram) for ngram in ngrams)

def read_lines(filename):
    fr = open(filename, 'r')
    lines = fr.readlines()
    fr.close()
    return lines

if __name__ == "__main__":
    #lines = ["hello world", "this new", "hello world"]
    lines = read_lines('test.txt')
    print(distinct(lines, 2))

