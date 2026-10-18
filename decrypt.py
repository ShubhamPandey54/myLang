import numpy as np
from scipy.io import wavfile

class decrypt():
      def __init__(self,filename):
            self.filename=filename
            
      def decode(self):     
        try:
            samplerate, y = wavfile.read(self.filename)
            if y[len(y)-1] ==9999:
                print("secret value:",y[len(y)-2])
                
        except FileNotFoundError :
            raise ValueError("not a valid file")
       
        s=[]
        i=0
        while i<=(len(y)-samplerate):
         s.append(y[i:i+samplerate])
         i+=samplerate

        j=[]

        for i in s :
          N = samplerate
          audio_block = i[0:N]  
          windowed_audio = audio_block * np.hanning(N)
          fft_output = np.fft.fft(windowed_audio)
          magnitudes = np.abs(fft_output)[:N // 2]
          frequencies = np.linspace(0, samplerate / 2, N // 2)
          dominant_index = np.argmax(magnitudes)
          peak_frequency = frequencies[dominant_index]
          j.append(peak_frequency)
    
        word=[]
        for i in j:
         if round(i)==780: 
            word.append("s")
         elif round(i)==250:
             word.append(" ")     
         elif round(i)==420:
             word.append("a")
         elif round(i)==440:
             word.append("b")
         elif round(i)==460:
             word.append("c")
       
         elif round(i)==480:
             word.append("d")     
         elif round(i)==500:
             word.append("e")
         elif round(i)==520:
             word.append("f")
         elif round(i)==540:
             word.append("g")

         elif round(i)==560:
             word.append("h")     
         elif round(i)==580:
             word.append("i")
         elif round(i)==600:
             word.append("j")
         elif round(i)==620:
             word.append("k")

         elif round(i)==640:
             word.append("l")     
         elif round(i)==660:
             word.append("m")
         elif round(i)==680:
             word.append("n")
         elif round(i)==700:
             word.append("o")
    
         elif round(i)==720:
             word.append("p")     
         elif round(i)==740:
             word.append("q")
         elif round(i)==760:
             word.append("r")
         elif round(i)==800:
             word.append("t")
    
         elif round(i)==820:
             word.append("u")     
         elif round(i)==840:
             word.append("v")
         elif round(i)==860:
             word.append("w")
         elif round(i)==880:
             word.append("x")

         elif round(i)==900:
             word.append("y")     
         elif round(i)==920:
             word.append("z")
       
        for i in word :
            print(i,end="")

filename=input("filename")
text =decrypt(filename)
text.decode()




