//here we need to take point pairs, duplicate a box around them with an appropriate border
//then recreate single rois as overlays on the duplicated images
orig=getTitle();
border=30;
cnt=roiManager("count");
for(i=0;i<cnt;i+=2){
	selectWindow(orig);
	roiManager("Select", i);
	//Roi.getBounds(x,y,width,height);
	Roi.getCoordinates(xp,yp);
	xp=xp[0]; yp=yp[0];
	roiManager("Select", i+1);
	Roi.getCoordinates(xp2,yp2);
	xp2=xp2[0]; yp2=yp2[0];
	width=abs(xp2-xp);
	height=abs(yp2-yp);
	xc=0.5*(xp2+xp);
	yc=0.5*(yp2+yp);
	//x and y need to be the upper left (might not exist)
	x=round(xc-0.5*width);
	y=round(yc-0.5*height);
	print(""+x+" , "+y+" , "+width+" , "+height);
	//now expand appropriately
	x-=border;
	y-=border;
	width+=2*border;
	height+=2*border;
	makeRectangle(x,y,width,height);
	//roiManager("Add");
	run("Duplicate...", "duplicate");
	//now remake the rois as points on the duplicated image
	makePoint(xp-x,yp-y);
	Overlay.addSelection();
	makePoint(xp2-x,yp2-y);
	Overlay.addSelection();
}
