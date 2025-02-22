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
x = s.recv(1048576).decode()

# ลบวงเล็บที่อยู่รอบๆ ข้อความ
x = x[1:-1]  # ลบวงเล็บทั้งคู่ออก

# แยกข้อมูลด้วย "] [" และลบช่องว่างที่ไม่จำเป็น
x = x.split("] [")  # แยกข้อมูลด้วย "] ["

# ลบช่องว่างและ \n จากข้อมูลแต่ละบรรทัด
x = [item.replace("\n", "").strip() for item in x]

# แปลงข้อมูลเป็น float และจัดการข้อมูลที่มีมากกว่าหนึ่งตัวเลข
x = [list(map(float, item.split())) for item in x]

# แปลงเป็น numpy array
array = np.array(x)

# ตั้งค่าการแสดงผลให้แสดงข้อมูลทั้งหมด
np.set_printoptions(threshold=np.inf)  # threshold=np.inf แสดงผลทั้งหมดของ array

# แสดงผลแบบที่ต้องการ (แสดงผลตามรูปแบบที่มีวงเล็บอยู่)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(array)

# บันทึกไฟล์เสียง
write("recording1.wav", freq, array)

# ปิดการเชื่อมต่อ
s.close()
