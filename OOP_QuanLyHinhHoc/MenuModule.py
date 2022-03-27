
from os import system

from DanhSachHinhHoc import DanhSachHinhHoc
from HinhChuNhat import HinhChuNhat
from HinhTron import HinhTron
from HinhVuong import HinhVuong

features = ("Thoat chuong trinh",
            "Doc file va nhap du lieu",
            "Xem danh sach hien hanh",
            "Tim tat ca hinh vuong/hinh tron/hinh chu nhat cho chu vi X",
            "Tim tat ca hinh vuong/hinh tron/hinh chu nhat co dien tich X",
            "Tim tat ca hinh vuong/ hinh tron/ hinh chu nhat co chu vi lon nhat/nho nhat")
kieuHinh = ("Thoat",
            "Hinh Vuong",
            "Hinh Tron",
            "Hinh Chu Nhat")


def XuatMenu():
    print("===================================== HE THONG MENU =====================================")
    for feature in features:
        print(str(features.index(feature)) + ". "+feature)
    print("=========================================================================================")


def XuatKieuHinh():
    print("========================= KIEU HINH =========================")
    for hinh in kieuHinh:
        print(str(kieuHinh.index(hinh))+". " + hinh)
    print("=============================================================")


def ChonMenu(soMenu=len(features)-1, condition=0):
    menu = ""
    while True:
        system('cls')
        if condition == 0:
            XuatMenu()
        elif condition == 1:
            XuatKieuHinh()
        temp = input(
            "Xin hay nhap 1 so [0.."+str(soMenu)+"] de thuc hien chuc nang tuong ung: ")
        try:
            menu = int(temp)
            if 0 <= menu and menu <= soMenu:
                break
        except:
            print("Nhap khong hop le. Xin hay thu lai!")
            input("Nhan phim Enter de tiep tuc!")
    return menu


def XuLyMenu(menu, ds):

    system('cls')
    # region Case 0
    if features[menu] == "Thoat chuong trinh":
        print("Thoat chuong trinh")
    # endregion
    # region Case 1
    elif features[menu] == "Doc file va nhap du lieu":
        ds.DocFile("HinhHoc.txt")
        print("Nhap du lieu thanh cong! Danh sach hinh hoc hien hanh: ")
        print(ds)
    # endregion
    # region Case 2
    elif features[menu] == "Xem danh sach hien hanh":
        print(ds)
    # endregion
    # region Case 3
    elif features[menu] == "Tim tat ca hinh vuong/hinh tron/hinh chu nhat cho chu vi X":
        choose = "x"
        ketQua = DanhSachHinhHoc()
        while choose != 0:
            choose = ChonMenu(len(kieuHinh)-1, 1)
            system('cls')
            if kieuHinh[choose] == "Thoat":
                break
            elif kieuHinh[choose] == "Hinh Vuong":
                x = float(input("Xin hay nhap chu vi cua hinh vuong: "))
                ketQua = ds.TimHinhCoChuVi(x, HinhVuong)
                if len(ketQua.danhSach) != 0:
                    print("Danh sach hinh vuong co chu vi {} la: ".format(x))
                    print(ketQua)
                else:
                    print(
                        "Khong co hinh vuong co dien tich {} trong danh sach hien hanh!".format(x))
                print("Danh sach hinh hoc hien hanh:")
                print(ds)
            elif kieuHinh[choose] == "Hinh Tron":
                x = float(input("Xin hay nhap chu vi cua hinh tron: "))
                ketQua = ds.TimHinhCoChuVi(x, HinhTron)
                if len(ketQua.danhSach) != 0:
                    print("Danh sach hinh tron co chu vi {} la: ".format(x))
                    print(ketQua)
                else:
                    print(
                        "Khong co hinh tron co dien tich {} trong danh sach hien hanh!".format(x))
                print("Danh sach hinh hoc hien hanh:")
                print(ds)
            elif kieuHinh[choose] == "Hinh Chu Nhat":
                x = float(input("Xin hay nhap chu vi cua hinh chu nhat: "))
                ketQua = ds.TimHinhCoChuVi(x, HinhChuNhat)
                if len(ketQua.danhSach) != 0:
                    print("Danh sach hinh chu nhat co chu vi {} la: ".format(x))
                    print(ketQua)
                else:
                    print(
                        "Khong co hinh chu nhat co dien tich {} trong danh sach hien hanh!".format(x))
                print("Danh sach hinh hoc hien hanh:")
                print(ds)
                
            input("Nhan phim Enter de tiep tuc!")
    # endregion
    # region Case 4
    elif features[menu] == "Tim tat ca hinh vuong/hinh tron/hinh chu nhat co dien tich X":
        choose = "x"
        ketQua = DanhSachHinhHoc()
        while choose != 0:
            choose = ChonMenu(len(kieuHinh)-1, 1)
            system('cls')
            if kieuHinh[choose] == "Thoat":
                break
            elif kieuHinh[choose] == "Hinh Vuong":
                x = float(input("Xin hay nhap dien tich cua hinh vuong: "))
                ketQua = ds.TimHinhCoDienTich(x, HinhVuong)
                if len(ketQua.danhSach) != 0:
                    print("Danh sach hinh vuong co dien tich {} la: ".format(x))
                    print(ketQua)
                else:
                    print(
                        "Khong co hinh vuong co dien tich {} trong danh sach hien hanh!".format(x))
                print("Danh sach hinh hoc hien hanh:")
                print(ds)
            elif kieuHinh[choose] == "Hinh Tron":
                x = float(input("Xin hay nhap dien tich cua hinh tron: "))
                ketQua = ds.TimHinhCoDienTich(x, HinhTron)
                if len(ketQua.danhSach) != 0:
                    print("Danh sach hinh tron co dien tich {} la: ".format(x))
                    print(ketQua)
                else:
                    print(
                        "Khong co hinh tron co dien tich {} trong danh sach hien hanh!".format(x))
                print("Danh sach hinh hoc hien hanh:")
                print(ds)
            elif kieuHinh[choose] == "Hinh Chu Nhat":
                x = float(input("Xin hay nhap dien tich cua hinh chu nhat: "))
                ketQua = ds.TimHinhCCoDienTich(x, HinhChuNhat)
                if len(ketQua.danhSach) != 0:
                    print("Danh sach hinh chu nhat co dien tich {} la: ".format(x))
                    print(ketQua)
                else:
                    print(
                        "Khong co hinh chu nhat co dien tich {} trong danh sach hien hanh!".format(x))
                print("Danh sach hinh hoc hien hanh:")
                print(ds)
            input("Nhan phim Enter de tiep tuc!")
    # endregion
    # region Case 5
    elif features[menu] == "Tim tat ca hinh vuong/ hinh tron/ hinh chu nhat co chu vi lon nhat/nho nhat":
        choose = "x"
        listMin = DanhSachHinhHoc()
        listMax = DanhSachHinhHoc()
        while choose != 0:
            choose = ChonMenu(len(kieuHinh)-1, 1)
            system('cls')
            if kieuHinh[choose] == "Thoat":
                break
            elif kieuHinh[choose] == "Hinh Vuong":
                listMin = ds.TimHinhCoChuViNhoNhat(HinhVuong)
                listMax = ds.TimHinhCoChuViLonNhat(HinhVuong)
                print("Danh sach hinh vuong co chu vi nho nhat la: ")
                print(listMin)
                print("Danh sach hinh vuong co chu vi lon nhat la: ")
                print(listMax)
                print("Danh sach hinh hoc hien hanh:")
                print(ds)
            elif kieuHinh[choose] == "Hinh Tron":
                listMin = ds.TimHinhCoChuViNhoNhat(HinhTron)
                listMax = ds.TimHinhCoChuViLonNhat(HinhTron)
                print("Danh sach hinh tron co chu vi nho nhat la: ")
                print(listMin)
                print("Danh sach hinh tron co chu vi lon nhat la: ")
                print(listMax)
                print("Danh sach hinh hoc hien hanh:")
                print(ds)
            elif kieuHinh[choose] == "Hinh Chu Nhat":
                listMin = ds.TimHinhCoChuViNhoNhat(HinhChuNhat)
                listMax = ds.TimHinhCoChuViLonNhat(HinhChuNhat)
                print("Danh sach hinh chu nhat co chu vi nho nhat la: ")
                print(listMin)
                print("Danh sach hinh chu nhat co chu vi lon nhat la: ")
                print(listMax)
                print("Danh sach hinh hoc hien hanh:")
                print(ds)
            input("Nhan phim Enter de tiep tuc!")
    # endregion
    # region Case 6

    # endregion

    input("Nhan phim Enter de tiep tuc! ")
