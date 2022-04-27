# I. Phép chia (split) mảng trong NumPy

# - Phép chia (Splitting) là phép toán ngược so với phép kết (joining)
# - Phép kết sẽ hợp 2 mảng lại với nhau, trong khi phép chia sẽ tách 1 mảng thành nhiều mảng khác nhau.
# - Sử dụng hàn array_split() để chia mảng. Truyền các tham số là mảng cần chia và số phần nần chia thành.

from os import system
import numpy as np

system('cls')

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)          # Chia mảng arr thành 3 phần.
print(newarr)

# NOTE: Kết quả trả về là 1 mảng chứa 3 mảng

# - Nếu mảng có ít phần tử hơn yêu cầu, hàm sẽ tự động điều chỉnh cho phù hợp với điều kiện

newarr = np.array_split(arr, 4)
print(newarr)

# NOTE: NumPy cũng có hàm split() với chức năng tương tự. Tuy nhiên, hàm này sẽ không tự điều chỉnh các phần tử khi các phần tử ít hơn yêu cầu. Như ví dụ trên, nếu xài hàm split(), chương trình sẽ báo lỗi.

# II. Chia thành nhiều mảng

#   - Kết quả trả về của phương thức array_split() là một array bao gồm các phần tử của mảng nguồn sau khi chia
#   - Nếu chia 1 mảng thành nhiều mảng khác nhau, có thể truy cập các mảng kết quả nầy như một phần tử của mảng.

newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

# III. Chia mảng 2-D

#   - Sử dụng cú pháp tương tự để chia mảng 2 chiều.
#   - Sử dụng phương thức array_split(), truyền đối số là mảng cần chia và số

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)
print(newarr)

#   - Ví dụ trên trả về kết quả là 3 mảng 2 chiều.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [
               10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)
print(newarr)

#   - Ta có thể chia 1 mảng 2 chiều dựa trên chỉ số trục axis của nó.
#   - Ví dụ, để tách mảng dọc theo hàng (row) bằng cách đặt tham số axis = 1.

newarr = np.array_split(arr, 3, axis=1)
print(newarr)

#   - Biện pháp thay thế là sử dụng hàm hsplit(), đối nghịch với hstack()

newarr = np.hsplit(arr, 3)
print(newarr)

# NOTE: Tương tự như vstack() hoặc dstack(), các biện pháp thay thế tương ứng là vsplit() và dsplit() (dsplit() chủ sử dụng được cho mảng 3 chiều trở lên)

newarr=np.vsplit(arr, 3)
print(newarr)
