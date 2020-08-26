          +---------------+
          |    Welcome    |
          |   dear user   |
          |   _________   |
          |    PYPRESS    |
          +---------------+
  
Introduction
============
  Pypress is a featured library to compress files and folders.
  Use it for other program
  or directly run it through user.py or selecting mode in __init__.py

Files
=====
  ****Change in any file should reflect here.
  input.py :-
    Err class #return error message from PyPress
    loc(LOCATION) # input file folder location (LOCATION).
      # returns Err class
      # zip location if it is a folder
      # transfer flow to compress.py compress() definition
      
  Compress.py :-
    compress(-)
      # opens specified file in 'rb' mode for folder zip file is taken.
      # calls press.
    press(-)
      # change '\' to '\\' in data.
      # for every changing layer`s every change , call press2(-)
      # assamble data for compressed file return to compress for writting.
    press2(-)
      # determine changing slice and its occurance (except the first occured).
      # if occurance is bigger than specified no, it replaces that occurance appen cganged slice in list of press(-)
    
    
