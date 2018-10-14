# Python BIOGEME - A Docker on Windows tutorial

The goals of this repository are twofold:
 * Create an updated version of a python biogeme docker image, and to maintain
 that image updated
 * Create a tutorial for windows users to be able to use Biogeme without the
 manual steps and overheads of a full virtual box

# The docker image

It is a basic linux image of Python 3.6, to which we install only BIOGEME,
enabling Python Biogeme

All the steps below assume that you have created your Biogeme image by cloning or downloading this repository to 
 your local machine and running the following command on the root of the folder
 
 Also, this should work on ANY operating system that supports Docker, although there are no many reasons to use Docker
 for BIOGEME estimation if you are on Linux or MacOS.

**docker build -t biogeme .**

# Running a generic BIOGEME script

After the biogeme image has been created, it is ready to be used on any command interface of your liking.

Let's assume that you have a PythonBiogeme file called **estimate.py** and a dataset called **dataset.dat** and 
that they are both on the same D:/biogeme/  

In order to run PythonBiogeme using docker, you just need to run the following command on your command prompt:

**docker run -v D:/BIOGEME://tmp/mr -w //tmp/mr biogeme pythonbiogeme estimate dataset.dat**

Note that the folder separator is **always** LINUX one   **/** and not **\\**, regardless of the operating system you 
are working on.

However, if you are not working on Windows, you will need a single **/** after the **:**, which makes

**docker run -v D:/BIOGEME:/tmp/mr -w /tmp/mr biogeme pythonbiogeme estimate dataset.dat**

# A more complete documentation

For a better overview of what motivated the creation of this repo, you can go to 
[my blog.](http://www.xl-optim.com/biogeme-docker)



# Credits

This repository draws heavily on the work done by
[fraukeseidel](https://github.com/fraukeseidel/python-biogeme)
The original docker spec used Python 3.4 and biogeme 2.4, and we update the
Python and biogeme versions to 3.6 and 2.6a respectivelly
