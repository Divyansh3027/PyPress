
        +---------------+
        |    Welcome    |
        |   dear user   |
        |   _________   |
        |    PYPRESS    |
        +---------------+
<b>&emsp;&emsp;&emsp;PyPress 0.0.0</b><br/>


  
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
<br/>&emsp;&ensp;# replace option provides info to progran weather to delete existing compressed file
<br/>&emsp;&ensp;# zip location if it is a folder
<br/>&emsp;&ensp;# transfer flow to compress.py compress() definition
<br/>&ensp;Compress.py :-
<br/>&emsp;compress(-)
<br/>&emsp;&ensp;# opens specified file in 'r' mode, for folder 'rb' mode and zip file is taken.
<br/>&emsp;&ensp;# if exist replace compress file by viewing replace permission if permission not granted it will stop the program.
<br/>&emsp;&ensp;# calls press for compressing data.
<br/>&emsp;press(-)
<br/>&emsp;&ensp;# change '\' to '\\' in data.
<br/>&emsp;&ensp;# for every changing layer`s every change , identifies the better changes and implements them in data each time.
<br/>&emsp;&ensp;# assamble data for compressed file return to compress for writting.
<br/>&ensp;User.py :-
<br/>&emsp;# A CLI (Command Line Interface) of PyPress.
<br/>&emsp;# Ask to compress or decompress c/d.
<br/>&emsp;# Ask to replace existing file even founded or not.
<br/>&emsp;# Ask name of file or folder to compress..
<br/>&ensp;Decompress.py :-
<br/>&emsp;decompress(-)
<br/>&emsp;&ensp;# Check if compressed file available.
<br/>&emsp;&ensp;# Analyse compressed file each element.
<br/>&emsp;&ensp;# Calls do to decompress data section with help of word section
<br/>&emsp;&ensp;# if destiny is folder creates zip file writes data section of compressed file in it and unpack it in destiny.
<br/>&emsp;&ensp;# if destiny is file it writes data section in destiny.
    
