# 2023_Gupta
Code associated with the submitted publication of Ayantika Sen Gupta, for 1) Finding pairs of peaks in CenpA, 2) Cropping and aligning them, 3) Analyzing the spatial intensity distribution.

Pipeline combines processing in ImageJ and python.


	1. Hand annotates pairs of peaks in the original images using single point ROI tool and save .zip files.  
      Alternatively use PeakFinder.ipynb to find them automatically (will likely need to tweak some parameters in first 3 lines of find_peaks_in_file).  
	2. With an image and its corresponding ROI list opened:  run 1-roi_macro_v2.ijm in ImageJ to get cropped areas have ROI points burned into them.
	3. Run 2-fit_spots_python.py in ImageJ which will use "fit custom tub 4 jru v1" to fit gaussians to the two peaks located at the ROI focii and then rotate them about their midpoint to be vertically aligned and centered in a new X,Y,Z stack (using "thick 3D polyline profile jru v1") and saved
	4. Use spa_sim_alignment.ipynb to perform merging, filtering and analysis.

