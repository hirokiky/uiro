Writing your views
==================

“Views” are methods to encapsulate the logic responsible for...:

* Processing a user’s request and context determined data by request.
* Returning the response, such as response object, dictionary or string.

Commonly views will look like this:

.. code-block:: python

    from uiro.controller import BaseController
    from uiro.view import view_config

    class MyController(BaseController):
        @view_config(method='get')
        def get_view(self, request, context):
            return 'Hello world!'

This MyController class is WSGI application returns response containing text 'Hello world!' in it's body.

* Controller is a WSGI application.
* view_config is decorator to construct methods as view.
* All of views should be named with '_view' suffix.

Views are logic about interfaces. Storing business logic in views is not recommended.

Testing views without decorators
--------------------------------

An Unit test should test target logic without any other things.
View methods must be applied view_config decorator, so It seems that it is difficult to test views
without any decorators.

Don't worry, Uiro provide a feature allowing you to write tests without decorators.
You can test views like this:

.. code-block:: python

    >>> target = MyController().get_view
    >>> assert target('dummy_request', 'dummy_context') == 'Hello world!'

Responsibility of controllers
-----------------------------

Constructing a WSGI application from views. It checks which view should be called and dispatching.
You don't need to write any logic for controllers. All of them have been determined by Uiro framework.
It is only used as a container for views like above example.

You can change logic in controller, specifying some values to interface provided by it's own.
The best example of this is `resource`, it is object to some resources on app determined by a request.
For more detail, see `Apply resources for views`_.

.. note::

    The number of APIs provided by Controllers should be as little as possible.
    Uiro should not force users to remember a lot of APIs. it will be labor for users and generally
    it will be difficult to use. and what is worth, changing APIs may be hard work so Uiro will become
    inflexible increasingly.

Apply resources for views
-------------------------

For many cases, necessary data for one view can be determined by only a request.
And It should be separate from views, to increase testability and readability:

* Separating logic to collect data form views.
* Allowing to dispatch views corresponds to collected data in context.

It will be applied request object and you can write logic to collect data in it.
It can be specified `resource` attribute in your Controller. A controller apply request
to class in `resource` attribute and pass it to each view methods.

You can use this behavior like this:

.. code-block:: python

    from .models import Page

    class PageResource(object):
        def __init__(self, request):
            self.request = request

        @property
        def page(self):
            return Page.query.filter_by(id=request.matched_dict['id']).one()

    class Controller(BaseController):
        resource = PageResource

        @view_config(method='get'):
        def get_view(request, context):
            return {'page': context.page}

Hereby, you separated collection logic and view (user interface).
When you test each views, you can pass dummy request and context easily. you can focus writing tests
for about interfaces.

.. note::

    It's better to store resource classes in a separated module to correspond to each models.
    Above example, The PageResource class in `page.py` seems better. Then of cause, you will store another
    logic for the Page model in `page.py` too.
