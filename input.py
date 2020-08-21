import shutil as shutil
import os.path as os

class Err:
  def __init__(self,*i):
    self.li=i
    
  def get(self,i=-1):
    return self.li[:i]
    
  def hasErr(self):
    return bool(len(self.li))

def loc(a='.'):
  global os,shutil
  a= os.abspath(a)
  
  if os.exists(a):
    if os.isfile(a):
      isfile =True
    elif os.isdir(a):
      isfile = False
      a2=a + '.zip'
      if os.exists(a2) and os.isdir(a2):
        tmp = Err('Archive location is directory.')
        return tmp
        
      else:
        shutil.make_archive(a,'zip',a)
        a=a2
    
    else:
      tmp = Err("Value is nither file nor directory")
      return tmp
    
    import compress as c
    m=c.compress(a,isfile)
    import os as os
    os.remove(a)
    return m
    
  else:
    tmp = Err("Location not exist")
    return tmp
  
  return Err()

"""
#A simple example

c=loc('./.')
if c.hasErr():
  print(c.get())

# where ./. become as ..
  
"""