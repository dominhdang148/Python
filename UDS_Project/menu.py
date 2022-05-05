from os import system
menuList = (
    'Thoát chương trình',
    'Phân tích cú pháp',
    'Gán nhãn thực thể có tên',
    'Phân loại văn bản',
    'Phân tích cảm xúc'
)


def XuatMenu():
    print('======================================== XỬ LÝ NGÔN NGỮ TỰ NHIÊN ========================================')
    for menu in menuList:
        print(str(menuList.index(menu))+' '+menu)
    print('=========================================================================================================')


def ChonMenu(SoMenu=len(menuList)-1):
    menu = ''
    while True:
        system('cls')
        XuatMenu()
        temp = input('Xin hãy nhập 1 số để chọn chức năng tương ứng: ')
        try:
            menu=int(temp)
            if 0<= menu & menu<=SoMenu:
                break
        except:
            print("Lệnh nhập không hợp lệ!")
            print("Nhấn phím Enter để tiếp tục!")
    return menu
