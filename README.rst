====
Uiro
====

le Web framework.

Uiro provides a foundation to create a pluggable Web application.
it suggest to use these packages to create third party apps (on uiro 0.1):

* webob==1.2.3
* gearbox==0.0.2
* matcha==0.3
* mako==0.9.0
* SQLAlchemy==0.8.2

To use these packages, Uiro (and it's third party app) users can
be free by version collisions.

.. warning::

  Uiro 0.1 is still Pre-alpha, not for production usage.

Installing
------------
Create your python env and install it from PyPI::

    pip install uiro

First project
----------------
After installing Uiro, 'gearbox' command will be available on your env.
You can manage projects and applications by using this command.
Now let's create your first Uiro package::

    gearbox create -n packagename

Above 'packagename' string should be replaced to some another name you want.

And then install created package::

   cd packagename
   python setup.py develop

This action makes your created package available on your env.

Then create SQLite DB as a file named 'default.db' to current dir::

    gearbox initdb

The setting for DB is written in development.ini, and some another
setting too, check it out.

Finally, you can serve your application, by `serve` command::

    gearbox serve

Then, you can run your web browser and access to localhost with port 8888
to confirm automatically created package is running.

Resources
=========
* `Repository <https://github.com/hirokiky/uiro/>`_
* `PyPI <http://pypi.python.org/pypi/uiro/>`_
