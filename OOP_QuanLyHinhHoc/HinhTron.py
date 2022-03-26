from mimetypes import init
from HinhHoc import HinhHoc
import math


class HinhTron(HinhHoc):

    def __init__(self, radius):
        self.__banKinh = radius

    def TinhChuVi(self):
        return float(round(self.__banKinh*math.pi*2,2))
    def TinhDienTich(self):
        return float(round(self.__banKinh*self.__banKinh*math.pi, 2))

    def __str__(self):
        return "Hinh tron ban kinh "+str(self.__banKinh)+" co dien tich "+str(self.TinhDienTich())+" va chu vi "+str(self.TinhChuVi())
