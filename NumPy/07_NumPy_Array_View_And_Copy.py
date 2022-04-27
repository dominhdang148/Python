# I. Sự khác biệt giữa copy và view

#   - Sự khác biệt chủ yếu giữa copy và view trên 1 array là: Copy sẽ thao tác trên 1 mảng mói, và View sẽ thao tác trên chính mảng gốc
#   - copy sẽ nhận dữ liệu từ mảng gốc và các thao tác làm thay đổi dữ liệu trên copy sẽ không ảnh hưởng đến mảng gốc và các thao tác làm
#   thay đổi dữ liệu trên mảng gốc cũng ko ảnh hưởng đến mảng copy.
#   - view sẽ không nhận dữ liệu từ mảng gốc và các thao tác làm thay đổi dữ liệu trên mảng view sẽ ảnh hưởng đến mảng gốc và các thao tác
#   thay đổi dữ liệu trên mảng gốc cũng sẽ ảnh hưởng đến mảng view

# II. COPY:

from os import system
import numpy as np

system('cls')

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#   --> COPY sẽ không bị ảnh hưởng bởi sự thay đổi từ mảng gốc

# III. VIEW:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

#   --> VIEW sẽ bị ảnh hưởng bởi sự thay đổi tử mảng gốc

# IV. Thay đổi dữ liệu trên View:

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)
#   --> Mảng gốc sẽ bị ảnh hưởng bởi sự thay đổi từ mảng View

# V. Kiểm tra xem mảng có nhận dữ liệu từ mảng khác hay không

#   - Dù ta đã biết rằng mảng copy sẽ nhận dữ liệu từ mảng gốc, còn mảng view thì không. Nhưng đôi khi ta vẫn phải kiểm tra xem 1 mảng bất kỳ
#   có nhận dữ liệu từ mảng khác hay không.
#   - Tất cả Array của NumPy đều có thuộc tính base. Thuộc tính này sẽ trả về None nếu mảng đang xét có nhận dữ liệu.
#   - Ngược lại, thuộc tính base sẽ tham chiếu đến mảng chứa dữ liệu gốc.

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

