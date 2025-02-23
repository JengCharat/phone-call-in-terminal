# import required libraries
# import socket for send array of numpy to server
import socket

import numpy as np
import sounddevice as sd
import wavio as wv
from scipy.io.wavfile import write

# create socket object
s = socket.socket()

# declare the port
port = 12345
# Sampling frequency
freq = 44100

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(("", port))
print("socket binded to %s" % (port))


# Recording duration
duration = 10

# กำหนดให้แสดงผลทั้งหมดของ numpy array
np.set_printoptions(threshold=np.inf)  # threshold=np.inf แสดงผลทั้งหมดของ array

# Start recorder with the given values of
# duration and sample frequency
# recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
#
# # Record audio for the given number of seconds
# sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
# write("recording0.wav", freq, recording)
# print("recording0.wav", freq, recording)
# or we can use this
# Convert the NumPy array to audio file
# wv.write("recording1.wav", recording, freq, sampwidth=2)

# a forever loop until we interrupt it or
# an error occurs
s.listen(5)
print("socket is listening")

c, addr = s.accept()
print("Got connection from", addr)
# while True:
# Establish connection with client.

# send a thank you message to the client. encoding to send byte type.

recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
# Record audio for the given number of seconds
sd.wait()
# rms = np.sqrt(np.mean(np.square(recording)))
# print(f"RMS Level: {rms[0]}")
byte_data = np.array2string(recording)
c.send(byte_data.encode())

# Close the connection with the client

# Breaking once connection closed

# c.close()
