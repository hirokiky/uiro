Serving static files
====================

Uiro prepares a feature to collect static files and serve it.
It will collect static files as same way for templates
(:doc:`templates`).

It will create an app for serving static files and register
in in URL dispatcher.
Static files will be collected from directory named 'static'
under your application::

    ./blog/static/

This example is with an application named `blog`.
URLs for static files in static directory will begin with
`/static/app_name/`. so in blog app case, if the directory has
css/main.css file, the file will be published like this::

    yoursite.com/static/blog/css/main.css

Getting URL for a static files
-------------------------------

You can get this URL by reversing form matching object

.. code-block:: python

    request.matching.reverse('blog:static', path=['css', 'main.css'])
