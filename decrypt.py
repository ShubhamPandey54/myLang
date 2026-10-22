import numpy as np
from scipy.io import wavfile
from encryption import noise 

class decrypt():
      def __init__(self,filename):
            self.filename=filename
            
      def decode(self):     
        try:
            samplerate, yed = wavfile.read(self.filename)
            duration = len(yed)/samplerate   
            sed=noise()  
            music=np.array(sed[0:int(duration)])
            if np.max(np.abs(music)) > 1.0:
              music = music / 32768.0
            music=np.concatenate(music,axis=0)
            y=  yed[:,0] - music[:,0]
                
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

          fft_output = np.fft.fft(audio_block)
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
             
#NUMBERS
         elif round(i) == 940:
             word.append("0")
         elif round(i) == 960:
             word.append("1")
         elif round(i) == 980:
             word.append("2")
         elif round(i) == 1000:
             word.append("3")
         elif round(i) == 1020:
             word.append("4")
         elif round(i) == 1040:
             word.append("5")
         elif round(i) == 1060:
             word.append("6")
         elif round(i) == 1080:
             word.append("7")
         elif round(i) == 1100:
             word.append("8")
         elif round(i) == 1120:
             word.append("9")

#SPECIAL CHARACTERS

         elif round(i) == 1140:
             word.append("!")
         elif round(i) == 1160:
             word.append('"')
         elif round(i) == 1180:
             word.append("#")
         elif round(i) == 1200:
             word.append("$")
         elif round(i) == 1220:
             word.append("%")
         elif round(i) == 1240:
             word.append("&")
         elif round(i) == 1260:
             word.append("'")
         elif round(i) == 1280:
             word.append("(")
         elif round(i) == 1300:
             word.append(")")
         elif round(i) == 1320:
             word.append("*")
         elif round(i) == 1340:
             word.append("+")
         elif round(i) == 1360:
             word.append(",")
         elif round(i) == 1380:
             word.append("-")
         elif round(i) == 1400:
             word.append(".")
         elif round(i) == 1420:
             word.append("/")
         elif round(i) == 1440:
             word.append(":")
         elif round(i) == 1460:
             word.append(";")
         elif round(i) == 1480:
             word.append("<")
         elif round(i) == 1500:
             word.append("=")
         elif round(i) == 1520:
             word.append(">")
         elif round(i) == 1540:
             word.append("?")
         elif round(i) == 1560:
             word.append("@")
         elif round(i) == 1580:
             word.append("[")
         elif round(i) == 1600:
             word.append("\\")
         elif round(i) == 1620:
             word.append("]")
         elif round(i) == 1640:
             word.append("^")
         elif round(i) == 1660:
             word.append("_")
         elif round(i) == 1680:
             word.append("`")
         elif round(i) == 1700:
             word.append("{")
         elif round(i) == 1720:
             word.append("|")
         elif round(i) == 1740:
             word.append("}")
         elif round(i) == 1760:
             word.append("~")
         
        for i in word :
            print(i,end="")
        

filename=input("filename")
text =decrypt(filename)
text.decode()




