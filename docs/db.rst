Connectiong to RDBs using SQLAlchemy
====================================

Uiro depends on SQLAlchemy_, a powerful ORM for python.
It only provides these features:

* Base class and Session for SQLAlchemy_ to write models
* Specifying zope.sqlalchemy_ extention
* A command to create tables
* Setting about database by .ini file

Creating your Model
-------------------

It's same with SQLAlchemy_.
Just using Base/Session provided by Uiro to creating tables automatically.

.. code-block:: python

    import sqlalchemy as sa
    from uiro.db import Base, Session

    class MyModel(Base):
        __tablename__ = 'mymodel'
        query = Session.query_property()

        id = sa.Column(sa.Integer, primary_key=True)
        name = sa.Column(sa.String(255))

        def __init__(self, name):
            self.name = name

And using like this:

.. code-block:: python

    >>> import transaction
    >>> with transaction.manager:
    ...     Session.add(MyModel(name='spam'))

You can see SQLAlchemy_ and zope.sqlalchemy_
documentation to learn more.

Create tables by initdb command
-------------------------------

You can initialize DB with following gearbox command:

.. code-block:: sh

    gearbox initdb

This command is to create tables to specified database.

Setting about database to use
-----------------------------

To change database to use, specify that URL to `sqlalchemy.url` setting in .ini file::

    sqlalchemy.url = sqlite:///default.db

.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _zope.sqlalchemy: https://pypi.python.org/pypi/zope.sqlalchemy
