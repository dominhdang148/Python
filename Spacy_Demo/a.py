#mô hình thống kê trong spaCy và một số thông số kỹ thuật 
# en_core_web_sm: 11MB
# en_core_web_md: 91MB
# en_core_web_lg: 789MB

#gọi thư viện ngôn ngữ spacy
from ast import MatchSequence, pattern
import spacy
nlp = spacy.load('en_core_web_sm')

# khởi tạo đối tượng nlp
doc = nlp("I go to school")

#tìm ra thành phần đường dẫn hoạt động
nlp.pipe_names

# vô hiệu hóa các thành phần của đường ống, chỉ giữ trình mã hóa hoạt động
nlp.disable_pipes('tagger','parser')
nlp.pipe_names

#tắt toàn bộ đường dẫn, chỉ mã hóa văn bản
nlp.disable_pipes('tagger','parser')

#=============================================================================
#tác vụ NLP khác nhau trong spacy
# 1. gắn thẻ Part-of-speech (POS) bằng spacy
# - cho ta biết chức năng của một từ là gì (noun, verb, adj, adv...) vầ nó được sử dụng như thế nào trong câu 
# - gắn thẻ pos là nhiệm vụ gắn thẻ tự động cho tất cả các từ của 1 câu
# - Hữ ích trong các nhiệm vụ cơ bản khác nhau trong NLP (kỹ năng tính năng, hiểu ngôn ngữ và trích xuất thông tin)

#lặp lại các mã thông báo
for token in doc:
    # in mã thông báo và phần thẻ phát biểu của nó
    print(token.text, "-->", token.pos_)
# giải thích các thẻ 
#spacy.explain()
#xuất ra màn hình
print(spacy.explain("PROPN"))

# 2. phân tích cú pháp phụ thuộc bằng spacy
# - Mỗi câu đều có cấu trúc ngữ pháp và với sự trợ giúp của phân tích cú pháp phụ thuộc, chúng ta có thể trích xuất cấu trúc này
# - xem nó như một đồ thị có hướng  với các nút tương ứng là cóc từ trong câu và các cạnh giữa các nút là các phụ thuộc tương ứng
# - Thực hiện phân tích cú pháp phụ thuộc một lần nữa khá dễ dàng trong spaCy.

# phân tích cú pháp phụ thuộc
for token in doc:
    print(token.text, "-->", token.dep_)
# thẻ phụ thuộc ROOT biểu thị động từ hoặc động từ chính trong câu
# các từ khác được kết nối trực tiếp hoặc giấn tiếp với từ ROOT của câu 
spacy.explain("ROOT")
print(spacy.explain("advmod"))

# 3, Nhận dạng đối tượng được đặt tên bằng spacy
# - thực thể là những từ hoặc nhóm từ biểu thị thông tin về những thứ phổ biến như người, địa điểm, tổ chức,...
doc = nlp("Indian spent over $71 billion on clothes in 2018")
for ent in doc.ents:
    print(ent.text, ent.label_)

spacy.explain("NORP")

# 4. đối sách dựa trên quy tắc sử dụng Spacy
# - tìm ra các từ và cụm từ trong văn bản bằng cách sử dụng các quy tắc do người dùng xác định
# * giống biểu thức chính quy trên steroid

import spacy 
nlp = spacy.load('en_core_web_sm')

#import spacy matcher
from spacy.matcher import Matcher
#initialize the matcher with the spacy vocabulary
matcher = Matcher(nlp.vocab)
doc = nlp("some people start their day with lemon water")
#define rule
pattern = [{'TEXT':'lemon'}, {'TEXT':'water'}]
#add rule
matcher.add('rule_1', none, pattern)
#matches = matcher(doc) matches
# extract matched text 
for match_id, start, end in matches:
    #get the matched span 
    mathched_span = doc[start:end]
    print(mathched_span.text)

doc1 = nlp("you read this book")
doc2 = nlp("i will book my tichet")
pattern =[{'TEXT':'book', 'POS' :'NOUN'}]
matcher = Matcher(nlp.vocab)
matcher.add('rule_2',None, pattern)