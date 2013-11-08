====
Uiro
====

le Web framework for Python.

Uiro provides a foundation to create a pluggable Web application.

* For creating a database-driven web application.
* Providing basict to create pluggable application.
* Designed to make user enable to use a lot of great WSGI libraries.

A simple Uiro application will be like this.

.. code-block:: python

    from wsgiref.simple_server import make_server
    from matcha import Matching, make_wsgi_app
    from uiro.controller import BaseController
    from uiro.view import view_config


    class Controller(BaseController):
        @view_config(method='get')
        def get_view(self, request, context):
            return 'Hello {name}!'.format(**request.matched_dict)

     matching = Matching('/hello/{name}', Controller())

    if __name__ == '__main__':
        app = make_wsgi_app(matching)
        server = make_server('0.0.0.0', 8888, app)
        server.serve_forever()

And setup.

.. code-block:: sh

    pip install uiro
    python hello.py

Now, you can visit http://localhost:8888/hello/world in a browser, you will see the text 'Hello world!'.

Next step
---------

Above example is too tiny to create a common-sensible Web application.
You can see `Uiro documentation <https://uiro.readthedocs.org/en/latest/>`_ and
learn more about Uiro

Dependents
----------

Uiro is Deciding necessary packages to avoid version collisions:

  * webob==1.2.3
  * gearbox==0.0.2
  * matcha==0.3
  * mako==0.9.0
  * SQLAlchemy==0.8.3

To use these packages, Uiro (and it's third party app) users can
be free by version collisions.

.. warning::

  Uiro 0.2 is still Pre-alpha, not for production usage.

Resources
=========
* `Repository <https://github.com/hirokiky/uiro/>`_
* `PyPI <http://pypi.python.org/pypi/uiro/>`_
* `Docs <https://uiro.readthedocs.org/>`_.
