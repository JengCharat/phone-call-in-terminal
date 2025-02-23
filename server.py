import socket

import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

# สร้าง socket
s = socket.socket()

# กำหนด port และ frequency
port = 12345
freq = 44100

# เชื่อมต่อกับ server
s.connect(("127.0.0.1", port))
data = ""
# while True:
# loop เพื่อรับข้อมูล
while True:
    # รับข้อมูลจาก server ทีละส่วน
    chunk = s.recv(1024).decode()

    if not chunk:  # ถ้าไม่มีข้อมูลเพิ่มเติมให้หยุด
        break

    # เก็บข้อมูลที่รับมา
    data += chunk

# หลังจากได้รับข้อมูลครบทั้งหมด
# แปลงข้อมูลที่ได้รับเป็น list ของ float โดยการแยกตามช่องว่าง
data = data.replace("[", "").replace("]", "")  # ลบวงเล็บ
x = list(map(float, data.split()))

# แปลงเป็น numpy array และ reshape ให้เป็น column vector
array = np.array(x).reshape(-1, 1)

# แสดงผลข้อมูล numpy array
print(array)

# เล่นเสียง
write("recording1.wav", freq, array)

sd.play(array, samplerate=freq)

# ปิดการเชื่อมต่อ
s.close()
