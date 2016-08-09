import pyaudio
import wave
from flask import Flask

app = Flask(__name__)
audio = pyaudio.PyAudio()

@app.route("/")
def hello():
    play()
    return('OK')

def play():
    chunk = 1024

    f = wave.open(r"/Users/lauriejames/Downloads/R2D2a.wav","rb")
    
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
        app.run(port=80)
    finally:
        audio.terminate()
