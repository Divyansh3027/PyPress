import shutil as shutil
import os.path as os

class Err:
  def __init__(self,*i):
    self.li=l
    
  def get(self,i=-1):
    return self.li[:i]

def loc(a='.'):
  global os,shutil
  if os.exists(a):
    if os.isfile(a):
      isfile =True
    elif os.isdir(a):
      isfile = False
      l2= os.dirname(a) + os.basename(a) +'.zip'
      if os.exists(l2) and os.isdir(l2):
        tmp = Err('Archive location is directory.')
        return tmp
        
      else:
        shutil.make_archive(os.dirname(a) + os.basename(a),'zip',os.dirname(a) + os.basename(a))
          
      del l2
    
    else:
      tmp = Err("Value is nither file nor directory")
      return tmp
    
    #Compress process come here
    
  else:
    tmp = Err("Location not exist")
    return tmp
  
  path = os.dirname(a)
  name = os.basename(a)
  del os
  del shutil

loc('./.')