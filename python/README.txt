******************************
** PHOTONIC SENTRY CAPSTONE **
**  Benchmarking the PFMD   **
******************************

-------------AUTHORS--------------
	- Arush Sharma
	- Dylan Stockard
	- Tyler Wong
	- Quanchen Ding

-----------DESCRIPTION------------
	The Photonic Fence Monitoring Device (PFMD) was developed by Photonic Sentry to track and record the 3-dimensional movements of flying insects. Using stereoscopic infrared cameras in an environment with a retroreflective background to silhouette foreground targets, the PFMD can directly measure x and y position coordinates while calculating the z value.
	Our team was tasked with benchmarking the PFMD's z-position accuracy. We chose the z-position specifically since it is the axis that is not directly measured, so our assumption was that it would have the largest error.

----------SOFTWARE SETUP----------
	There are two python notebooks to use in order to replicate our results. In addition, you will need to download data and store it in the format detailed below for analysis.

	Data:
		You must follow this format in order for the code files to access and analyze the data. 
		1. Create a folder called "pfmd_data" in a known directory (you will paste this directory into the notebooks later)
		2. Within "pfmd_data", create another folder called "data". This is where our notebooks will read in data to analyze.
		3. Within "data", create a folder for each configuration, and name the folder as such. For example, your "data" folder might have three configuration folders named "z_up", "z_center", and "z_down". Our data is structured in this way so it is easy to load in specific configurations for analysis.
		4. Upload all data tracks you want to analyze as CSVs into their appropriate configuration folder. We recommend that you filter out noisy tracks/info when downloading from pfmd.net so the analysis only has data from the desired tracks. We have already done this in the track CSVs found on our GitHub.
		5. Back in the "pfmd_data" directory, include a CSV called "ground_truth_values.csv". This file will be used to map track CSVs to their session name and ground truth value. The "ground_truth_values.csv" file on our GitHub is updated for all of our z-position tracks, but note that you will need to add any future tracks to the "ground_truth_values.csv" file with its session name and ground truth value for analysis to work properly.
		

	pfmd_heatmap.pynb:
		This notebook generates the heatmap of the data to analyze the effects on z accuracy based on x and y position. If the data above is set up correctly, all you need to do is to get the absolute path to "pfmd_data" and store it into the PFMD_DATA_PATH. See the pfmd_heatmap.pynb notebook for more detailed information on what methods and analysis can be done. 

	pfmd_weight_analysis.pynb:
		This notebook looks at the weights calculated by the 1st order model and analyzes how they change from track-to-track. If the data above is set up correctly, all you need to do is to get the absolute path to "pfmd_data" and store it into the PFMD_DATA_PATH. See the pfmd_weight_analysis.pynb notebook for more detailed information on what methods and analysis can be done. 

	pfmd_3d_plots.pynb:
		This notebook generates interactive 3d visualizations of the data. It is similar to the function of pfmd.net, but with the ability to stack tracks on the same plot to compare more closely. If the data above is set up correctly, all you must do is to get the absolute path to "pfmd_data" and store it into the PFMD_DATA_PATH. See the pfmd_3d_plots.pynb notebook for more detailed information on what methods and analysis can be done. 
	
	pfmd_file_preprocessing.pynb:
      	This notebook will identify missing files and duplicated file names that can potentially throw errors. If the data above is set up correctly, all you must do is to get the absolute path to "pfmd_data" and store it into the PFMD_DATA_PATH. Run this notebook if you have errors or strange results while running the other notebooks.