# 2023_Gupta
Code associated with the submitted publication of Ayantika Sen Gupta, for 1) Finding pairs of peaks in CenpA, 2) Cropping and aligning them, 3) Analyzing the spatial intensity distribution.

Pipeline combines processing in FiJi and python.  FiJi should have the "Stowers" package module installed from the manager.

1.  Hand annotate pairs of peaks in the original images using FiJi and save roi .zip files.  Alternatively can run PeakFinder.ipynb as a jupyter notebook to generate these zip files automatically (you will likely need to tweak some parameters in the find_peaks_in_file function).

2. With an image and its corresponding ROI list opened:  run 1-roi_macro_v2.ijm in FiJi to get the cropped areas that have corresponding point ROIs added to them.

3. Within FiJi run a second macro:  2-fit_spots_python.py which will align the individual peak pairs.

4.  Run spa_sim_alignment.ipynb as a jupyter notebook to perform merging, filtering, and kymograph analysis.

Written by Jay Unruh and Sean McKinney of the Stowers Institute for Medical Research
