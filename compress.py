import os.path as os

def press2(a,b,d,cm):
  top = d[0][b:b+a]
  count=0
  i=0
  for p in range(a,len(d[0])-a):
    if not(i==0):
      i -= 1
      continue
    if d[0][p:p+a] == top:
      i = a
      count += 1
  if count > 5: # use any no. I choose 5 to nat make load on file.
    d[0]=d[0].replace(top,'\\'+str(len(cm))+'.')
    cm.append(top)


def press(data,path,head):
  complete=[]
  data = data.replace('\\','\\\\')
  
  data = [data]
  for i in [3,3,4,4,5,5,6,6,7,7]:
    print(len(data[0]))
    print()
    for j in range(len(data[0])-i):
      press2(i,j,data,complete)
  data = data[0]
  
  print()
  
  return (head,complete,data)
    
    

def compress(f,is_file):
  f2=f
  loc = os.dirname(f)
  with open(f,'r' if is_file else 'rb') as c :
    f=(f if is_file else f[:-4])
    inf=str(c.read())
    if os.exists(f+'.cmp'):
      if os.isdir(f+'.cmp'):
        from input import Err
        return Err('a folder exist with compress output file name.\nSo unable to output compressed file')
        
  with open(f+'.cmp',"w") as c2:
    c2.write(str(int(is_file))+'\n')
    h,c,d = press(inf,loc,f)
    c2.write(str(h)+'\n')
    c2.write(str(c)+'\n')
    c2.write(str(d))
    c2.close()
  
  from input import Err
  return Err()