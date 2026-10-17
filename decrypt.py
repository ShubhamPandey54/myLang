import numpy as np

x= np.linspace(0.,1.,44100)
for i in x:
  if i in x[:15]:
    data=np.sin(2*np.pi*780*x)
    
  else: 
    data=np.sin((np.pi)-(2*np.pi*780*x))
 

string=[]
d=15
for i in data[15:45]:
   m= np.linspace(0.,1.,44100)
   z=np.arcsin(i)
   x=(np.pi-z)/(2*np.pi*m[d])
   print(x)
   if 778<x<781:
     string.append("s")
   d+=1
   

sd=[]  
con=1
for i in data[1:15]:
    m= np.linspace(0.,1.,44100)
    z=np.arcsin(i)
    x=z/(2*np.pi*m[con])
    if 778<x<781:
     sd.append("s")
    con+=1

print(len(string))
print(len(sd))


