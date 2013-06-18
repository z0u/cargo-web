The Cargo Website
=================

Installing requirements
-----------------------

There are a few steps you'll need to perform once to work with this website::

1. Install the required system packages::

       $ sudo apt-get install fabric python-pip python-virtualenv

2. Create a Python virtual environment to store downloaded packages in::

       $ mkdir ~/.virtualenvs
       $ virtualenv ~/.virtualenvs/cargo

3. Download and install the required Python packages::

       $ pip install -r cargo_web/requirements.txt

   This refers to the `requirements.txt` file in the website directory.


Building the website
--------------------

Before you build the website, you need to first activate the virtual
environment::

    $ source ~/.virtualenvs/cargo/bin/activate

Then run Pelican to build the static website from your source files::

    $ pelican

