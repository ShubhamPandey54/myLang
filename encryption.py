import math
from scipy.io.wavfile import write
import numpy as np 

class mylang():
   def __init__(self,string):
      self.string=string

   def lang(self):
      s=[]
      for letter in self.string: 
         if letter=="A" or letter=="a":
             x=np.linspace(0.,1.,44100)
             data=np.sin(2*np.pi*420*x)
             for i in data:
                s.append(i)

         elif letter==" ":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*250*x)
            for i in data:
               s.append(i)

         elif letter.lower()=="b":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*440*x)
            for i in data:
               s.append(i)      
         elif letter.lower()=="c":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*460*x)
            for i in data:
               s.append(i)  

         elif letter.lower()=="d":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*480*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="e":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*500*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="f":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*520*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="g":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*540*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="h":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*560*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="i":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*580*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="j":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*600*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="k":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*620*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="l":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*640*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="m":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*660*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="n":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*680*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="0":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*700*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="p":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*720*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="q":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*740*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="r":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*760*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="s":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*780*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="t":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*800*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="u":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*820*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="v":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*840*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="w":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*860*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="x":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*880*x)
            for i in data:
               s.append(i)  

         elif letter.lower()=="y":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*900*x)
            for i in data:
               s.append(i)   

         elif letter.lower()=="z":
            x=np.linspace(0.,1.,44100)
            data=np.sin(2*np.pi*920*x)
            for i in data:
               s.append(i)   

      data=np.array(s)
      print(data)
      write("audio.wav",44100,data.astype(np.float32))
             
ask=input("TEXT: ")        
con=mylang(ask)
con.lang()
