# Microblog: Feature Implementation

_This assignment matches up with the final assessment in Module 3 on feature implementation.  The students will implement the features required by the two smaller user stories._

## Learning Goals

The learning goals of this assignment are:

1. Implement features in an existing real-world, open-source application from a user story.

2. Analyze and revise previous estimates based on increased domain knowledge.

## Overview

Now it's time to get to work!  In this assignment, we are going to have you actually implement new features in the microblogging application. 

For this task, we are going to have you implement the two smaller features mentioned in the previous assignments.

The user stories for those features are the following:

1. As a user of the microblog, in order to allow me to change my personal e-mail address, I should be able to update my e-mail address on the profile editing page of the microblog.

2. As a user of the microblog, in order to allow me to login faster, I should be able to login with my e-mail address or my username.

With these user stories, we want you to first come up with an estimate for how long you think these tasks will take.  Then, we want you to actually implement these stories.  Lastly, we want you to compare the time it took to actually implement the features back to your initial estimate.

### Tips

Here are some tips for implementing these features:

1. You may find it useful to start your work by identifying how the existing features work (e.g., login, e-mail addresses) before trying to make your modifications.  When doing this, think back to the code archaeology techniques we discussed earlier this module.

2. We encourage you to think early and often about how you will validate your changes either through manual or automated testing.  Automated testing is a useful investment early on if you expect to run your tests often.

3. Any input from the user should be validated to ensure it's properly formatted.

4. For the error message for an invalid email, make sure the error message is "Please format your email address correctly.", otherwise your test will not pass.

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

1. Push your changes to your repo and go to the Gradescope assigment entitled Module 3: New Features
2. Click the _Submit Assignment_ button (or _Resubmit Assignment_ button if you are submitting a second attempt)
3. Click the _GitHub_ submission method
4. Log into your GitHub account (if you have not done so already)
5. Select your repository for this class, likely the _CMU-SOEN-Microblog-Assignemnt-Repo_, under the _Repository_ drop down, and under the _Branch_ drop down select _module3-new-features_ branch
6. Click upload and wait for the results of the autograder