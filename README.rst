The Cargo Website
=================

For better or worse, this is a website built with the Pelican static website
generator.

Put standard pages in the `content/pages` directory as Markdown or
reStructuredText. Put blog entries at the root of `content`. These are then
turned into HTML by Pelican and dumped into the `output` directory.

The custom HTML on the home page as well as the other branding and CSS is in
`themes`.

Installing requirements
-----------------------

There are a few steps you'll need to perform once to work with this website::

1. Install the required system packages::

       $ sudo apt-get install fabric python-pip python-virtualenv \
         virtualenvwrapper

2. We'll install the relevant Python packages into a virtualenv. You can do this
   using the standard `virtualenv` command, but `virtualenvwrapper` makes it a
   little easier by providing the `mkvirtualenv` and `workon` commands.

   Create a Python virtual environment to store downloaded packages in::

       $ mkvirtualenv cargo

3. Now activate the virtual environment::

       $ workon cargo

   (This is actually done automatically by `mkvirtualenv`.)

3. Download and install the required Python packages::

       (cargo)$ pip install -r cargo_web/requirements.txt

   This refers to the `requirements.txt` file in the website directory.


Building the website
--------------------

Before you build the website, you need to first activate the virtual
environment as above.

Then we run Pelican to build the static website from your source files. There's
a single command way to do this, but I've found it a bit unreliable.

In one shell run the command to watch the source files and rebuild the static
pages into the `output` directory::

    (cargo)$ make regenerate

In another, run the mini web-server that serves the files from `output`::

    (cargo)$ make serve

You can now browse the site at `http://localhost:8000/`.


Uploading the website
---------------------

    $ rsync -avz --exclude=releases output/ cargo-web@lille.sturm.com.au:/home/web/cargo/htdocs


Uploading software releases
---------------------------

    $ rsync -avz --progress *.zip *.bz2 cargo-web@lille.sturm.com.au:/home/web/cargo/htdocs/static/releases/

