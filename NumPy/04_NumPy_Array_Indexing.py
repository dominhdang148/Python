# I. Truy cập phần tử của Array

#   - Việc lập chi mục mảng cũng giống như vicẹ truy cập một phần tử của mảng
#   - Có thể truy cập 1 phần tử của mảng bằng cách tham chiếu điến chỉ số index của nó.
#   - Chỉ số trong Array của NumPy luôn bắt đầu bằng số 0, nghĩa là phần tử đầu tiên của 1 array luôn có chỉ số index = 0, và phần tử thứ 2 có index = 1

from os import system
import numpy as np

system('cls')

arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[1])
print(arr[2]+arr[3])

# II. Truy cập mảng 2 chiều

#   - Để truy cập các phần tử trong mảng mảng 2 chiều, ta có thể sủng dụng dấu phẩy ngăn cách các số nguyên đại diện cho chiều và chỉ số của phần tử đó
#   - Có thể hiểu mảng 2 chiều như 1 bảng gồm các cột và các dòng, vị trí của dòng (row) sễ đại diện chiều của phần tử và vị trí của cột (column) sẽ đại diện cho chỉ sổ của phần tử đó

arrMat = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arrMat)
print('Phần tử thứ 2 ở hàng thứ nhất là: ', arrMat[0, 1])
print('Phần tử thứ 5 ở hàng thứ 2 là:', arrMat[1, 4])

# III. Truy cập mảng 3 chiều

#   - Để truy cập các phần tử trong mảng 3 chiều, ta có thể sử dụng dấu phẩy ngăn cách các số nguyên đại diện cho chiều và chỉ số của phần tử đó.

arrTens = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arrTens)
print(arrTens[0, 1, 2])  # ---> 6

#   GIẢI THÍCH VÍ DỤ TRÊN:

#   Xét mảng [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]:
#   - Số nguyên đầu tiên đại diện cho chiều thứ nhất của Array. -> Chiều thứ nhất gồm có 2 mảng 2 chiều:
#   [[1, 2, 3], [4, 5, 6]] và [[7, 8, 9], [10, 11, 12]]
#   - Do số đại diện cho chiều thứ nhất là số 0 -> mảng thứ nhất được chọn:
#   [[1, 2, 3], [4, 5, 6]]
#   - Số nguyên thứ 2 đại diện cho chiều thứ 2 của Array -> Chiều thứ 2 gồm có 2 mảng 1 chiều:
#   [1, 2, 3] và [4, 5, 6]
#   - Do số đại diện cho chiều thứ 2 là số 1 -> mảng thứ 2 được chọn
#   [4, 5, 6]
#   - Số nguyên thứ 3 đại diện cho chiều thứ 3 của Array -> Chiều thứ 3 gồm có 3 giá trị:
#   4
#   5
#   6
#   - Do số đại diện cho chiều thứ 3 là số 2 -> Giá trị thứ 3 được chọn: -> Kết quả là 6

# IV. Chỉ số âm (Negative Indexing)

#   - Sử dụng chỉ số âm (những số nguyên nhỏ hơn 0) để truy cập các phần tử của Array theo chiều ngược (Từ phải sang trái/ từ dưới lên)

print('Phần tử cuối cùng của chiều thứ 2 của arrMat là: ', arrMat[1, -1])
