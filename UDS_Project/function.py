import underthesea as uds
import numpy as np
from nltk.corpus import wordnet

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
def TimTuDongNghia(word):
    synonyms=[]
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return np.array(synonyms)
def TimTuTraiNghia(word):
    antonyms=[]
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
                 if l.antonyms():
                        antonyms.append(l.antonyms()[0].name())
    return np.array(antonyms)