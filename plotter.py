import subprocess
import numpy as np
import shutil
import os
def plotter (a):
    for d in a[0,1:]:
        e="Results/"+str(d)
        shutil.copy("plot.sh",str(e)+"/plot.sh")
        os.chdir(str(e))
        subprocess.Popen("./plot.sh")
        os.chdir("/mnt/c/users/ret64/desktop/spice/SPICE_Programs/Programs/MAGPOX")

fileo=np.loadtxt("comp.txt",dtype='str',delimiter="\t",unpack=False)
plotter(fileo)