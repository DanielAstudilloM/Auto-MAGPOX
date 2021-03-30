import os
import numpy as np
import shutil
import time
import subprocess
# import matlab.engine
#taking composition from file and setting the input file for magpox
def input(g):
    mat=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    fileo=np.loadtxt("comp.txt",dtype='str',delimiter="\t",unpack=False)
    n=0
    for c in fileo[:,0]:
        fr=fileo[n,g]
        if c.lower() in["SiO2","sio2"]:
            if float(fr) in[0,0.0,0.00]:
                mat[0]=0.0001
            else:
                mat[0]=float(fileo[n,g])
        if c.lower() in["TiO2","tio2"]:
            if float(fr) in[0,0.0,0.00]:
                mat[1]=0.0001
            else:
                mat[1]=float(fileo[n,g])
        if c.lower() in["Al2O3","al2o3"]:
            if float(fr) in[0,0.0,0.00]:
                mat[2]=0.0001
            else:
                mat[2]=float(fileo[n,g])
        if c.lower() in["Cr2O3","cr2o3"]:
            if float(fr) in[0,0.0,0.00]:
                mat[3]=0.0001
            else:
                mat[3]=float(fileo[n,g])
        if c.lower() in["FeO","feo"]:
            if float(fr) in[0,0.0,0.00]:
                mat[4]=0.0001
            else:
                mat[4]=float(fileo[n,g])
        if c.lower() in["MgO","mgo"]:
            if float(fr) in[0,0.0,0.00]:
                mat[5]=0.0001
            else:
                mat[5]=float(fileo[n,g])
        if c.lower() in["MnO","mno"]:
            if float(fr) in[0,0.0,0.00]:
                mat[6]=0.0001
            else:
                mat[6]=float(fileo[n,g])
        if c.lower() in["CaO","cao"]:
            if float(fr) in[0,0.0,0.00]:
                mat[7]=0.0001
            else:
                mat[7]=float(fileo[n,g])
        if c.lower() in["K2O","k2o"]:
            if float(fr) in[0,0.0,0.00]:
                mat[8]=0.0001
            else:
                mat[8]=float(fileo[n,g])
        if c.lower() in["Na2O","na2o"]:
            if float(fr) in[0,0.0,0.00]:
                mat[9]=0.0001
            else:
                mat[9]=float(fileo[n,g])
            #Fe2O3
            mat[10]=0.001
            mat[11]=0.0001
            mat[12]=0.0001
            mat[13]=0.0001
        
        # if c in["P2O3","p2o3"]:
            # if float(fr) in[0,0.0,0.00]:
                # mat[]=0.0001
            # else:
                # mat[9]=0.0001
        # if c in["",""]:
            # mat[11]=float(fileo[n,1])
        n=n+1
    return (mat)
def outread (a,b,c):
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
        filex.write(str(mat[0])+"\t"+str(mat[1])+"\t"+str(mat[2])+"\t"+str(mat[3])+"\t"+str(mat[4])+"\t"+str(mat[5])+"\t"+str(mat[6])+"\t"+str(mat[7])+"\t"+str(mat[8])+"\n")
        filex.close()
def plotter (a):
    for d in a[0,1:]:
        e="Results/"+str(d)
        shutil.copy("plot.sh",str(e)+"/plot.sh")
        subprocess.Popen(str(e)+"/./plot.sh")

fileo=np.loadtxt("comp.txt",dtype='str',delimiter="\t",unpack=False)
j=1
if os.path.exists("Results"):
    shutil.rmtree("Results")
if os.path.exists("INPUTER.txt"):
    os.remove("INPUTER.txt")
    # for d in fileo[0,1:]:
        # p=0
        # if os.path.exists("Results/"+str(d)):
            # if os.path.exists("results/"+str(d)+"/asde.txt"):
                # os.remove("results/"+str(d)+"/asde.txt")
            # if os.path.exists("results/"+str(d)+"/asdf.txt"):
                # os.remove("results/"+str(d)+"/asdf.txt")
            # if os.path.exists("results/"+str(d)+"/asdg.txt"):
                # os.remove("results/"+str(d)+"/asdg.txt")
            # if os.path.exists("results/"+str(d)+"/asdh.txt"):
                # os.remove("results/"+str(d)+"/asdh.txt")
            # if os.path.exists("input.txt"):
                # os.remove("input.txt")
            # if p!=0 and os.path.exists("results/"+str(d)+"/res.txt"):
                # os.remove ("results/"+str(d)+"/res.txt")
                # p=1
            # filex=open("input.txt","w")
            # filex.write("title = "+"'"+str(d)+"'"+"\n"+"CJ="+str(input(j)))
            # filex.close()
            # os.system("subpro.py")
            # shutil.copy("asde.txt","c:/users/ret64/desktop/prog/Results/"+str(d)+"/asde.txt")
            # shutil.copy("asdf.txt","c:/users/ret64/desktop/prog/Results/"+str(d)+"/asdf.txt")
            # shutil.copy("asdg.txt","c:/users/ret64/desktop/prog/Results/"+str(d)+"/asdg.txt")
            # shutil.copy("asdh.txt","c:/users/ret64/desktop/prog/Results/"+str(d)+"/asdh.txt")
            # j=j+1
        # else:
            # os.mkdir("c:/users/ret64/desktop/prog/Results/"+str(d))
            # if os.path.exists("input.txt"):
                # os.remove("input.txt")
            # filex=open("input.txt","w")
            # filex.write("title = "+"'"+str(d)+"'"+"\n"+"CJ="+str(input(j)))
            # filex.close()
            # os.system("subpro.py")
            # shutil.copy("asde.txt","c:/users/ret64/desktop/prog/Results/"+str(d)+"/asde.txt")
            # shutil.copy("asdf.txt","c:/users/ret64/desktop/prog/Results/"+str(d)+"/asdf.txt")
            # shutil.copy("asdg.txt","c:/users/ret64/desktop/prog/Results/"+str(d)+"/asdg.txt")
            # shutil.copy("asdh.txt","c:/users/ret64/desktop/prog/Results/"+str(d)+"/asdh.txt")
            # j=j+1

os.mkdir("Results")
for d in fileo[0,1:]:
    os.mkdir("Results/"+str(d))
    e="Results/"+str(d)
    if os.path.exists(str(e)+"/plot.sh"):
        os.remove(str(e)+"/plot.sh")
    if os.path.exists(str(e)+"/plot.ps"):
        os.remove(str(e)+"/plot.ps")
    if os.path.exists(str(e)+"/plot.pdf"):
        os.remove(str(e)+"/plot.pdf")
    for v in range(2,31,2):
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
        z=input(j)
        filex=open("INPUTER.txt","x")
        filex.write("today"+"\n"+"2"+"\n"+str(d)+"\n"+str(z[0])+"\n"+str(z[1])+"\n"+str(z[2])+"\n"+str(z[3])+"\n"+str(z[4])+"\n"+str(z[5])+"\n"+str(z[6])+"\n"+str(z[7])+"\n"+str(z[8])+"\n"+str(z[9])+"\n"+str(z[10])+"\n"+"0.01\n"+"0.99\n"+str(float(v))+"\n"+"2")
        filex.close()
        a=subprocess.Popen("bash -c './a.out'")
        a.wait()
        print("finished")
        # a=open("fxmotr_wfx.txt","r")
        # a.close()
        shutil.copy("MAGPOX.XTL","Results/"+str(d)+"/xtl"+str(v)+".txt")
        xtl=open("Results/"+str(d)+"/xtl"+str(v)+".txt", "r",encoding="ISO-8859-1")
        data=xtl.read()
        data= data.replace(" ","")
        xtl.close()
        xtl=open("Results/"+str(d)+"/xtl"+str(v)+".txt","w")
        xtl.write(data)
        xtl.close()
        shutil.copy("MAGPOX.LIQ","Results/"+str(d)+"/liq"+str(v)+".txt")
        shutil.copy("MAGPOX.DAT","Results/"+str(d)+"/dat"+str(v)+".txt")
        shutil.copy("MAGPOX.WFX","Results/"+str(d)+"/wfx"+str(v)+".txt")
        
        # shutil.copy("fxmotr_phys.txt","Results/"+str(d)+"/phys"+str(v)+".txt")
        # shutil.copy("fxmotr_inst.txt","Results/"+str(d)+"/inst"+str(v)+".txt")
        # time.sleep(5)
        outread(e,v,v)
        
        # os.remove("fxmotr_wfx.txt")
        # os.remove("fxmotr_liq.txt")
        # os.remove("fxmotr_xtl.txt")
        # os.remove("fxmotr_main.txt")
        # time.sleep(0.5)
    j=j+1
# plotter (fileo)