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

def loc(a='.',replace=True):
  global os,shutil
  a= os.abspath(a)
  a1=a
  if os.exists(a):
    if os.isfile(a):
      isfile =True
    elif os.isdir(a):
      isfile = False
      num = 0
      a1 += '.zip'
      while os.exists(a1) or os.isdir(a1):
        a1=a + str(num)+'.zip'
        num +=1
      a2 = a1[:-4]
      shutil.make_archive(a2,'zip',a)
    
    else:
      tmp = Err("Value is nither file nor directory")
      return tmp
    
    import compress as c
    m=c.compress(a,a1,isfile,replace)
    return m
    
  else:
    return Err("Location not exist")
  import os as os
  os.remove(a1)
  
  return Err()

"""
#A simple example
c=loc('input.py' [,False | True]) => to compress input.py
if c.hasErr():
  print(c.get())
# where ./. become as ..
  
"""