          +---------------+
          |    Welcome    |
          |   dear user   |
          |   _________   |
          |    PYPRESS    |
          +---------------+
  
Introduction
============
<br/>  Pypress is a featured library to compress files and folders.
<br/>  Use it for other program
<br/>  or directly run it through user.py or selecting mode in __init__.py

Files
=====
<br/>&ensp;****Change in any file should reflect here.
<br/>&ensp;input.py :-
<br/>&emsp;Err class #return error message from PyPress
<br/>&emsp;loc(LOCATION) # input file folder location (LOCATION).
<br/>&emsp;&ensp;# returns Err class
<br/>&emsp;&ensp;# zip location if it is a folder
<br/>&emsp;&ensp;# transfer flow to compress.py compress() definition
<br/>&ensp;Compress.py :-
<br/>&emsp;compress(-)
<br/>&emsp;&ensp;# opens specified file in 'rb' mode for folder zip file is taken.
<br/>&emsp;&ensp;# calls press.
<br/>&emsp;press(-)
<br/>&emsp;&ensp;# change '\' to '\\' in data.
<br/>&emsp;&ensp;# for every changing layer`s every change , call press2(-)
<br/>&emsp;&ensp;# assamble data for compressed file return to compress for writting.
<br/>&emsp;press2(-)
<br/>&emsp;&ensp;# determine changing slice and its occurance (except the first occured).
<br/>&emsp;&ensp;# if occurance is bigger than specified no, it replaces that occurance appen cganged slice in list of press(-)
    
    
