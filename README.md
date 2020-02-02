# Exchange Rate Currency Conversion Microservice 

This is a currency exchange microservice written using a Test Driven Development (TDD) approach in Python3.

## Install the pre-requisites

1. Python version 3
1. Pipenv - Python virtual environment

## Installation steps
### 1. Python3
Make sure you have Python installed and it's availible from your command line. You can check if it's installed and determine it's version by running:
```sh
python --version
```
You shoud get some output like `3.6.2`  If you don't have this version of Python, please install the latest `3.x` version.

To install python 3 on a Mac
```sh
brew install python3
```
<details><summary><strong>Installation of Python3 on other platforms</strong></summary>
To [install Python3 on RHEL](https://developers.redhat.com/blog/2018/08/13/install-python3-rhel/)

To [install Python3 on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-18-04-server)

To [install Python3 on Windows](https://phoenixnap.com/kb/how-to-install-python-3-windows)

To install Python on any other platform take a look at the [Installing Python](https://docs.python-guide.org/starting/installation/) section of ***The Hitchhikers Guide to Python*** or refer to [python.org](http://python.org)
</details>

### 2. Pipenv - Python virtual environment


To check you have pipenv installed run the following:
```sh
pipenv --version
```
You should see something like `version 2018.11.26` if not please setup the latest version of pipenv as follows.

To install pipenv on a Mac using brew
```sh
brew install pipenv
```
<details><summary><strong>Installation of Pipenv on other platforms</strong></summary>

> If you have a working installation of pip, and maintain certain “toolchain” type Python modules as global utilities in your user environment, pip user installs allow for installation into your home directory. Note that due to interaction between dependencies, you should limit tools installed in this way to basic building blocks for a Python workflow like virtualenv, pipenv, tox, and similar software.

To install pipenv on anyplatform with `pip`
```sh
pip install --user pipenv

#or
# todo: validate this
python3 -m pip install pipenv

```

For more detailed instruction [see here](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv)
</details>

It is a best practice to use use Python virtual environments to isolate project-specific dependencies and create reproducible environments.



<details><summary><strong>Read more about Pipenv and Virtual Environments</strong></summary>

### Pipenv Features
* Pipenv is a production-ready tool that aims to bring the best of all packaging worlds to the Python world. It harnesses Pipfile, pip, and virtualenv into one single command.

* Enables truly ***deterministic builds***, while specifying only what is needed.

* With pipenv you no longer need to use `pip` and `venv` separately.


*  Setting a virtual environment to separate each project from affecting other projects and the rest of your operating system's a good idea. You may be making changes in your virtual environment that could have unintended consequences. 

Learn more about Pipenv [here](https://pipenv-fork.readthedocs.io/en/latest/)
</details>


### Intializing a `pipenv` Python Virtual Environment

How does one setup a Python Virtual Environment using `pipenv`?

Option A:
> Installing a pypi library with `pipenv` will automatically create a virtual enviroment

Here is how to do it.

What library to start off with?  Since this microservice will make http requests to an external 3rd party REST endpoint, we decided to use the popular  `requests` library.

At your command line cd to the root directoryof the currency exchange.
```sh
cd src/currencyexchange
pipenv install requests
```

The output for installing `requests` lib is:
![requests install via pipenv](./doc/images/pipenv-install-requests.png)

So great!  Now pipenv ran, installed `requests` and created a `Pipfile` and a `Pipfile.lock` 

Check!
```sh
pipenv check
```

Output should confirm all is good!

![check with pipenv](./doc/images/pipenv-check.png)

You can also confirm the virtual environment is setup by confirming a new file called `Pipfile` exists at the root directory. 

Even though the `pipenv` virtual environment is setup, you still need to ***activate*** it.  This is simplly


## Anatomy of this application
### Key runtime packages
* HTTP Client
  * `requests` http library to call external http API endpoints



# License

This code is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)

