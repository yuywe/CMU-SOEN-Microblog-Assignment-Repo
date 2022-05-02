# Microblog: Static Analysis

_This assignment matches up with the final assessment in Module 6 on quality assurance and testing._

## Learning Goals

The learning goals of this assignment are:

1. Apply a static analysis tool on a real-world open-source code base in order to detect bugs and code smells.

2. Identify false positive results in the analysis, if present.

3. Evaluate a particular static analysis tool on a real-world open-source code base.

## Overview

As discussed in this module, automated static and dynamic analysis are useful techniques for ensuring high code quality when delivering software at scale.  In this assignment, we are going to look at one particular static analysis tool and how it operates on the microblogging platform.

The tool we are going to use for this assignment is [Flake8](https://flake8.pycqa.org/en/latest/), a tool for enforcing a style guide.  We recommend that you review the tool's documentation at the link provided above.

For this assignment, you should run Flake8 on a copy of the microblog (on the app folder in particular).  Flake8 will detect a number of issues that will need to be resolved in the application, and you'll need to either ignore any *false positives*, if they exist, and address the list of legitmate style violations.  You should not ignore any error that is not a false positive, and you should address all of the legitimate style violations.

**NOTE** running flake8 will produce some false positives.  Some of these false positives will have a very noticeable pattern (i.e. they might all occur in a similar type of file...).  However, to get full points, you cannot have any output from running flake8 on the app folder.  To deal with this, you might want to look into using a .flake8 folder with a per-file-ignores section.  See the documentation [here](https://flake8.pycqa.org/en/latest/user/options.html?highlight=per-file-ignores#cmdoption-flake8-per-file-ignores) for an example of what this could look like.  You may need to do some more research on your own to figure out exactly what you need.

Once this is completed, you should write a reflection that answers the following questions:

1. Did you find the warnings and errors produced by Flake8 relevant?  Why or why not?

2. _Requirements:_ We have previously discussed auditing tools and the requrements that influence them.  For Lighthouse, this was the WAI-ARIA accessibility requirement.  What is it for Flake8?  Does it identify any other problems outside of that?

3. Would you use this in your organization?  If so, why?  If not, why not? 

# Installation Instructions

## Prerequisites 

_Provided are instructions for Mac OS X and Linux; if you're on Windows, we recommend you use the Windows Subsystem for Linux (WSL) and follow the Linux instructions._

1. If you don't have Python 3 installed already, follow the instructions below.  On all OS's, you can see if you have Python 3 installed by running `python3 --version`.  If you have Python 3 installed, you can skip to the next step.

* If you are using Linux or WSL in Windows, use the following [instructions](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server).  
* If you are on Mac OS X, first make sure you have [Xcode](https://developer.apple.com/xcode/) installed.  Next, install the Xcode command-line tools using the following command `xcode-select --install`.  Then, use the following [instructions](https://opensource.com/article/19/5/python-3-default-mac) on making Python 3 the default Python environment.

2. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Microblog

_All starter code for all of the assignments is available through Gradescope._

1. Download the assignment's starter code from Gradescope.

2. Change directory into the start code example directory.

3. Create and activate a virtual environment for Python.  This should be run in your terminal.

```sh
python3 -m venv venv && source venv/bin/activate
```

4. Install the required Python dependencies.

```sh
pip3 install -r requirements.txt
```

5. Setup the database for the Flask service.

```sh
flask db upgrade && flask translate compile
```

6. Run the flask application.

```sh
python3 -m flask run
```

7. Verify you can access the application using your web browser by navigating to the microblog at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

# Submission Instructions

1. Push your changes to your repo and go to the Gradescope assigment entitled Module 6: Static Analysis
2. Click the _Submit Assignment_ button (or _Resubmit Assignment_ button if you are submitting a second attempt)
3. Click the _GitHub_ submission method
4. Log into your GitHub account (if you have not done so already)
5. Select your repository for this class, likely the _CMU-SOEN-Microblog-Assignemnt-Repo_, under the _Repository_ drop down, and under the _Branch_ drop down select _module6-static-analysis_ branch
6. Click upload and wait for the results of the autograder