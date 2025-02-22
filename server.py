import socket

import numpy as np
from scipy.io.wavfile import write

# สร้าง socket
s = socket.socket()
# กำหนด port และ frequency
port = 12345
freq = 44100

s.connect(("127.0.0.1", port))

# ข้อความที่ได้จากการรับข้อมูล
# x = "[[ 1.91572341e-14  1.71508434e-14] [-6.12094320e-10 -5.47954515e-10] [-3.56669752e-08 -3.18704174e-08] [ 1.04535786e-04  4.70938467e-05] [ 9.77807504e-05  6.44944594e-05] [ 1.09818277e-04  8.55066828e-05]]"

x = s.recv(1048576).decode()
print(x)
# ลบวงเล็บที่อยู่รอบๆ ข้อความ
x = x[1:-1]  # ลบวงเล็บทั้งคู่ออก

# แยกข้อมูลด้วย "] [" และลบช่องว่างที่ไม่จำเป็น
x = x.split("] [")  # แยกข้อมูลด้วย "] ["

# ลบวงเล็บในแต่ละส่วน
x = [item.replace("[", "").replace("]", "") for item in x]

# แปลงข้อมูลเป็น float และจัดการข้อมูลที่มีมากกว่าหนึ่งตัวเลข
x = [list(map(float, item.split())) for item in x]

# แปลงเป็น numpy array
array = np.array(x)

# แสดงผล
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

np.set_printoptions(threshold=np.inf)  # threshold=np.inf แสดงผลทั้งหมดของ array
print(array)

write("recording1.wav", freq, array)
