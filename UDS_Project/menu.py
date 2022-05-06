from os import system
class MenuClass:
    menuList = (
        'Thoát chương trình',
        'Phân tích cú pháp',
        'Gán nhãn thực thể có tên',
        'Phân loại văn bản',
        'Phân tích cảm xúc'
    )
    def __init__(self):
        pass

    def XuatMenu(self):
        print('======================================== XỬ LÝ NGÔN NGỮ TỰ NHIÊN ========================================')
        for menu in self.menuList:
            print(str(self.menuList.index(menu))+'. '+menu)
        print('=========================================================================================================')


    def ChonMenu(self,SoMenu=len(menuList)-1):
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


    def XuLyMenu(self,menu):
        system('cls')
        # region Case 0
        if self.menuList[menu] == "Thoát chương trình":
            print("Thoát chương trình")
        # endregion
        # region Case 1
        elif self.menuList[menu] == "Phân tích cú pháp":
            print("Phân tích cú pháp")
        # endregion
        # region Case 2
        elif self.menuList[menu] == "Gán nhãn thực thể có tên":
            print("Gắn nhãn thực thể có tên")
        # endregion
        # region Case 3
        elif self.menuList[menu] == "Phân loại văn bản":
            print("Phân loại văn bản")
        # endregion
        # region Case 4
        elif self.menuList[menu] == "Phân tích cảm xúc":
            print("Phân tích cảm xúc")
        # endregion
        input('Nhấn phím Enter để tiếp tục')
