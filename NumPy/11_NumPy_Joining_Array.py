# I. Kết mảng NumPy

#   - Kết (Join) có nghĩa kéo nội dung của 2 hay nhiều mảng lại với nhau tạo thành 1 mảng riêng biệt.
#   - Trong SQL, ta thực hiện việc phép kết nhiều bảng lại với nhau dựa theo khóa. Trong NumPy, ta kết nhiều mảng lại với nhau dựa theo trục của mảng (axis)
#   - Ta truyền vào các đối số là các mảng mà ta muốn nối vào trong phương thức concatenate(), cùng với đối số axis. Nếu Axis không được truyền vào, phương thức sẽ mặc định axis = 0
from os import system
import numpy as np

system('cls')

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))  # Kết 2 mảng 1 chiều
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Kết 2 mảng 2 chiều dựa theo trục hoành
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

# II. Nối mảng bằng phương thức stack()

#   - Stack (xếp chồng) cũng tương tự với concatenation, tuy nhiên, stack sẽ được thực hiện dựa trên 1 trục axis mới.
#   - Ta có thể Kết 2 mảng 1 chiều dọc theo trục axis thứ 2, kết quả cũng sẽ tương tự với stack
#   - Ta truyền vào các đối số là các mảng mà ta muốn k vào trong phương thức stack(), cùng với đối số axis. Nếu axis không được truyền vào, phương thức sẽ mặc định axis = 0

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)
print(arr)

# III. Xếp chồng dọc theo hành

#   - NumPy cung cấp 1 hàm hỗ trợ: hstack() để stack dọc theo hàng (trục ngang)

arr = np.hstack((arr1, arr2))
print(arr)

# IV. Xếp chồng dọc theo cột

#   - NumPy cung cấp 1 hàm hỗ trợ: vstack() để stack dọc theo cột (trục dọc)

arr = np.vstack((arr1, arr2))
print(arr)

# V. Xếp chồng dọc theo chiều sâu

#   - NumPy cung cấp 1 hàm hỗ trợ: dstack() để stack dọc theo chiều sâu

arr = np.dstack((arr1, arr2))
print(arr)
