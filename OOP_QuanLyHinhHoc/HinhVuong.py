from mimetypes import init
from HinhHoc import HinhHoc


class HinhVuong(HinhHoc):

    def __init__(self, edge):
        self.__canh = edge

    def TinhChuVi(self):
        return float(self.__canh*4)

    def TinhDienTich(self):
        return float(self.__canh*self.__canh)

    def __str__(self):
        return "Hinh vuong canh "+str(self.__canh)+" co dien tich "+str(self.TinhDienTich())+" va chu vi "+str(self.TinhChuVi())
