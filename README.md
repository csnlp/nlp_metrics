NLP 对话领域的常用自动评价指标

## BLEU
关于BLEU的讲解:[BLEU](https://csnlp.github.io/2019/02/13/nlp-metrics/#more)
关于BLEU的代码:[BLEU](https://github.com/csnlp/nlp_metrics/blob/master/bleu.py)
相关依赖: [nltk](https://www.nltk.org/)
使用方法:
```python
import bleu

from bleu import cal_bleu

# sentence: a str separated by space; e.g. "Hello World."
# references: a list of sentences: e.g. ["Hello Me", "Good World"]
# weights: a list of number which be summed together is 1; [0.1, 0.2, 0.3, 0.4]. This is for BLEU-4
  The weight for unigram, bigram, 3-gram, 4-gram is [0.1, 0.2, 0.3, 0.4]

BLEU-SCORE = cal_bleu(sentence, references, weights)
```
## ROUGE
+ 

## DISTINCT
distinct is firstly proposed by Jiwei Li et.al in paper <A Diversity-Promoting Objective Function for Neural Conversation Models> for the diversity evaluation of generated responses. 

