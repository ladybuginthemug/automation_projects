
#!/usr/bin/env python

from multiprocessing import Pool
import os
import subprocess

src = "/home/data/prod/"
dirs = next(os.walk(src))[1]

def backingup(dirs):
    dest ='home/data/prod_backup/'
    subprocess.call(["rsync", "-arq", src+'/'+ dirs, dest])

p = Pool(len(dirs))
p.map(backingup, dirs)









