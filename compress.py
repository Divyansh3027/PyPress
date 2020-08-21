import os.path as os

def press2(a,b,d,cm):
  pass

def press(data,path,head):
  for i in [4,5,6,7,8]:
    complete=[]
    for j in range(len(data)-i):
      data=press2(i,j,data,complete)

def compress(f,is_file):
  loc = os.pathname(f)
  with open(f,'rb') as c :
    f=(f[:-1] if is_file else f[:-5])
    if os.exists(loc+f+'.cmp'):
      if os.isdir(loc+f+'.cmp'):
        from input import Err
        return Err('a folder exist with compress output file name.\nSo unable to output compressed file')
    press(c.read(),loc,f)
      
      