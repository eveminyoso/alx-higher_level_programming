#!/usr/bin/python3
def multiple_returns(sentence):
    sentence = tuple((sentence))
    if len(sentence) == 0:
        return 0, None
    len_ = len(sentence)
    return len_, sentence[0]
