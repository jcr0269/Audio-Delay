import sounddevice as sd
from scipy.io.wavfile import write

fs = 8000  # Sample rate
seconds = 20  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('audio3.wav', fs, myrecording)