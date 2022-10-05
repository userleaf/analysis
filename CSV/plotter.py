from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import os

os.system("rm *.png")
result = subprocess.run(['ls'], stdout=subprocess.PIPE)
scans=result.stdout.decode('utf-8')
scans=scans.split('\n')[:-1]
try:
    scans.remove('plotter.ipynb')
    scans.remove('plotter.py')
except:
    pass

for scan in scans:
    data = np.genfromtxt(scan, delimiter=',')
    result = subprocess.run(['head','-20',f'{scan}'], stdout=subprocess.PIPE)
    head=result.stdout.decode('utf-8')
    head=head.split('\n')[:-1]
    plt.title(scan[:-4])
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity (a.u.)')
    for i in range(1,len(head)):
        plt.text(1, i*0.05, head[i][:-2], transform=plt.gca().transAxes,fontsize=8, color='gray', horizontalalignment='right', verticalalignment='center')
        # show head as text
    # save high resolution image
    plt.plot(data[:,0], data[:,1], color='red')
    plt.savefig(f'{scan[:-4]}.png', transparent=False, dpi=300, bbox_inches="tight")
    plt.clf()