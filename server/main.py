import pyaudio
import wave
import random
from flask import Flask

app = Flask(__name__)
audio = pyaudio.PyAudio()

NUM_FILES = 10
FILE_PATH = "/Users/lauriejames/git/tilda-r2d2/server/wav"

@app.route("/")
def hello():
    play()
    return('OK')

def play():
    filenum = random.randint(0, NUM_FILES)
    chunk = 1024

    f = wave.open('{}/R2D2-{}.wav'.format{FILE_PATH, filenum}, "rb")

    stream = audio.open(format = audio.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)

    data = f.readframes(chunk)

    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()


if __name__ == "__main__":
    try:
        app.run(port=80, host='0.0.0.0')
    finally:
        audio.terminate()
