# Thêm thư viện docx

from docx import Document
from os import system

# Tạo một đối tượng là 1 file word:

system('cls')
doc = open("Demo.docx", "rb")

# Tạo một đối tượng đọc file word trên:

document = Document(doc)

# Tạo một biến docu là 1 chuỗi trống. Chuỗi này sẽ lưu từng đoạn (paragraph) của văn bản word trên.

docu = ""
for para in document.paragraphs:
    docu += para.text+'\n'

# In kết quả thu được:

print(docu)
