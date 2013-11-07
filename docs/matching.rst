URL Dispatching
===============

Registering Controller
----------------------

You can write dispatcher in `yourpacake/matching.py` like this:

.. code-block:: python

    from matcha import Matching as m, bundle
    from .views import DashbordController, PageController

    matching = bundle(
        m('/', DashbordController(), name='dashbord'),
        m('/page/{slug}', PageController(), name='page'),
    )

Then, client accessing:

:localhost/: DashboardController will be dispatched
:localhost/page/hello_word: PageController will be dispatched
:localhost/page/about_ritsu: also PageController will be dispatched

Uiro is using matcha_ dispatcher.
For more details about dispatching, watch matcha_ documentation.

Getting URL arguments from request
-----------------------------------

When accessing '/page/hello_word', you can that 'slug' value in your views.

.. code-block:: python

   >>> # In your views
   >>> request.matched_dict['slug']
   'hello_world'

Getting URL for each controllers
--------------------------------

.. code-block:: python

    request.matching.reverse('page', slug='hello_world')

request.matching is actually same value with matching object constructed by above example.
Uiro watches matching object and call controllers, then it assigns taken matching object to
request object.

Actually behavior
-----------------

To choice which Controller should be called, Uiro is using matcha_ dispatcher.
Uiro will automatically construct application from a matching object of matcha_
specified by configuration .ini file.

In .ini file, the `uiro.root_matching` is key to specify core matching object
for your application. the value should be splittable by colon (':'), then, the left value
is path to module to store your root matching object, and the right value is it's name.

If you write a setting like this::

    uiro.root_matching = path.to.yourmodule:matchingobject

follow matching object will be used as root matching to construct your application.

.. code-block:: python

    # In path.to.yourmodule module.
    matchingobject = Matching('/', SomeWSGIApp())

Constructed application will call SomeWSGIApp when the PATH_INFO is '/'.

.. _matcha: https://pypi.python.org/pypi/matcha
