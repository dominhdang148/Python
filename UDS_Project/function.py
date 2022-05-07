import underthesea as uds
import numpy as np

def TachTu(sentence):
    return np.array(uds.word_tokenize(sentence))
