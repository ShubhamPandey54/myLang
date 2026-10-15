from scipy.io import wavfile
import numpy as np 
import math

samplerate, data = wavfile.read("final.wav")
string=[]
x=np.linspace(0.,1.,44100)
d=1
print(x[15])

data[15:20]
for i in data[1:16]:
    val=np.asin(i)
    z=val/(2*np.pi*x[d])
    if 778<z<781:
     string.append(z)
    d=d+1

c=np.asin(data[149])
re=c/(2*np.pi*x[149])
print(re)

