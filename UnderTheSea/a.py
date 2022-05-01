
# Thêm thư viện docx

from docx import Document
from os import system
import underthesea as uds
import numpy as np
# Tạo một đối tượng là 1 file word:

system('cls')
doc = open("Demo.docx", "rb")

# Tạo một đối tượng đọc file word trên:

document = Document(doc)

# Tạo một biến docu là 1 chuỗi trống. Chuỗi này sẽ lưu từng đoạn (paragraph) của văn bản word trên.

docu = ""
for para in document.paragraphs:
    docu += para.text+'\n'

# Tách đoạn văn bản thành các câu.

sentence_List = uds.sent_tokenize(docu)

# Tách từng câu thành các từ.
word_List = []
for s in sentence_List:
    word_List.append(uds.word_tokenize(s))
# fullsentence=uds.word_tokenize(docu, format='text')
# # In kết quả thu được:

print("=========================================================================== KẾT QUẢ PHÂN TÍCH VĂN BẢN ===========================================================================")

print("Các câu có trong đoạn văn bản là: \n")
sentence_List = np.array(sentence_List)
for sentence in sentence_List:
    print('\t'+sentence)

print("\nCác từ trong từng câu là:\n")

word_List = np.array(word_List, dtype='object')
for sentence in word_List:
    print('\t',end="")
    for word in sentence:
        print(word, end=" | ")
    print('\n', end="")

print("\n=================================================================================================================================================================================")

input("Nhấn 1 phím bất kỳ để tiếp tục!!!")
