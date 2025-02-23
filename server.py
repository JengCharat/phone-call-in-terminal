import socket

import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

# สร้าง socket

# กำหนด port และ frequency
port = 12345
freq = 44100

# เชื่อมต่อกับ server

while True:
    # loop เพื่อรับข้อมูล

    s = socket.socket()
    s.connect(("127.0.0.1", port))
    data = ""
    while True:
        # รับข้อมูลจาก server ทีละส่วน
        chunk = s.recv(1048576).decode()
        if "]]" in data:  # ถ้าพบ `]]` ในข้อมูล ให้หยุดรับข้อมูล
            print("close]]")
            s.close()
            break  # ออกจาก loop ถ้าเจอ `]]`

        if not chunk:  # ถ้าไม่มีข้อมูลเพิ่มเติมให้หยุด
            print("close")
            s.close()
            break
        # เก็บข้อมูลที่รับมา
        data += chunk

    # print("found")
    # print(data)
    # หลังจากได้รับข้อมูลครบทั้งหมด
    # แปลงข้อมูลที่ได้รับเป็น list ของ float โดยการแยกตามช่องว่าง
    data = data.replace("[", "").replace("]", "")  # ลบวงเล็บ
    x = list(map(float, data.split()))

    # แปลงเป็น numpy array และ reshape ให้เป็น column vector
    array = np.array(x).reshape(-1, 1)

    # แสดงผลข้อมูล numpy array
    print(array)

    # เล่นเสียง
    # write("recording1.wav", freq, array)
    #
    print("try play sound")
    array = np.float32(array)  # หรือแปลงเป็น int16 ตามความเหมาะสม
    array = np.clip(array, -1, 1)  # ตรวจสอบให้ค่าของ array อยู่ในช่วง [-1, 1]

    # เล่นเสียง
    sd.play(array, samplerate=freq)

    # รอให้การเล่นเสียงเสร็จ
    # sd.wait()
    #
    # # ปิดการเชื่อมต่อ
