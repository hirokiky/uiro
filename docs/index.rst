.. uiro documentation master file, created by
   sphinx-quickstart on Sun Nov  3 12:53:04 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Uiro framework documentation
================================

le Web framework.

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
On next step, you can create your first project through :doc:`intro` documentation.
In this doc, you can create an application package, not just for a example.

To learn more about Uiro browse these topics:

.. toctree::
   :maxdepth: 2

   intro
   views
   matching
   db
   templates
   static
   config
   commands
   multipackages
   modules
