"""
It is used to interact user with this program direct.
== == ==== == ======== ==== ==== ==== ======= ======|
"""

import input as im

i = input('enter location to be compressed : ')
n = im.loc(i)
if n.hasErr():
  print(n.get())
