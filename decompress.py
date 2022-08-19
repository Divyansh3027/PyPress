from ast import literal_eval as val
import shutil
import os.path as os

def do(w,d):
    for a in w:
        t=w[-1]
        w=w[:-1]
        d.replace('\\'+str(len(w))+'.',t)
    return d
        

def decompress(path,replace=True):
    if not os.exists(path):
        from input import Err
        return Err('Compressed file not exist.')
    with open(path,'r') as cf:
        is_file = cf.readline()[0]
        loc = cf.readline()[:-1]
        word = val(cf.readline()[:-1])
        data = cf.readline()
        data = data.replace('\\\\','\\')
        data = do(word,data)
        
    if replace or not os.exist(loc):
        z = loc
        if not is_file:
            z +='.zip'
            num =0
            while os.exists(z):
                z = loc+str(num)+'.zip'
                num += 1
            with open(z,'wb+') as f:
                f.write(val(data))
                f.close()
            shutil.unpack_archive(z,loc)
            return
        with open(loc,'w+') as f:
            f.write(data)
            f.close()
        
        
            
        
        
        
    