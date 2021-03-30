import subprocess
import numpy as np
import shutil
import os
def mover (a):
    for d in a[0,1:]:
        e="Results/"+str(d)
        shutil.copy(str(e)+"/plot.pdf","/mnt/c/Users/ret64/Desktop/MAGPOXresults/pdfs/plot"+str(d)+".pdf")
fileo=np.loadtxt("comp.txt",dtype='str',delimiter="\t",unpack=False)
mover(fileo)