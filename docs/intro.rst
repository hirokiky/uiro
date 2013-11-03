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

