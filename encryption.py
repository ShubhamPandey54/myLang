import math
from scipy.io.wavfile import write
import numpy as np 

class mylang():
   def __init__(self,string):
      self.string=string
      self.list=[]

   def lang(self):
      
      for letter in self.string: 
         if letter=="A" or letter=="a":
             x=np.linspace(0.,1.,44100)
             data=0.02*np.sin(2*np.pi*420*x)+ np.random.normal(0, 0.2, 44100)
             for i in data:
                self.list.append(i)

         elif letter==" ":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*250*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)

         elif letter.lower()=="b":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*440*x)+np.random.normal(0.,0.2,44100)
            for i in data:
               self.list.append(i)      
         elif letter.lower()=="c":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*460*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)  

         elif letter.lower()=="d":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*480*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="e":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*500*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="f":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*520*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="g":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*540*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="h":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*560*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="i":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*580*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="j":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*600*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="k":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*620*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="l":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*640*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="m":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*660*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="n":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*680*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="o":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*700*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="p":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*720*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="q":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*740*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="r":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*760*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="s":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*780*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="t":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*800*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="u":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*820*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="v":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*840*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="w":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*860*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="x":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*880*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)  

         elif letter.lower()=="y":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*900*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="z":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*920*x)+ np.random.normal(0, 0.2, 44100)
            for i in data:
               self.list.append(i) 
          
   def covert(self,value,key=9999):
      self.list.append(value)
      self.list.append(key)

   def encrypt(self):
            data=np.array(self.list)
            write("final.wav",44100,data.astype(np.float32))
            print("encryption successfull...")

ask=input("TEXT: ")   
con=mylang(ask)
con.lang()
con.covert(value=321)
con.encrypt()

