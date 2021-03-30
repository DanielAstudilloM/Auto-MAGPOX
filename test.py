import os
import subprocess
if os.path.exists ("MAGPOX.XTL"):
    os.remove("MAGPOX.XTL")
if os.path.exists ("MAGPOX.WFX"):
    os.remove("MAGPOX.WFX")
if os.path.exists ("MAGPOX.LIQ"):
    os.remove("MAGPOX.LIQ")
if os.path.exists ("MAGPOX.DAT"):
    os.remove("MAGPOX.DAT")
# if os.path.exists ("FXMOLIQ.DAT"):
    # os.remove("FXMOLIQ.DAT")
# if os.path.exists ("FXMORXN.DAT"):
    # os.remove("FXMORXN.DAT")
# if os.path.exists ("FXMOTREL.DAT"):
    # os.remove("FXMOTREL.DAT")
# if os.path.exists ("FXMOTRM.DAT"):
    # os.remove("FXMOTRM.DAT")

# a=subprocess.Popen("./a.out")

print("finshed")
