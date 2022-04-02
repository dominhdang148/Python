from DanhSachHinhHoc import DanhSachHinhHoc
from HinhHoc import HinhHoc
from MenuModule import kieuSapXep


class GeneralLibrary:
    def KiemTraDieuKien(a, b, sortType):
        if(sortType) == "Sap xep theo chieu tang chu vi":
            if a.TinhChuVi() > b.TinhChuVi():
                return 1
        elif(sortType) == "Sap xep theo chieu gian chu vi":
            if a.TinhChuVi() < b.TinhChuVi():
                return 1
        elif(sortType) == "Sap xep theo chieu tang dien tich":
            if a.TinhDienTich() > b.TinhDienTich():
                return 1
        elif(sortType) == "Sap xep theo chieu giam dien tich":
            if a.TinhDienTich() < b.TinhDienTich():
                return 1
        return -1

    def partition(array, begin, end):
    pivot_idx = begin
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end)
        