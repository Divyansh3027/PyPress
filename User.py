"""
It is used to interact user with this program direct.
== == ==== == ======== ==== ==== ==== ======= ======|
"""


print('welcome to PyPress.')
print()
print('You have two options')
print('C : to compress.')
print('D : to decompress.')
print()

a =input('what you want to do:').upper()

if a=='D':
  import decompress as d
  i= input('enter location to decompress : ')
  print('What if file/folder is already existing.')
  b = input('Replace if exist...(y/n)').lower()
  if b=='y':
    n=d.decompress(i,True)
  elif b=='n':
    n=d.decompress(i,False)
  else:
    print('exiting unknown input',b)
    exit()
  
elif a=='C':
  import input as im
  i = input('enter location to be compressed : ')
  print('What if file/folder is already existing.')
  b = input('Replace if exist...(y/n)').lower()
  if b=='y':
    n=im.loc(i,True)
  elif b=='n':
    n=im.loc(i,False)
  else:
    print('exiting unknown input',b)
    exit()

else:
  print('exitting unknown input',a)
  exit()
