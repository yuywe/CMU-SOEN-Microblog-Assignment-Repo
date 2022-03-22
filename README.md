# Overview

The ability to dive into an unknown code base and be productive immediately is an extremely valuable skill for software engineers.  One of the best ways to get acquainted with a new code base is to try to fix a bug: fixing a bug requires that the engineer be able to identify the actual bug and reproduce it, localize that bug using a debugging methodology, identify why the bug is occurring, and resolve that bug.

In this assignment, you will be provided with a version of the microblog that contains a bug that is causing users of the microblog trouble with using the service. You've received several bug reports, but these bugs reports vary.

1. Some of the users are reporting problems with logging into the site after changing their passwords.
2. Some of the users are reporting problems with logging into the site from a new computer.
3. Observability metrics, however, show that many of the users are still able to use the microblog and continue to post new updates multiple times during the day.

Your task: identify the bug in the application and resolve the bug.  In order to do this, you should think about this as a multi-step process:

1. Using a local copy of the microblog, try to reproduce the issue reported by the users to verify that the bug reports are valid.  
2. Once you are able to reproduce the issue, you should focus on localizing the bug: using the techniques discussed in the lecture components on code archaeology, try to identify where the application is going wrong.  You may find it useful to write a regression test that can be used to reproduce the issue, so you do not have to do this step manually.
3. Once you have identified the bug, apply your fix and verify that the fix resolves the issue.

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

1. Push your changes to your repo and go to the Gradescope assigment entitled Module 2: Bug Fixes
2. Click the _Submit Assignment_ button (or _Resubmit Assignment_ button if you are submitting a second attempt)
3. Click the _GitHub_ submission method
4. Log into your GitHub account (if you have not done so already)
5. Select your repository for this class, likely the _CMU-SOEN-Microblog-Assignemnt-Repo_, under the _Repository_ drop down, and under the _Branch_ drop down select _module2-bug-fixes_ branch
6. Click upload and wait for the results of the autograder