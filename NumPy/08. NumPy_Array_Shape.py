# I. Kích thước (shape) của mảng

#   - Kích thước của 1 Array là số phần tử trong mỗi chiều (dimension) của Array đó

# II. Truy vấn kích thước của 1 Array

#   - Mảng của NumPy có 1 thuộc tính tên shape. Thuộc tính này sẽ trả về 1 Tuple với mỗi chỉ mục có số phần tử tương ứng

from os import system
from langcodes import NORMALIZED_MACROLANGUAGES
import numpy as np

system('cls')

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

#   - Kết quả của ví dụ trên là (2,4), nghĩa là arr có 2 chiều, chiều thứ 1 có 2 phần tử và chiều thứ 2 có 4 phần tử

arr = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr)
print("Kích thước của arr là: ", arr.shape)

# III. Tuple shape đại diện cho điều gì?

#   - Các số nguyên ở mỗi chỉ mục mô tả số phần tử mà các chiều tương ứng chứa đựng
#   - Ở ví dụ trên, ở chỉ mục thứ 4 có 4 phần tử, nên có thể nói: ở chiều thứ 5 (4+1) có 4 phần tử 
