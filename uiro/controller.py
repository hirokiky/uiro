from webob.dec import wsgify
from webob.response import Response

from uiro.request import Request
from uiro.view import ViewNotMatched


class BaseController(object):
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

    class DashboardController(BaseController):
        @view_config(method='get')
        def get_view(self, request):
            return "Hello guys"

        @view_config(method='post')
        def post_view(self, request):
            return "Posted something"

    Check the behavior of view_config for more detail.
    """
    def __init__(self):
        self.views = []
        for attr_names in dir(self):
            if not attr_names.startswith('_') and attr_names.endswith('_view'):
                self.views.append(getattr(self, attr_names))

    @wsgify(RequestClass=Request)
    def __call__(self, request):
        for view in self.views:
            try:
                return view._wrapped(self, request)
            except ViewNotMatched:
                continue
        else:
            return Response(status_code=404)
