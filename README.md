## Installation Instructions

### Prerequisites 

_Provided are instructions for Mac OS X and Linux; if you're on Windows, we recommend you use the Windows Subsystem for Linux (WSL) and follow the Linux instructions._

1. If you don't have Python 3 installed already, follow the instructions below.  On all OS's, you can see if you have Python 3 installed by running `python3 --version`.  If you have Python 3 installed, you can skip to the next step.

* If you are using Linux or WSL in Windows, use the following [instructions](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server).  
* If you are on Mac OS X, first make sure you have [Xcode](https://developer.apple.com/xcode/) installed.  Next, install the Xcode command-line tools using the following command `xcode-select --install`.  Then, use the following [instructions](https://opensource.com/article/19/5/python-3-default-mac) on making Python 3 the default Python environment.

2. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

### Jupyter Notebook

_All starter code for all of the assignments is available through Gradescope._

1. Clone the repository from Github (if not done already).

2. Switch the branch to module7-ml branch.

3. Create and activate a virtual environment for Python.  This should be run in your terminal.

```sh
python3 -m venv venv && source venv/bin/activate
```

4. Install the required Python dependencies.

```sh
pip3 install -r requirements.txt
```

5. Install scikit-learn.  If you have a Windows, Linux, or Mac _without_ the M1 chip, you can follow the instructions [here](https://scikit-learn.org/stable/install.html).  If you do have a Mac with an M1 chip, you can follow these steps:

```sh
python3 -m pip install --no-cache --no-use-pep517 pythran cython pybind11 gast"==0.4.0"

python3 -m pip install --pre -i https://pypi.anaconda.org/scipy-wheels-nightly/simple scipy

python3 -m pip install --no-use-pep517 scikit-learn"==1.0.0"
```

6. Install Lime.

```sh
pip3 install lime
```

7. Restart your IDE.

8. Setup flask application and environment.

```sh
export FLASK_APP=hello
export FLASK_ENV=development
```

8. Run the flask application.

```sh
python3 -m flask run
```

9. Verify you can access the predictor service using your web browser by navigating to the predictor at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## FAQ
* If you run into any issues with installing Python 3 or running the code itselfon a Mac, you may need to uninstall and reinstall xcode to get the latest version.  Some instructions for how to do so are [here](https://inthetechpit.com/2019/12/31/how-to-clean-uninstall-xcode-on-mac/).
* If you run into any issues with using scikit-learn after you install it (especially on a Mac with an m1 chip), try uninstalling and reinstalling numpy ```sh
pip3 uninstall numpy
pip3 install numpy
```
uninstalling scikit-learn
```sh
pip3 uninstall scikit-learn
```
and follow the instructions to install scikit-learn again.  Make sure to restart you IDE after performing this.
