# -*- coding: utf-8 -*-
"""
word detect moudle
created by gln 20180330
"""

import nltk
from nltk.corpus import words
import logging
from correct import correct

nltk.download('punkt')
nltk.download("words")


def judge_word(sentence):
    """
    :param sentence:
    :return:
    """

    tokens = nltk.word_tokenize(sentence)
    logging.debug(tokens)

    flag_list=[]
    for word in tokens:
        flag = word in words.words()
        flag_list.append(flag)
    return tokens, flag_list

def main():

    test = "agc would is going to famaly 2 3 verygood u know 实现 , ."
    tokens, flag_list = judge_word(test)

    for i,item in enumerate(tokens):
       if flag_list[i]:
          logging.info("{} is a word".format(item))
       else:
          logging.info("{} is not a word, may be {}".format(item, correct(item)))

if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG)
    main()
