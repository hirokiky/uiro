from webob.dec import wsgify
from webob.response import Response

from uiro.view import ViewNotMatched


class BaseController(object):
    def __init__(self):
        self.views = []
        for attr_names in dir(self):
            if not attr_names.startswith('_') and attr_names.endswith('_view'):
                self.views.append(getattr(self, attr_names))

    @wsgify
    def __call__(self, request):
        for view in self.views:
            try:
                return view._wrapped(request)
            except ViewNotMatched:
                continue
        else:
            return Response(status_code=404)
