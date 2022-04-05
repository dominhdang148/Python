
from os import system
from tkinter import Menu
from traceback import print_tb

from DanhSachHinhHoc import DanhSachHinhHoc
from HinhChuNhat import HinhChuNhat
from HinhTron import HinhTron
from HinhVuong import HinhVuong

features = ("Thoat chuong trinh",
            "Doc file va nhap du lieu",
            "Xem danh sach hien hanh",
            "Tim tat ca hinh vuong/hinh tron/hinh chu nhat cho chu vi X",
            "Tim tat ca hinh vuong/hinh tron/hinh chu nhat co dien tich X",
            "Tim tat ca hinh vuong/ hinh tron/ hinh chu nhat co chu vi lon nhat/nho nhat",
            "Tim tat ca hinh vuong/ hinh tron/ hinh chu nhat co dien tich lon nhat/nho nhat",
            "Tinh tong chu vi dien tich cac hinh vuong/ hinh tron/ hinh chu nhat",
            "Dem so luong hing vuong/ hinh tron/ hinh chu nhat",
            "Sap xep danh sach hinh",
            "Tim cac hinh co chu vi lon nhat/nho nhat",
            "Tim cac hinh co dien tich lon nhat/nho nhat",
            "Xoa hinh co chu vi lon nhat/nho nhat",
            "Xoa hinh co dien tich lon nhat/nho nhat",\
            "Hien thi danh sach hinh hoc theo chieu tang/giam cua chu vi/dien tich")
kieuHinh = ("Thoat",
            "Hinh Vuong",
            "Hinh Tron",
            "Hinh Chu Nhat")
kieuSapXep = ("Thoat",
              "Sap xep theo chieu tang chu vi",
              "Sap xep theo chieu giam chu vi",
              "Sap xep theo chieu tang dien tich",
              "Sap xep theo chieu giam dien tich")
ds = DanhSachHinhHoc()


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


def XuatKieuSapXep():
    print("=================== SAP XEP DANH SACH ===================")
    for x in kieuSapXep:
        print(str(kieuSapXep.index(x))+". "+x)
    print("=========================================================")


def ChonMenu(soMenu=len(features)-1, condition=0):
    menu = ""
    while True:
        system('cls')
        if condition == 0:
            XuatMenu()
        elif condition == 1:
            XuatKieuHinh()
        elif condition == 2:
            XuatKieuSapXep()
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


def XuLyMenu(menu):
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

            elif kieuHinh[choose] == "Hinh Tron":
                x = float(input("Xin hay nhap chu vi cua hinh tron: "))
                ketQua = ds.TimHinhCoChuVi(x, HinhTron)
                if len(ketQua.danhSach) != 0:
                    print("Danh sach hinh tron co chu vi {} la: ".format(x))
                    print(ketQua)
                else:
                    print(
                        "Khong co hinh tron co dien tich {} trong danh sach hien hanh!".format(x))

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
            elif kieuHinh[choose] == "Hinh Tron":
                x = float(input("Xin hay nhap dien tich cua hinh tron: "))
                ketQua = ds.TimHinhCoDienTich(x, HinhTron)
                if len(ketQua.danhSach) != 0:
                    print("Danh sach hinh tron co dien tich {} la: ".format(x))
                    print(ketQua)
                else:
                    print(
                        "Khong co hinh tron co dien tich {} trong danh sach hien hanh!".format(x))
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
            elif kieuHinh[choose] == "Hinh Tron":
                listMin = ds.TimHinhCoChuViNhoNhat(HinhTron)
                listMax = ds.TimHinhCoChuViLonNhat(HinhTron)
                print("Danh sach hinh tron co chu vi nho nhat la: ")
                print(listMin)
                print("Danh sach hinh tron co chu vi lon nhat la: ")
                print(listMax)
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
    elif features[menu] == "Tim tat ca hinh vuong/ hinh tron/ hinh chu nhat co dien tich lon nhat/nho nhat":
        choose = "x"
        listMax = DanhSachHinhHoc()
        listMin = DanhSachHinhHoc()
        while choose != 0:
            choose = ChonMenu(len(kieuHinh)-1, 1)
            system('cls')
            if kieuHinh[choose] == "Thoat":
                break
            elif kieuHinh[choose] == "Hinh Vuong":
                listMax = ds.TimHinhVuongCoCanhLonNhat_NhoNhat(1)
                listMin = ds.TimHinhVuongCoCanhLonNhat_NhoNhat(0)
                print("Danh sach hinh vuong co canh lon nhat la: ")
                print(listMax)
                print("Danh sach hinh vuong co canh nho nhat la: ")
                print(listMin)
            elif kieuHinh[choose] == "Hinh Tron":
                listMax = ds.TimHinhTronCoBanKinhLonNhat_NhoNhat(1)
                listMin = ds.TimHinhTronCoBanKinhLonNhat_NhoNhat(0)
                print("Danh sach hinh tron co ban kinh lon nhat la: ")
                print(listMax)
                print("Danh sach hinh tron co ban kinh nho nhat la: ")
                print(listMin)
            elif kieuHinh[choose] == "Hinh Chu Nhat":
                listMax = ds.TimHinhChuNhatCoCD_CRLonNhat_NhoNhat(1)
                listMin = ds.TimHinhChuNhatCoCD_CRLonNhat_NhoNhat(0)
                print("Danh sach hinh chu nhat co chieu dai lon nhat la: ")
                print(listMax)
                print("Danh sach hinh chu nha co chỉu rong nho nhat la: ")
                print(listMin)
            print("Danh sach hinh hoc hien hanh:")
            print(ds)
            input("Nhan phim Enter de tiep tuc!")
    # endregion
    # region Case 7
    elif features[menu] == "Tinh tong chu vi dien tich cac hinh vuong/ hinh tron/ hinh chu nhat":
        choose = "x"
        resultP = 0
        resultS = 0
        while choose != 0:
            choose = ChonMenu(len(kieuHinh)-1, 1)
            system('cls')
            if kieuHinh[choose] == "Thoat":
                break
            elif kieuHinh[choose] == "Hinh Vuong":
                resultP = ds.TinhTongChuViHinh(HinhVuong)
                resultS = ds.TinhTongDienTichHinh(HinhVuong)
                print(
                    "Tong chu vi tat ca hinh vuong trong danh sach la: {}".format(resultP))
                print(
                    "Tong dien tich tat ca hinh vuong trong danh sach la: {}".format(resultS))
            elif kieuHinh[choose] == "Hinh Tron":
                resultP = ds.TinhTongChuViHinh(HinhTron)
                resultS = ds.TinhTongDienTichHinh(HinhTron)
                print(
                    "Tong chu vi tat ca hinh tron trong danh sach la: {}".format(resultP))
                print(
                    "Tong dien tich tat ca hinh tron trong danh sach la: {}".format(resultS))
            elif kieuHinh[choose] == "Hinh Chu Nhat":
                resultP = ds.TinhTongChuViHinh(HinhChuNhat)
                resultS = ds.TinhTongDienTichHinh(HinhChuNhat)
                print(
                    "Tong chu vi tat ca hinh chu nhat trong danh sach la: {}".format(resultP))
                print(
                    "Tong dien tich tat ca hinh chu nhat trong danh sach la: {}".format(resultS))
            print("Danh sach hinh hoc hien hanh:")
            print(ds)
            input("Nhan phim Enter de tiep tuc!")
    # endregion
    # region Case 8
    elif features[menu] == "Dem so luong hing vuong/ hinh tron/ hinh chu nhat":
        choose = "x"
        ketQua = 0
        while choose != 0:
            choose = ChonMenu(len(kieuHinh)-1, 1)
            system('cls')
            if kieuHinh[choose] == "Thoat":
                break
            elif kieuHinh[choose] == "Hinh Vuong":
                ketQua = ds.DemSoLuongHinh(HinhVuong)
                print("So luong hinh vuong co tronh danh sach la: {}".format(ketQua))
            elif kieuHinh[choose] == "Hinh Tron":
                ketQua = ds.DemSoLuongHinh(HinhTron)
                print("So luong hinh tron co tronh danh sach la: {}".format(ketQua))
            elif kieuHinh[choose] == "Hinh Chu Nhat":
                ketQua = ds.DemSoLuongHinh(HinhChuNhat)
                print("So luong hinh chu nhat co tronh danh sach la: {}".format(ketQua))
            print("Danh sach hinh hoc hien hanh:")
            print(ds)
            input("Nhan phim Enter de tiep tuc!")
    # endregion
    # region Case 9
    elif features[menu] == "Sap xep danh sach hinh":
        choose = "x"
        while choose != 0:
            choose = ChonMenu(len(kieuSapXep)-1, 2)
            system('cls')
            if kieuSapXep[choose] == "Thoat":
                break
            elif kieuSapXep[choose] == "Sap xep theo chieu tang chu vi":
                print("Danh sach hinh hoc hien hanh:")
                print(ds)
                input("Nhan 1 phim bat ky de sap xep danh sach hinh theo chieu tang chu vi")
                system('cls')
                ds.SapXepHinhTheoChuVi()
            elif kieuSapXep[choose] == "Sap xep theo chieu giam chu vi":
                print("Danh sach hinh hoc hien hanh:")
                print(ds)
                input("Nhan 1 phim bat ky de sap xep danh sach hinh theo chieu giam chu vi")
                system('cls')
                ds.SapXepHinhTheoChuVi(True)
            elif kieuSapXep[choose] == "Sap xep theo chieu tang dien tich":
                print("Danh sach hinh hoc hien hanh:")
                print(ds)
                input("Nhan 1 phim bat ky de sap xep danh sach hinh theo chieu tang dien tich")
                system('cls')
                ds.SapXepHinhTheoDienTich()
                print("Sap xep thanh cong! Danh sach hinh hoc sau khi sap xep: ")
                print(ds)
            elif kieuSapXep[choose] == "Sap xep theo chieu giam dien tich":
                print("Danh sach hinh hoc hien hanh:")
                print(ds)
                input("Nhan 1 phim bat ky de sap xep danh sach hinh theo chieu tang dien tich")
                system('cls')
                ds.SapXepHinhTheoDienTich()
                print("Sap xep thanh cong! Danh sach hinh hoc sau khi sap xep: ")
                print(ds)
            print("Danh sach hinh hoc sau khi sap xep:")
            print(ds)
            input("Nhan phim Enter de tiep tuc")
     # endregion
    # region Case 10
    elif features[menu]=="Tim cac hinh co chu vi lon nhat/nho nhat":
        listMax=ds.TimHinhCoChuViLonNhat()
        listMin=ds.TimHinhCoChuViNhoNhat()
        print("Danh sach hinh co chu vi lon nhat la:")
        print(listMax)
        print("Danh sach hinh co chu vi nho nhat la:")
        print(listMin)
        print("Danh sach hinh hoc hien hanh:")
        print(ds)
    # endregion
    # region Case 11
    elif features[menu]=="Tim cac hinh co dien tich lon nhat/nho nhat":
        listMax=ds.TimHinhCoDienTichLonNhat()
        listMin=ds.TimHinhCoDienTichNhoNhat()
        print("Danh sach hinh co dien tich lon nhat la:")
        print(listMax)
        print("Danh sach hinh co dien tich nho nhat la:")
        print(listMin)
        print("Danh sach hinh hoc hien hanh:")
        print(ds)
    # endregion
    # region Case 12
    elif features[menu]=="Xoa hinh co chu vi lon nhat/nho nhat":
        print("Danh sach hinh hoc hien hanh: ")
        print(ds)
        input("Nhan phim Enter de xoa hinh co chu vi lon nhat va nho nhat!")
        system('cls')
        ds.XoaHinhCoChuViLonNhat_NhoNhat(0)
        ds.XoaHinhCoChuViLonNhat_NhoNhat(1)
        print("Da xoa thanh cong! Danh sach hinh hoc hien hanh: ")
        print(ds)
    # endregion
    # region Case 13
    elif features[menu]=="Xoa hinh co dien tich lon nhat/nho nhat":
        print("Danh sach hinh hoc hien hanh: ")
        print(ds)
        input("Nhan phim Enter de xoa hinh co dien tich lon nhat va nho nhat!")
        system('cls')
        ds.XoaHinhCoDienTichLonNhat_NhoNhat(0)
        ds.XoaHinhCoDienTichLonNhat_NhoNhat(1)
        print("Da xoa thanh cong! Danh sach hinh hoc hien hanh: ")
        print(ds)
    # endregion
    # region Case 14
    elif features[menu]=="Hien thi danh sach hinh hoc theo chieu tang/giam cua chu vi/dien tich":
        choose = "x"
        while choose != 0:
            choose = ChonMenu(len(kieuSapXep)-1, 2)
            system('cls')
            if kieuSapXep[choose] == "Thoat":
                break
            elif kieuSapXep[choose] == "Sap xep theo chieu tang chu vi":
                ketQua=ds.HienThiTatCaCacHinhTheoChuVi()
                print("Danh sach hinh hoc theo chieu tang chu vi: ")
            elif kieuSapXep[choose] == "Sap xep theo chieu giam chu vi":
                ketQua=ds.HienThiTatCaCacHinhTheoChuVi(True)
                print("Danh sach hinh hoc theo chieu giam chu vi: ")
            elif kieuSapXep[choose] == "Sap xep theo chieu tang dien tich":
                ketQua=ds.HienThiTatCaCacHinhTheoDienTich()
                print("Danh sach hinh hoc theo chieu tang dien tich: ")
            elif kieuSapXep[choose] == "Sap xep theo chieu giam dien tich":
                ketQua=ds.HienThiTatCaCacHinhTheoDienTich(True)
                print("Danh sach hinh hoc theo chieu giam dien tich: ")
            print(ketQua)
            input("Nhan phim Enter de tiep tuc")
    # endregion
    input("Nhan phim Enter de tiep tuc! ")
    