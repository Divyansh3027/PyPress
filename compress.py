import os.path as os
from input import Err



def press(data):
  print('Real file size',len(data))
  complete=[]
  data = data.replace('\\','\\\\')
  
  #data = [data]
  for i in [10,9,8,7,6,5,4]:
    print('File size now',len(data),'bytes')
    
    for j in range(len(data)-i):
      top = data[j:j+i]
      count = 0
      loop = 0
      
      for p in range(len(data)-i):
        if loop:
          loop-=1
          continue
        if data[p:p+i] == top:
          loop = i
          count +=1
          if count == 5:
            data= data.replace(top,'\\'+str(len(complete)))
            complete.append(top)
            break
          
  print('Compressed file size',len(data))
  print('writting your file.')
  
  return (complete,data)
  
    

def compress(f,is_file):
  f2=f
  f=(f if is_file else f[:-4])
  loc = os.dirname(f)
  with open(f,'r' if is_file else 'rb') as c :
    inf=str(c.read())
    if os.exists(f+'.cmp'):
      if os.isdir(f+'.cmp'):
        return Err('a folder exist with compress output file name.\nSo unable to output compressed file')
        
  with open(f+'.cmp',"w") as c2:
    c2.write(str(int(is_file))+'\n')
    c,d = press(inf)
    c2.write(str(f)+'\n')
    c2.write(str(c)+'\n')
    c2.write(str(d))
    c2.close()
  
  return Err() #no argument, error not occured.