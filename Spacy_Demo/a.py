#mô hình thống kê trong spaCy và một số thông số kỹ thuật 
# en_core_web_sm: 11MB
# en_core_web_md: 91MB
# en_core_web_lg: 789MB

#gọi thư viện ngôn ngữ spacy
import spacy
nlp = spacy.load('en_core_web_sm')

# khởi tạo đối tượng nlp
doc = nlp("Tôi đi học")

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
# - cho ta biết chức năng của một từ là gì vầ nó được sử dụng như thế nào trong câu 
# - gắn thẻ pos là nhiệm vụ gắn thẻ tự động cho tất cả các từ của 1 câu
# - Hữ ích trong các nhiệm vụ cơ bản khác nhau trong NLP (kỹ năng tính năng, hiểu ngôn ngữ và trích xuất thông tin)

#lặp lại các mã thông báo
for token in doc:
    # in mã thông báo và phần thẻ phát biểu của nó
    print(token.text, "-->", token.pos_)