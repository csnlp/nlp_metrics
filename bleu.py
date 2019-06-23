# reference code: https://github.com/vikasnar/Bleu/blob/master/calculatebleu.py 
# reference code: http://www.nltk.org/_modules/nltk/align/bleu_score.html
import math

import nltk
from nltk.util import ngrams
from nltk import word_tokenize
from nltk import Counter

def cal_bleu(candidate, references, weights):
    precision_ns = (modified_precision(candidate, references, i) for i, weight in enumerate(weights, start=1))
    
    # Why Try: if certain precision_n is 0, the log(precision_n) will return a ValueError
    try:
        s = math.fsum(weight * math.log(precision_n) for weight, precision_n in zip(weights, precision_ns))
    except ValueError:
        return 0
    bp = brevity_penalty(candidate, references)

    return bp * math.exp(s)
        

def modified_precision(candidate, references, n):
    candidate_counter = Counter(get_ngrams(candidate, n))
    if not candidate_counter:
        return 0

    max_reference_counter = {}
    for reference in references:
        reference_counter = Counter(get_ngrams(reference, n))
        for ngram in candidate_counter:
            max_reference_counter[ngram] = max(max_reference_counter.get(ngram, 0), reference_counter[ngram])

    clipped_counter = dict((ngram, min(reference_counter_count, max_reference_counter[ngram])) for ngram, reference_counter_count in reference_counter.items())
    return sum(clipped_counter.values()) / sum(candidate_counter.values())


def brevity_penalty(candidate, references):
    len_reference = min(len(reference) for reference in references)
    len_candidate = len(candidate)
    if len_candidate > len_reference:
        return 1
    else:
        return math.exp(1 - float(len_reference)/float(len_candidate))



def get_ngrams(sentence, n):
    phases = word_tokenize(sentence)
    n_grams = ngrams(sentence, n)
    return n_grams

if __name__ == '__main__':
    print cal_bleu('hello word', ['hello word'], [1])
