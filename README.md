# python-biogeme

This repository was created when we were estimating a series of discrete choice
models using a mix of datasets, most of which are proprietary formats and
can only be opned by software that is available for Windows only. At the same
time, the estimation software we had chosen was BIOGEME, which only runs
properly on unix-based systems.

As a consequence, the workflow had become unecessarily convoluted, and a better
alternative was needed. Due to the workflow and experimentation process we
had chosen, wereached a


The goals of this repository are twofold:
 * Create an updated version of a python biogeme docker image, and to maintain
 that image updated
 * Create a tutorial for windows users to be able to use Biogeme without the
 manual steps and overheads of a full virtual box



# The docker image

It is a basic linux image of Python 3.6, to which we install only biogeme,
enabling Python Biogeme


# Running your estimation script

The workflow we have defined assumes a set structure for the model estimation
runs, which are the following:

* The estimation files are the are **estimate.py** and **dataset.csv**
* Both files are in the same folder in computer where you are running your
docker image

As each person would have different workflows  

In the example below, the directory that holds all files is
**D:\my_folder**



To run the estimation
sudo docker run -v D:/my_folder:/tmp/mr -w /tmp/mr biogeme pythonbiogeme estimate dataset.csv

On Windows, double slashes on the Linux paths are needed

sudo docker run -v D:/my_folder://tmp/mr -w //tmp/mr biogeme pythonbiogeme estimate dataset.csv


This assumes that you built your docker image using

docker build -t biogeme .


# Credits

This repository draws heavily on the work done by
[fraukeseidel](https://github.com/fraukeseidel/python-biogeme)
The original docker spec used Python 3.4 and biogeme 2.4, and we update the
Python and biogeme versions to 3.6 and 2.6a respectivelly
