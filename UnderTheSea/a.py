
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
word_List = uds.word_tokenize(docu)
# Gắn nhãn POS cho các từ trong câu
pos_tag_List=uds.pos_tag(docu)

# In kết quả thu được:

print("\t\tKÊT QUẢ PHÂN TÍCH VĂN BẢN")

print("Các câu có trong đoạn văn bản là: \n")
sentence_List = np.array(sentence_List)
for sentence in sentence_List:
    print('\t'+sentence)

print("\nCác từ có trong đoạn văn bản là: \n")
word_List = np.array(word_List)
for word in word_List:
    print(word)

print("\nCác từ trong đoạn văn với nhãn POS tương ứng là: ")
pos_tag_List= np.array(pos_tag_List)
for word in pos_tag_List:
    print(word[0]+'-->'+word[1])
input("\nNhấn 1 phím bất kỳ để tiếp tục!!!")