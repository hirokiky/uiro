import itertools
from functools import reduce

from uiro.template import get_app_template


class ViewNotMatched(Exception):
    """ Called view was not apposite.
    This exception is to notify Controllers that called view was not apposite
    to the applied rquest.
    """


def get_base_wrappers(method='get', template_name='', predicates=(), wrappers=()):
    """ basic View Wrappers used by view_config.
    """
    wrappers += (preserve_view(MethodPredicate(method), *predicates),)

    if template_name:
        wrappers += (render_template(template_name),)

    return wrappers


_counter = itertools.count()


def view_config(
        method='get',
        template_name='',
        predicates=(),
        wrappers=(),
        base_wrappers_getter=get_base_wrappers,
):
    """ Creating Views applied some configurations
    and store it to _wrapped attribute on each Views.

    * _wrapped expects to be called by Controller
      (subclasses of uiro.controller.BaseController)
    * The original view will not be affected by this decorator.
    """
    wrappers = base_wrappers_getter(method, template_name, predicates, wrappers)

    def wrapper(view_callable):
        def _wrapped(*args, **kwargs):
            return reduce(
                lambda a, b: b(a),
                reversed(wrappers + (view_callable,))
            )(*args, **kwargs)
        view_callable._wrapped = _wrapped
        view_callable._order = next(_counter)
        return view_callable
    return wrapper


def preserve_view(*predicates):
    """ Raising ViewNotMatched when applied request was not apposite.

    preserve_view calls all Predicates and when return values of them was
    all True it will call a wrapped view.
    It raises ViewNotMatched if this is not the case.

    Predicates:
    This decorator takes Predicates one or more, Predicate is callable
    to return True or False in response to inputted request.
    If the request was apposite it should return True.
    """
    def wrapper(view_callable):
        def _wrapped(self, request, context, *args, **kwargs):
            if all([predicate(request, context) for predicate in predicates]):
                return view_callable(self, request, context, *args, **kwargs)
            else:
                raise ViewNotMatched
        return _wrapped
    return wrapper


class MethodPredicate(object):
    """ Predicate class to checking Method of request object.

    MethodPredicate is preserve views when the request method was not same with
    applied in instantiate.
    """
    def __init__(self, method):
        self.method = method

    def __call__(self, request, context):
        return request.method.lower() == self.method.lower()


def render_template(template_name, template_getter=get_app_template):
    """ Decorator to specify which template to use for Wrapped Views.

    It will return string rendered by specified template and
    returned dictionary from wrapped views as a context for template.
    The returned value was not dictionary, it does nothing,
    just returns the result.
    """
    def wrapper(func):
        template = template_getter(template_name)

        def _wraped(self, request, context, *args, **kwargs):
            res = func(self, request, context, *args, **kwargs)
            if isinstance(res, dict):
                return template.render(**res)
            else:
                return res
        return _wraped
    return wrapper
