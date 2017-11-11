"""
Utilities
Set of basic utilities for HackWM
by Dylan Hamer
"""

import subprocess


def runProcess(process):
    print("Running: "+str(process))
    try:
        subprocess.Popen(process)
    except:
        print("An error occured while launching: "+process)


