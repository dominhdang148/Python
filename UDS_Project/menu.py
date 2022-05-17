from os import system
import function as f
import refdict as r


class MenuClass:
    menuList = (
        'Thoát chương trình',
        'Phân tích cú pháp (Tiếng Việt)',
        'Gán nhãn thực thể có tên (Tiếng Việt)',
        'Tìm từ đồng nghĩa (Tiếng Anh)',
        'Tìm từ trái nghĩa (Tiếng Anh)'
    )
    text = ""

    def __init__(self):
        pass

    def XuatMenu(self):
        print('======================================== XỬ LÝ NGÔN NGỮ TỰ NHIÊN ========================================')
        for menu in self.menuList:
            print(str(self.menuList.index(menu))+'. '+menu)
        print('=========================================================================================================')

    def ChonMenu(self, SoMenu=len(menuList)-1):
        menu = ''
        while True:
            system('cls')
            self.XuatMenu()
            temp = input('Xin hãy nhập 1 số để chọn chức năng tương ứng: ')
            try:
                menu = int(temp)
                if 0 <= menu and menu <= SoMenu:
                    break
                else:
                    print("Lệnh nhập không hợp lệ")
                    input("Nhấn phím Enter để tiếp tục!")
            except:
                print("Lệnh nhập không hợp lệ!")
                input("Nhấn phím Enter để tiếp tục!")
        return menu

    def XuLyMenu(self, menu):
        system('cls')
        # region Case 0
        if self.menuList[menu] == "Thoát chương trình":
            print("Thoát chương trình")
        # endregion
        # region Case 1
        elif self.menuList[menu] == "Phân tích cú pháp (Tiếng Việt)":
            print("Phân tích cú pháp (Tiếng Việt)")
            self.text = input("Xin hãy nhập 1 câu tiếng Việt: ")
            result = f.TachTu(self.text)
            print("========================================================")
            print("Các từ có trong câu trên là: ")
            for word in result:
                print(word)
            print("========================================================")
            print("Các từ với nhãn POS tương ứng: ")
            result = f.GanNhanPOS(self.text)
            for word in result:
                print(word[0]+' --> ' + word[1]+' --> '+r.pos_Dict[word[1]])
            print("========================================================")
            print("Các từ với nhãn Chunking tương ứng: ")
            result = f.GanNhanChunking(self.text)
            for word in result:
                print(word[0] + ' --> ' + word[2]+' --> '+r.chunk_Dict[word[2]])
        # endregion
        # region Case 2
        elif self.menuList[menu] == "Gán nhãn thực thể có tên (Tiếng Việt)":
            print("Gắn nhãn thực thể có tên (Tiếng Việt)")
            self.text = input("Xin hãy nhập 1 câu tiếng Việt: ")
            result=f.GanNhanThucThe(self.text)
            print("Các thực thể có tên của câu trên: ")
            for word in result:
                if(word[3]!='O'):
                    print(word[0] +' --> '+ r.name_Dict[word[3]])
        # endregion ``
        # region Case 3
        elif self.menuList[menu] == "Tìm từ đồng nghĩa (Tiếng Anh)":
            print("Tìm từ đồng nghĩa (Tiếng Anh)")
            self.text = input("Xin hãy nhập 1 từ tiếng Anh: ")
            result=f.TimTuDongNghia(self.text)
            print("Các từ đồng nghĩa của từ '"+self.text+"' là: ")
            for word in result:
                print(word)
        # endregion
        # region Case 4
        elif self.menuList[menu] == "Tìm từ trái nghĩa (Tiếng Anh)":
            print("Tìm từ trái nghĩa (Tiếng Anh)")
            self.text = input("Xin hãy nhập 1 từ tiếng Anh: ")
            result=f.TimTuTraiNghia(self.text)
            print("Các từ trái nghĩa của từ '"+self.text+"' là: ")
            for word in result:
                print(word)
        # endregion
        input('\nNhấn phím Enter để tiếp tục')