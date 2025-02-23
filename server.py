import socket

import numpy as np
from scipy.io.wavfile import write

# สร้าง socket
s = socket.socket()

# กำหนด port และ frequency
port = 12345
freq = 44100

# เชื่อมต่อกับ server
s.connect(("127.0.0.1", port))

# รับข้อมูลจาก server (ขนาด 1048576 ไบต์)
x = s.recv(1073741824).decode()
# แปลง string เป็น list ของ float โดยการแยกตามช่องว่าง
x = list(map(float, x.replace("[", "").replace("]", "").split()))

# แปลงเป็น numpy array และ reshape ให้เป็น column vector
array = np.array(x).reshape(-1, 1)

# แสดงผล
print(array)
# บันทึกไฟล์เสียง
write("recording1.wav", freq, array)

# ปิดการเชื่อมต่อ
s.close()
