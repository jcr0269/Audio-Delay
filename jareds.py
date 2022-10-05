# import scipy.signal
from scipy.io import wavfile
from playsound import playsound
# import soundfile as sf
import scipy.signal as signal
import numpy as np
import matplotlib
# matplotlib.use('TkAgg', force=True)
import matplotlib.pyplot as plt
import pyaudio
import wave
# f = sf.SoundFile('audio1.wav')
samplerate, data = wavfile.read('audio3.wav')

ylen = len(data)
print('total number of samples', ylen)
print(samplerate)
T = ylen/samplerate
print(T)
#The T just tells me how long I like to talk for. You are lucky this assignment

#here is me figuring out that there is a library to do some of what i figured out
#which made me a little frustrated.

delay_array = round(20*samplerate)

#The sample rate is 8000, if you divide the amount of data by the sample rate, you can determine
#that to achieve a delay of 5 and 12 seconds you need to sample at 40,000 and 96000
#The data was 160,000. 8000*5(second = 40k and 8000*12=96000
t = np.zeros(delay_array)
t[0] = 1
t[40000] = 0.6
t[96000] = 0.3

actual_data = data[:,0]
# test = np.array(data)
# conv = scipy.signal.fftconvolve(f, t, mode="full")
conv = np.convolve(t, actual_data, mode='full')
#normalize

conv = conv/conv.max()
conv =  127+ (conv * 2**7)
#rewrite to the file for the convolved signal so we can play it.
wavfile.write('fudgeme.wav', samplerate, conv.astype(np.uint8))
# print(conv)
# playsound("fudgeme.wav")
# samplerate1, data1 = wavfile.read('fudgeme.wav')

chunk = 1024

# Open the sound file
wf = wave.open("fudgeme.wav", 'rb')

# Create an interface to PortAudio
p = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# Read data in chunks
data = wf.readframes(chunk)

# Play the sound by writing the audio data to the stream
while data != '':
    stream.write(data)
    data = wf.readframes(chunk)

# Close and terminate the stream
stream.close()
p.terminate()




# some_data = t
plt.title("Impulse_Train")
# plt.plot(some_data)
plt.ylabel("The Beautiful Sound")
plt.acorr(conv, maxlags=conv.size-1)
plt.show()


