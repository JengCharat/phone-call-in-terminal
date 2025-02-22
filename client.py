# import required libraries
# import socket for send array of numpy to server
import socket

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
duration = 5


# Start recorder with the given values of
# duration and sample frequency
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)
print("recording0.wav", freq, recording)
# or we can use this
# Convert the NumPy array to audio file
# wv.write("recording1.wav", recording, freq, sampwidth=2)

# a forever loop until we interrupt it or
# an error occurs
s.listen(5)
print("socket is listening")
while True:
    # Establish connection with client.
    c, addr = s.accept()
    print("Got connection from", addr)

    # send a thank you message to the client. encoding to send byte type.
    c.send("Thank you for connecting".encode())

    # Close the connection with the client
    c.close()

    # Breaking once connection closed
    break
