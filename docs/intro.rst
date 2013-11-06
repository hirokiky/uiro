Starting your first package
============================

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

What files are in your package?
-------------------------------

Your package must contain these packages::

    .
    ├── packagename
    │   ├── __init__.py
    │   ├── views.py
    │   ├── matching.py
    │   ├── models.py
    │   ├── templates
    │   │   └── top.mako
    │   └── static
    │       └── uiro.css
    ├── development.ini
    ├── setup.py
    ├── README.rst
    ├── CHANGES.txt
    └── MANIFEST.in

:views.py:
    Module to store Controllers which bundles each Views.

    See :doc:`views` documentation.

:matching.py:
    Entry point for each Controllers, specifying which Controller should be called
    corresponds to URL gave by clients.

    See :doc:`matching` documentation.

:models.py:
    Module to store Models, which is abstraction layer for structuring and manipulating the database.
    Uiro framework depends on SQLAlchemy_, you can write your own Models by SQLAlchemy_ more easily.

    See :doc:`db` documentation.

:templates:
    Directory to store mako templates.
    Templates will be collected automatically.
    The top.mako template can be picked up as a signature like 'packagename:top.mako'.

    See :doc:`templates` documentation.

:static:
    Directory to store static files.
    Static files will be also collected automatically and served, so you should not handle them manually.
    The uiro.css file will be in /static/packagename/uiro.css, and the link can be generated, using request.matching.

    See :doc:`static` documentation.

:development.ini:
    Configation file for WSGI application.
    It specifies that which Matching to use, which Database to connect and so on.

    See :doc:`config` documentation.

:setup.py:
    Builder your package, which usually tells you that the module/package you are about
    to install have been packaged and distributed.

    See `setuptools <http://pythonhosted.org/setuptools/>`_ documentation.

:MANIFEST.in:
    File to specify which file should be contained in package.

:CHANGES.txt:
    Text file to describe your package's change logs.

:README.rst:
    README file for your package.

.. _SQLAlchemy: http://www.sqlalchemy.org/
