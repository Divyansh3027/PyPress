
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
<br/>&emsp;****Change in any file should reflect here.
<br/>&emsp;input.py :-
<br/>&emsp;&emsp;Err class #return error message from PyPress
<br/>&emsp;&emsp;loc(LOCATION) # input file folder location (LOCATION).
<br/>&emsp;&emsp;&emsp;# returns Err class
<br/>&emsp;&emsp;&emsp;# replace option provides info to progran weather to delete existing compressed file
<br/>&emsp;&emsp;&emsp;# zip location if it is a folder
<br/>&emsp;&emsp;&emsp;# transfer flow to compress.py compress() definition
<br/>&emsp;Compress.py :-
<br/>&emsp;&emsp;compress(-)
<br/>&emsp;&emsp;&emsp;# opens specified file in 'r' mode, for folder 'rb' mode and zip file is taken.
<br/>&emsp;&emsp;&emsp;# if exist replace compress file by viewing replace permission if permission not granted it will stop the program.
<br/>&emsp;&emsp;&emsp;# calls press for compressing data.
<br/>&emsp;&emsp;press(-)
<br/>&emsp;&emsp;&emsp;# change '\' to '\\' in data.
<br/>&emsp;&emsp;&emsp;# for every changing layer`s every change , identifies the better changes and implements them in data each time.
<br/>&emsp;&emsp;&emsp;# assamble data for compressed file return to compress for writting.
<br/>&emsp;User.py :-
<br/>&emsp;&emsp;# A CLI (Command Line Interface) of PyPress.
<br/>&emsp;&emsp;# Ask to compress or decompress c/d.
<br/>&emsp;&emsp;# Ask to replace existing file even founded or not.
<br/>&emsp;&emsp;# Ask name of file or folder to compress..
<br/>&emsp;Decompress.py :-
<br/>&emsp;&emsp;decompress(-)
<br/>&emsp;&emsp;&emsp;# Check if compressed file available.
<br/>&emsp;&emsp;&emsp;# Analyse compressed file each element.
<br/>&emsp;&emsp;&emsp;# Calls do to decompress data section with help of word section
<br/>&emsp;&emsp;&emsp;# if destiny is folder creates zip file writes data section of compressed file in it and unpack it in destiny.
<br/>&emsp;&emsp;&emsp;# if destiny is file it writes data section in destiny.
    
