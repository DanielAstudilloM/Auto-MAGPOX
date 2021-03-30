# Written By Daniel Astudillo

import os
import numpy as np
import shutil
import time
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

def input(file,counter):
    """Reads the composition and samples file and creates a variable containing the info to be written into a MAGPOX input file"""
    mat=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    fileo=np.loadtxt(file,dtype='str',delimiter="\t",unpack=False)
    n=0
    for c in fileo[:,0]:
        fr=fileo[n,counter]
        if c.lower() in["SiO2","sio2"]:
            if float(fr) in[0,0.0,0.00]:
                mat[0]=0.0001
            else:
                mat[0]=float(fileo[n,counter])
        if c.lower() in["TiO2","tio2"]:
            if float(fr) in[0,0.0,0.00]:
                mat[1]=0.0001
            else:
                mat[1]=float(fileo[n,counter])
        if c.lower() in["Al2O3","al2o3"]:
            if float(fr) in[0,0.0,0.00]:
                mat[2]=0.0001
            else:
                mat[2]=float(fileo[n,counter])
        if c.lower() in["Cr2O3","cr2o3"]:
            if float(fr) in[0,0.0,0.00]:
                mat[3]=0.0001
            else:
                mat[3]=float(fileo[n,counter])
        if c.lower() in["FeO","feo"]:
            if float(fr) in[0,0.0,0.00]:
                mat[4]=0.0001
            else:
                mat[4]=float(fileo[n,counter])
        if c.lower() in["MgO","mgo"]:
            if float(fr) in[0,0.0,0.00]:
                mat[5]=0.0001
            else:
                mat[5]=float(fileo[n,counter])
        if c.lower() in["MnO","mno"]:
            if float(fr) in[0,0.0,0.00]:
                mat[6]=0.0001
            else:
                mat[6]=float(fileo[n,counter])
        if c.lower() in["CaO","cao"]:
            if float(fr) in[0,0.0,0.00]:
                mat[7]=0.0001
            else:
                mat[7]=float(fileo[n,counter])
        if c.lower() in["K2O","k2o"]:
            if float(fr) in[0,0.0,0.00]:
                mat[8]=0.0001
            else:
                mat[8]=float(fileo[n,counter])
        if c.lower() in["Na2O","na2o"]:
            if float(fr) in[0,0.0,0.00]:
                mat[9]=0.0001
            else:
                mat[9]=float(fileo[n,counter])
            #Fe2O3
        if c.lower() in["feo"]:
            if float(fr) in[0,0.0,0.00]:
                mat[10]=0.0001
            else:
                mat[10]=float(fileo[n,counter])
            mat[11]=0.0001
            mat[12]=0.0001
            mat[13]=0.0001
        n=n+1
    return (mat)
def outread (a,b,c):
    """Reads XTL files and exctracts first appearances of minerals into res.txt"""
    if os.path.exists (str(a)+"/res.txt"):
        fileo=np.loadtxt(str(a)+"/xtl"+str(c)+".txt",dtype='str',delimiter="\t",unpack=False)
        x=fileo [1:,1:]
        x=x.astype(np.float)
        # print (x)
        g=1
        l=0
        mat=[b,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for t in x[0,1:]:
            for f in x[0:,g]:
                # print (f)
                if f!=0:
                    mat[g]=x[l,0]
                    # g=g
                    break
                l=l+1
            g=g+1
            l=0
        filex=open(str(a)+"/res.txt","a")
        filex.write(str(mat[0])+"\t"+str(mat[1])+"\t"+str(mat[2])+"\t"+str(mat[3])+"\t"+str(mat[4])+"\t"+str(mat[5])+"\t"+str(mat[6])+"\t"+str(mat[7])+"\t"+str(mat[8])+"\n")
        filex.close()
    else:
        fileo=np.loadtxt(str(a)+"/xtl"+str(c)+".txt",dtype='str',delimiter="\t",unpack=False)
        x=fileo [1:,1:]
        x=x.astype(np.float)
        # print (x)
        g=1
        l=0
        mat=[b,0,0,0,0,0,0,0,0,0,0,0]
        for t in x[0,1:]:
            for f in x[0:,g]:
                # print (f)
                if f!=0:
                    mat[g]=x[l,0]
                    # g=g
                    break
                l=l+1
            g=g+1
            l=0
        filex=open(str(a)+"/res.txt","x")
        filex.write("pressure\tforsterite\tXanorthite\twollastonite-cpx\tenstatite-cpx\twollastonite-opx\tenstatite-opx\twollastonite-pig\tenstatite-pig\n")
        filex.write(str(mat[0])+"\t"+str(mat[1])+"\t"+str(mat[2])+"\t"+str(mat[3])+"\t"+str(mat[4])+"\t"+str(mat[5])+"\t"+str(mat[6])+"\t"+str(mat[7])+"\t"+str(mat[8])+"\n")
        filex.close()
def GMTplot (a):
    """Plots phase diagrams using a GMT file"""
    for Sample in a[0,1:]:
        Sample_Folder="Results/"+str(Sample)
        shutil.copy("plot.sh",str(Sample_Folder)+"/plot.sh")
        subprocess.Popen(str(Sample_Folder)+"/./plot.sh")
def remover():
    """Removes the original MAGPOX result files"""
    if os.path.exists("INPUTER.txt"):
        os.remove("INPUTER.txt")
    if os.path.exists ("MAGPOX.XTL"):
        os.remove("MAGPOX.XTL")
    if os.path.exists ("MAGPOX.WFX"):
        os.remove("MAGPOX.WFX")
    if os.path.exists ("MAGPOX.LIQ"):
        os.remove("MAGPOX.LIQ")
    if os.path.exists ("MAGPOX.DAT"):
        os.remove("MAGPOX.DAT")
def init():
    """Removes old folders and input textfiles"""
    if os.path.exists("Results"):
        shutil.rmtree("Results")
    if os.path.exists("INPUTER.txt"):
        os.remove("INPUTER.txt")
    os.mkdir("Results")
def plotrem(Sample_Folder):
    """Removing sh,ps and pdf files created with the GMTplot function"""
    if os.path.exists(str(Sample_Folder)+"/plot.sh"):
        os.remove(str(Sample_Folder)+"/plot.sh")
    if os.path.exists(str(Sample_Folder)+"/plot.ps"):
        os.remove(str(Sample_Folder)+"/plot.ps")
    if os.path.exists(str(Sample_Folder)+"/plot.pdf"):
        os.remove(str(Sample_Folder)+"/plot.pdf")
def runner (File_Name,maxP,minP,inc,crx_rate=0.01,crx_max=0.99,wsl=True):
    """Main Algorithm for running MAGPOX and file processing"""
    fileo=np.loadtxt(File_Name,dtype='str',delimiter="\t",unpack=False)
    j=1
    init()
    for Sample in fileo[0,1:]:
        os.mkdir("Results/"+str(Sample))
        Sample_Folder="Results/"+str(Sample)
        plotrem(Sample_Folder)
        for Pressure in range(minP,maxP+inc,inc):
            #Removing any remnant files
            remover()
            
            #Creating the MAGPOX readable Input file
            Comps=input(File_Name,j)
            filex=open("INPUTER.txt","x")
            filex.write("today"+"\n"+"2"+"\n"+str(Sample)+"\n"+str(Comps[0])+"\n"+str(Comps[1])+"\n"+str(Comps[2])
            +"\n"+str(Comps[3])+"\n"+str(Comps[4])+"\n"+str(Comps[5])+"\n"+str(Comps[6])+"\n"+str(Comps[7])+"\n"+str(Comps[8])
            +"\n"+str(Comps[9])+"\n"+str(Comps[10])+"\n"+str(crx_rate)+"\n"+str(crx_max)+"\n"+str(float(Pressure))+"\n"+"2")
            filex.close()

            #Running MAGPOX
            if wsl==True:
                a=subprocess.Popen("bash -c './a.out'")
                a.wait()
            if wsl==False:
                a=subprocess.Popen("./a.out")
                a.wait()
            print("finished")

            #Copying Files to results folder on another format
            shutil.copy("MAGPOX.XTL","Results/"+str(Sample)+"/xtl"+str(Pressure)+".txt")
            xtl=open("Results/"+str(Sample)+"/xtl"+str(Pressure)+".txt", "r",encoding="ISO-8859-1")
            data=xtl.read()
            data= data.replace(" ","")
            xtl.close()
            xtl=open("Results/"+str(Sample)+"/xtl"+str(Pressure)+".txt","w")
            xtl.write(data)
            xtl.close()
            shutil.copy("MAGPOX.LIQ","Results/"+str(Sample)+"/liq"+str(Pressure)+".txt")
            shutil.copy("MAGPOX.DAT","Results/"+str(Sample)+"/dat"+str(Pressure)+".txt")
            shutil.copy("MAGPOX.WFX","Results/"+str(Sample)+"/wfx"+str(Pressure)+".txt")

            #Processing the Files
            outread(Sample_Folder,Pressure,Pressure)
            
        j=j+1
def plot (file):
     fileo=np.loadtxt(file,dtype='str',delimiter="\t",unpack=False)
     for Sample in fileo[0,1:]:
        Sample_Folder="Results/"+str(Sample)
        diagram_file=Sample_Folder+"/res.txt"
        diagram_dataframe=pd.read_csv(diagram_file,delimiter="\t")

        pressure=diagram_dataframe.get("pressure").astype(float)*0.1
        forsterite=diagram_dataframe.get("forsterite").astype(float)
        anorthite=diagram_dataframe.get("Xanorthite").astype(float)
        cpx=diagram_dataframe.get("wollastonite-cpx").astype(float)
        opx=diagram_dataframe.get("wollastonite-opx").astype(float)
        pig=diagram_dataframe.get("wollastonite-pig").astype(float)

        fig=plt.figure()
        plot1=fig.subplots()
        plot1.plot(pressure,forsterite,"ro")
        plot1.plot(pressure,anorthite,"yo")
        plot1.plot(pressure,cpx,"go")
        plot1.plot(pressure,opx,"o",color="purple")
        plot1.plot(pressure,pig,"go")
        plot1.set_ylim(1000,1700)
        plt.show()



# Conditions (see runner function)
pmin=2
pmax=30
inc=2
file="comp.txt"

# Steps and max crystallization are defaulted to 0.01 and 0.99 in the runner function, 
# they can be adjusted by changing the default values of crx_rate and crx_max default values of the runner function
# For Example: runner (fle,pmax,pmin,inc,crx_rate=0.05,crx_max=0.7)

# Commands are also defaulted to Windows operating with the WSL, the command can be changed in the wsl argument 
# in the runner function
# For Example: runner(fle,pmax,pmin,inc, wsl=False) would be appropriate to run it on Linux

runner(file,pmax,pmin,inc)
plot(file)
#Add Post-Processing (e.g. plotting function)