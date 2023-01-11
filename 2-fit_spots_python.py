from ij import IJ,WindowManager
import jguis.PlotWindow3D as pw3D
import jguis.Traj3D as t3D
from ij.plugin.frame import RoiManager
import math
import os

#dir=IJ.getDir('current')
dir='S:/micro/jeg/as2355/20220929/10032022/'
zratio=3.2
thickness=60
#print(os.listdir(dir))
#print(dir)
imgnames=WindowManager.getImageTitles()
print(imgnames)
rman=RoiManager.getInstance()
if rman is None:
	rman = RoiManager()

for i in range(len(imgnames)):
	rman.reset()
	img=WindowManager.getImage(imgnames[i])
	WindowManager.setCurrentWindow(img.getWindow())
	newname=imgnames[i][:-3]+'.tif'
	img.setTitle(newname)
	IJ.run("To ROI Manager")
	img.setPosition(2,1,1)
	IJ.run("fit custom tub4 jru v1", "z_ratio="+str(zratio)+" x_stdev=1.95000 z_stdev=2.00000 calibrate? hide xz_width=20")
	WindowManager.getWindow("Profile 1").close()
	WindowManager.getWindow("Profile 2").close()
	WindowManager.getWindow("fit").close()
	WindowManager.getWindow("XZ Profile").close()
	IJ.saveAs(img,"Tiff",dir+newname)
	pimg=WindowManager.getImage("MultiGaus Plot")	
	IJ.run("thick 3D polyline profile jru v1", "3d=[MultiGaus Plot] z=["+newname+"] thickness="+str(thickness)+" z_ratio="+str(zratio)+" end=0 straighten ignore")
	reimg=WindowManager.getCurrentImage()
	realignname=newname[:-4]+"_realigned.tif"
	IJ.saveAs(reimg,"Tiff",dir+realignname)
	reimg.close()
	pimg.close()
	rman.reset()
	img.close()
	#break