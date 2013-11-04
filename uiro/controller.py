from webob.dec import wsgify
from webob.response import Response

from uiro.request import Request
from uiro.view import ViewNotMatched


class NotFound(Exception):
    """ Error for notifying the resource was not found.
    """


class ControllerMetaClass(type):
    def __new__(cls, name, bases, attrs):
        super_new = super(ControllerMetaClass, cls).__new__
        new_class = super_new(cls, name, bases, attrs)

        new_class.views = [value for name, value in attrs.items()
                           if not name.startswith('_') and name.endswith('_view')]
        new_class.views.sort(key=lambda x: x._order)
        return new_class


class BaseController(metaclass=ControllerMetaClass):
    """ Base WSGI application class to handle Views.

    Controllers try to call methods containing '_view' suffix on it's name.
    But actually it will call _wrapped attribute of each Views:

    * Original View methods can be called without any decorators.
      This behavior is provided for ensuring depending-less tests.
    * When wrapped View raised ViewNotMatched, it will try next one.
    * All of views are not matched, it will return 404 response.

    You can inherit this class and register views. Then, decorate views
    with uiro.view.view_config to apply configation to each views,
    such as witch views will be call or witch template to use.

    .. code-block:: python

       class DashboardController(BaseController):
           @view_config(method='get')
           def get_view(self, request):
               return "Hello guys"

           @view_config(method='post')
           def post_view(self, request):
               return "Posted something"

    Check the behavior of view_config for more detail.
    """
    views = []
    resource = (lambda s, x: x)

    @wsgify(RequestClass=Request)
    def __call__(self, request):
        try:
            context = self.resource(request)
        except NotFound:
            raise Response(status_code=404)

        for view in self.views:
            try:
                return view._wrapped(self, request, context)
            except ViewNotMatched:
                continue
        else:
            return Response(status_code=404)
