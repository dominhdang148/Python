# I. Cắt mảng (Slicing Array)

#   - Cắt (slicing) trong Python nghĩa là lấy 1 dãy các phần tử của một Array dựa trên 1 chỉ số index làm điểm bắt đầu và 1 chỉ số index làm chỉ sổ cuối.
#   - Ta truyền "Lát cắt" bằng các chỉ số: [start:end]
#   - Ta cũng có thể xác định bước cắt (step): [start:end:step]
#   - Nếu không truyền start, chương trình sẽ xem start=0
#   - Nếu không truyền end, chương trình sẽ xem như end = độ dài của Array với chiều đang xét.
#   - Nết không truyền step, chương trình sẽ xem step=1

from os import system
import numpy as np
system('cls')
arr = np.array([1, 2, 3, 4, 5, 6, 7])  # Cắt các phần tử từ index 1 đến inđex 5
print(arr[1:5])

#  LƯU Ý: Kết quả trả về bao gồm phần tử có index là start, nhưng không boa gồm phần tử có index là end

print(arr[4:])  # Cắt các phần tử từ index 4 đến hết array
print(arr[:4])  # Cắt các phần tử từ đầu array đến index 4 (Không bao gồm index 4)

# II. Cắt mảng âm (Negative slicing)

#   - Sử dụng dấu trừ (-) để tham chiếu đến chỉ số index từ cuối mảng

print(arr[-3:-1]) # Cắt các phần tử từ index 3 từ cuối mảng đến phần từ 1 từ cuối mảng

# III. STEP (bước)

#   - Sử dụng step để xác định các bước của việc cắt mảng

print(arr[1:5:2])  # Cắt các phần tử từ index 1 đến index 5 cách nhau 2 phần tử
print(arr[::2])  # Trả về tất cả các phần tử của array cách nhau 2 phần tử

# IV. Cắt mảng 2 chiều

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) # Từ pnần tử mảng thứ 2, cắt các phần tử từ index 1 đến index 4 (không bao gồm index 4)
 
#   LƯU Ý: phần tử thứ 2 luôn có chỉ số index = 1

print(arr[0:2,2]) # Từ tất cả phần tử mảng, trả về phần tử có chỉ số index = 2
print(arr[0:2,1:4]) # Từ tất cả phần tử mảng, cắt các phần tử tử index 1 đến index 4 (không bao gồm index 4) ---> Trả về 1 mảng 2 chiều (2-D Array)

