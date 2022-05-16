# from joblib import PrintTime
# import nltk #import nltk
# #============
# #MÃ HÓA
# # chia nhỏ văn bản theo từng từ hoặc từng câu một cách thuận tiện
# #-->các phần văn bản nhỏ hơn mà vẫn tương đối mạch lạc và có ý nghĩa ngay cả khi nằm ngoài ngữ cảnh
# #Mã hóa bằng từ: cho phép bạn xác định các từ xuất hiện đặc biệt thường xuyên
# #Mã hóa theo câu: bạn có thể phân tích cách các từ đó liên quan với nhau và xem thêm ngữ cảnh
# from nltk.tokenize import sent_tokenize, word_tokenize
# example_string = """
# Hello, Trang. How's it going,pretty good! Today I have maths, english and PE. """
# # chia nhỏ đoạn thành từng câu
# print(sent_tokenize(example_string))
# print(word_tokenize(example_string))
# #--> các dấu câu nó cũng xét là 1 từ riêng
# #====================================
# #LỌC CÁC KÝ TỰ ĐẶC BIỆT (DẤU CÂU)
# import string
# result = string.punctuation
# Sentence = "Hey, Geeks !, How are you?"
# for i in Sentence:
#        if i in string.punctuation:
#         print("Punctuation: " + i)
# #====================================
# #LỌC CÁC TỪ ĐÃ DỪNG (Filtering Stop Words)
# # từ dừng:  là những từ mà bạn muốn bỏ qua, vì vậy bạn lọc chúng ra khỏi văn bản khi xử lý
# nltk.download("stopwords")
# #nltk.download('wordnet', quiet=True)
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# worf_quote = "Sir, I protest. I am not a merry man!"
# #mã hóa từng từ sau đó lưu trong words_in_quote
# words_in_quote = word_tokenize(worf_quote)
# words_in_quote
# stop_words = set(stopwords.words("english"))
# #print(stop_words, "\n")
# filtered_list = []
# for word in words_in_quote:
#    if word.casefold() not in stop_words:
#         filtered_list.append(word)
#         filtered_list = [
#       word for word in words_in_quote if word.casefold() not in stop_words
#     ]
#         print(filtered_list)
# #====================================
# #TẠO GỐC(Stemming)
# #tác vụ xử lý văn bản, trong đó bạn giảm bớt các từ xuống gốc , là phần cốt lõi của một từ
# from nltk.stem import PorterStemmer
# words=['write','writer','writing','writers'] # khai báo 1 array gồm 4 phần từ
# ps=PorterStemmer() # tạo mới đối tượng PorterStemmer()
# for word in words: #chạy vòng for
#     print(f"{word}: {ps.stem(word)}")# in ra từng word
# from nltk.tokenize import word_tokenize
# stemmer = PorterStemmer()
# string_for_stemming = """
# The crew of the USS Discovery discovered many discoveries.
# Discovering is what explorers do."""
# words = word_tokenize(string_for_stemming)
# stemmed_words = [stemmer.stem(word) for word in words]
# print(stemmed_words)
# #===================================
# #BỔ NGỮ (Lemmatizing)
# # Việc bổ sung Python cho phép chúng ta nhóm các dạng từ được tổng hợp lại với nhau. Nó liên kết các từ có nghĩa tương tự với một từ và ánh xạ các từ khác nhau vào một gốc.
# #làm giảm các từ về nghĩa cốt lõi của chúng, nhưng nó sẽ cung cấp cho bạn một từ tiếng Anh hoàn chỉnh có nghĩa của riêng nó
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# lemmatizer.lemmatize("scarves")
# string_for_lemmatizing = "The friends of DeSoto love scarves."
# text_ex = word_tokenize(string_for_lemmatizing)
# print(text_ex)
# lemmatized_words = [lemmatizer.lemmatize(word) for word in text_ex]
# print(lemmatized_words)
# #=======================================
# #GẮN THẺ (Part of speech - POS)
# # cho biết  vai trò của các từ khi bạn sử dụng chúng cùng nhau trong câu
# from nltk.tokenize import word_tokenize
# sagan_quote = """
# If you wish to make an apple pie from scratch,
# you must first invent the universe."""
# words_in_sagan_quote = word_tokenize(sagan_quote)
# words_in_sagan_quote
# import nltk
# nltk.pos_tag(words_in_sagan_quote)
# #nltk.help.upenn_tagset()
# jabberwocky_excerpt = """
# 'I go to school."""
# words_in_excerpt = word_tokenize(jabberwocky_excerpt)
# print(nltk.pos_tag(words_in_excerpt))
# #=======================================
# #CHUNKING
# # phân đoạn cho phép bạn xác định các cụm từ
# from nltk.tokenize import word_tokenize
# lotr_quote = "It's a dangerous business, Frodo, going out your door."
# words_in_lotr_quote = word_tokenize(lotr_quote)
# print(words_in_lotr_quote)
# lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
# print(lotr_pos_tags)
# #Tạo ngữ pháp phân đoạn 
# grammar = "NP: {<DT>?<JJ>*<NN>}"
# chunk_parser = nltk.RegexpParser(grammar)
# tree = chunk_parser.parse(lotr_pos_tags)
# #print(tree.draw())
# #======================================
# #CHINKING
# #Chinking được sử dụng cùng với chunking, nhưng trong khi chunking được sử dụng để bao gồm một mẫu, thì chinking được sử dụng để loại trừ một mẫu.
# lotr_pos_tags
# grammar = """
# Chunk: {<.*>+}
#        }<JJ>{"""
# chunk_parser = nltk.RegexpParser(grammar)
# tree = chunk_parser.parse(lotr_pos_tags)
# #print(tree.draw())
# #=====================================
# #SỬ DỤNG NHẬN DẠNG ĐỐI TƯỢNG ĐẶT TÊN (NER)

# #=====================================
# #PHÂN TÍCH VĂN BẢN
# #NLTK cung cấp một số kho tài liệu bao gồm mọi thứ, từ tiểu thuyết
# #nltk.download("book")
# from nltk.book import *
# #Concordance
# #Cung cấp cho bạn cái nhìn về cách một từ đang được sử dụng ở cấp độ câu và những từ nào được sử dụng với nó
# text8.concordance("man")
# text8.concordance("woman")
#Việc nhúng vào một kho ngữ liệu có sự phù hợp sẽ không cung cấp cho bạn bức tranh đầy đủ, nhưng vẫn có thể thú vị khi xem qua và xem có điều gì nổi bật hay không.
#=================================
#TÌM TỪ ĐỒNG NGHĨA, TỪ TRÁI NGHĨA
#từ đồng nghĩa
from nltk.corpus import wordnet
syn=wordnet.synsets('cat')
print(syn)

#không có từ trái nghĩa
from nltk.corpus import wordnet
antonyms=[]
for syn in wordnet.synsets('depressed'):
        for l in syn.lemmas():
                 if l.antonyms():
                          antonyms.append(l.antonyms()[0].name())
antonyms
print(antonyms)
#có thừ trái nghĩa
for syn in wordnet.synsets('good'):
        for l in syn.lemmas():
                  if l.antonyms():
                            antonyms.append(l.antonyms()[0].name())
antonyms
print(antonyms)