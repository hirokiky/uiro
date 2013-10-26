from functools import reduce

from uiro.template import get_app_template


class ViewNotMatched(Exception):
    """ Called view was not apposite.
    """


def get_base_wrappers(method='get', template_name=''):
    wrappers = [preserve_view(MethodPredicate(method))]

    if template_name:
        wrappers.append(render_template(template_name))

    return wrappers


def view_config(
        method='get',
        template_name='',
        base_wrappers_getter=get_base_wrappers
):
    wrappers = base_wrappers_getter(method, template_name)

    def wrapper(view_callable):
        def _wrapped(*args, **kwargs):
            return reduce(
                lambda a, b: b(a),
                reversed(wrappers + [view_callable])
            )(*args, **kwargs)
        view_callable._wrapped = _wrapped
        return view_callable
    return wrapper


def preserve_view(*predicates):
    def wrapper(view_callable):
        def _wrapped(self, request, *args, **kwargs):
            if all([predicate(request) for predicate in predicates]):
                return view_callable(self, request, *args, **kwargs)
            else:
                raise ViewNotMatched
        return _wrapped
    return wrapper


class MethodPredicate(object):
    def __init__(self, method):
        self.method = method

    def __call__(self, request):
        return request.method.lower() == self.method.lower()


def render_template(template_name, template_getter=get_app_template):
    def wrapper(func):
        template = template_getter(template_name)

        def _wraped(self, request, *args, **kwargs):
            res = func(self, request, *args, **kwargs)
            if isinstance(res, dict):
                return template.render(**res)
            else:
                return res
        return _wraped
    return wrapper
