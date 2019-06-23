import re

def generate_ngrams(sentence, n):
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-zA-Z0-9\s]', ' ', sentence)
    
    tokens = [token for token in sentence.split(" ") if token != " "]
    ngrams = zip(*[tokens[i:] for i in range(n)])

    return [" ".join(ngram) for ngram in ngrams]
