import math
from scipy.io.wavfile import write
from scipy.io import wavfile
import numpy as np 

class mylang():
   def __init__(self,string):
      self.string=string
      self.list=[]

   def lang(self):
      
      for letter in self.string: 
         if letter=="A" or letter=="a":
             x=np.linspace(0.,1.,44100)
             data=0.02*np.sin(2*np.pi*420*x)
             for i in data:
                self.list.append(i)

         elif letter==" ":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*250*x)
            for i in data:
               self.list.append(i)

         elif letter.lower()=="b":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*440*x)
            for i in data:
               self.list.append(i)      
         elif letter.lower()=="c":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*460*x)
            for i in data:
               self.list.append(i)  

         elif letter.lower()=="d":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*480*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="e":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*500*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="f":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*520*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="g":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*540*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="h":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*560*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="i":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*580*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="j":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*600*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="k":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*620*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="l":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*640*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="m":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*660*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="n":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*680*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="o":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*700*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="p":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*720*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="q":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*740*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="r":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*760*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="s":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*780*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="t":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*800*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="u":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*820*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="v":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*840*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="w":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*860*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="x":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*880*x)
            for i in data:
               self.list.append(i)  

         elif letter.lower()=="y":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*900*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="z":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*920*x)
            for i in data:
               self.list.append(i) 

         elif letter=="0":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*940*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="1":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*960*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="2":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*980*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="3":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1000*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="4":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1020*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="5":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1040*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="6":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1060*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="7":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1080*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="8":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1100*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="9":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1120*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="!":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1140*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=='"':
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1160*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="#":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1180*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="$":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1200*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="%":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1220*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="&":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1240*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="'":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1260*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="(":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1280*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter==")":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1300*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="*":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1320*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="+":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1340*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter==",":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1360*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="-":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1380*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter==".":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1400*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="/":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1420*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter==":":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1440*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter==";":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1460*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="<":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1480*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="=":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1500*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter==">":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1520*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="?":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1540*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="@":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1560*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="[":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1580*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="\\":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1600*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="]":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1620*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="^":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1640*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="_":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1660*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="`":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1680*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="{":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1700*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="|":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1720*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="}":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1740*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)

         elif letter=="~":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1760*x)+np.random.normal(0,0.2,44100)
            for i in data:
               self.list.append(i)
          
   def cryptic(self,value,key=9999):
      self.list.append(value)
      self.list.append(key)

   def encrypt(self):
            Fs, y = wavfile.read("C:\\Users\\AMAN\\Downloads\\Cass Elliot - Make Your Own Kind Of Music (Lyric Video).wav")
            s=[]
            i=0
            while i<=(len(y)-44100):
                  s.append(y[i:i+44100])
                  i+=Fs
            data=np.array(self.list)
            duration=len(data)/44100
            print(duration)
            print(s[0:int(duration)])
            print(len(np.array(s[:int(duration)])))
         
            music=np.array(s[0:int(duration)])
            if np.max(np.abs(music)) > 1.0:
              music = music / 32768.0
            array_a_mono_blocks = data.reshape(int(duration), 44100)
            array = np.stack([array_a_mono_blocks, array_a_mono_blocks], axis=-1)
            final_signal=  0.03*array + music 
            write("fnal.wav",44100, final_signal.reshape(-1, 2).astype(np.float32))
            print("encryption successfull...")

ask=input("TEXT: ")   
con=mylang(ask)
con.lang()
con.encrypt()

