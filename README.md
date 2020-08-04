# Py-School-Match

## Installation 
### Dependencies:
graph-tool (>= 2.27)
sudo apt install latexmk
sudo apt install texlive-full

### To create virtual environment:

conda create --name gt -c conda-forge graph-tool

conda activate gt - to switch to the environment

conda deactivate - to switch to base environment

### Now install graph tool after switching to the gt environment using below command:

conda install -c conda-forge graph-tool

1. install py-school-match using below command to run the package

	pip install py-school-match

2. clone git repository: git@github.com:ashmean3/CMSC6950_py_school_match_project.git\
	cd CMSC6950_py_school_match_project\
	type make to start execution and generate the output files

3. Move to data folder in the computer and look for output.csv file\
	output.csv file will contain the list of students and corresponding allocated schools along with students who are not assigned to a school.
