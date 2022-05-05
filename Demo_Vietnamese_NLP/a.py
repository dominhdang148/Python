
# Thêm thư viện docx

from docx import Document
from os import system
import underthesea as uds
import numpy as np
# Tạo một đối tượng là 1 file word:

#  system('chcp 65001')  # Chỉnh console sang chế độ gõ tiếng Việt
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
pos_tag_List = uds.pos_tag(docu)
# Gắn nhãn chunking
chunking_List = uds.chunk(docu)
# Gắn hãn
# In kết quả thu được:

print("\t\tKÊT QUẢ PHÂN TÍCH VĂN BẢN")

print("Các câu có trong đoạn văn bản là: \n")
sentence_List = np.array(sentence_List)
for sentence in sentence_List:
    print('\t'+sentence)

print("\nCác từ có trong đoạn văn bản là: \n")
word_List = np.array(word_List)
for word in word_List:
    print('\t'+word)

print("\nCác từ trong đoạn văn với nhãn POS tương ứng là: ")
pos_tag_List = np.array(pos_tag_List)
for word in pos_tag_List:
    print('\t'+word[0]+'-->'+word[1])
print("\nCác từ trong đoạn văn với nhãn chunking tương ứng là:")
chunking_List = np.array(chunking_List)
for word in chunking_List:
    print('\t'+word[0]+'-->'+word[2])

input("\nNhấn 1 phím bất kỳ để tiếp tục!!!")
