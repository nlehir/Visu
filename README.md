# Visualization of massive data.
This repository contains slides and exercices for 5th year students at epitech for the course
"Visualization of massive data".

Scripts contains errors on the default "exercise" branch. These exercises are
material for students to work locally after cloning the repository.

The branch "correction" contains correct scripts. Students are encouraged to
work rather with the "exercise" branch during the module, in order to have the
time to look for the solutions, that are discussed during the course.

## Course outline

### Day 1
- definition of big data
- orders of magnitude
- definition of big data visualization
- data modelling
- supervised learning
- unsupervised learning
- hierarchical clustering
- reminders on random variables
- overfitting
- principal component analysis

### Day 2
- classical visualization methods
- scatter matrices
- parallel coordinate plots
- miscellaneous : radar plots, heat maps
- treemaps
- visualization platforms
- classification trees
- reliability, metrics, prediction errors
- advanced methods

## Jupyter notebooks
We can use the convenient jupyter notebooks during the course. 
This will allow us to run scripts in the browser.

### Installation
You need to have docker installed.
To install docker, please follow the instructions here:
https://docs.docker.com/get-docker/
The dockerfile sets the installation up.

### Build and launch by scripts
-   To build: ```./buildJupyterImage.sh```
-   To launch: ```./launchNotebookServer.sh```

### Open notebooks
Jupyter is a web app, to open your notebooks, open in your browser the following url:
http://localhost:8888/lab
