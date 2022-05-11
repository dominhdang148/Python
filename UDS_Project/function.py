import underthesea as uds
import numpy as np

def TachTu(sentence):
    return np.array(uds.word_tokenize(sentence))
def GanNhanPOS(sentence):
    return np.array(uds.pos_tag(sentence))
def GanNhanChunking(sentence):
    return np.array(uds.chunk(sentence))
def GanNhanThucThe(sentence):
    return np.array(uds.ner(sentence))
def PhanLoaiVB(sentence):
    return np.array(uds.classify(sentence))
