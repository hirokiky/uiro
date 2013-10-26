from functools import reduce


class ViewNotMatched(Exception):
    """ Called view was not apposite.
    """


def view_config(
        method='get',
):
    wrappers = [preserve_view(MethodPredicate(method))]

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
        def _wrapped(request, *args, **kwargs):
            if all([predicate(request) for predicate in predicates]):
                return view_callable(request, *args, **kwargs)
            else:
                raise ViewNotMatched
        return _wrapped
    return wrapper


class MethodPredicate(object):
    def __init__(self, method):
        self.method = method

    def __call__(self, request):
        return request.method.lower() == self.method.lower()
