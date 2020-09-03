import shutil
import os.path as os

class Err:
  def __init__(self,*i):
    self.li=i
    
  def get(self,i=None):
    if i is None:
      return self.li[:]
    return self.li[:i]
    
  def hasErr(self):
    return bool(len(self.li))

def loc(a='.'):
  global os,shutil
  a= os.abspath(a)
  
  if os.exists(a):
    already =False
    if os.isfile(a):
      isfile =True
    elif os.isdir(a):
      isfile = False
      a2=a + '.zip'
      if os.exists(a2):
        already =True
        if os.isdir(a2):
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
    if already:
      import os as os
      os.remove(a)
    return m
    
  else:
    tmp = Err("Location not exist")
    return tmp
  
  tmp = Err()
  return tmp

"""
#A simple example
c=loc('input.py') => to compress input.py
if c.hasErr():
  print(c.get())
# where ./. become as ..
  
"""