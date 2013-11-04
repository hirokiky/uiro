import pytest


@pytest.fixture
def target_class():
    from uiro.controller import BaseController
    return BaseController


def test_init(target_class):
    class Controller(target_class):
        def yui_view(self):
            return 'yui'
        yui_view._order = 1

        def ritsu_view(self):
            return 'ritsu'
        ritsu_view._order = 0

        def get_mio(self):
            return 'mio'

        def _mugi_view(self):
            return 'mugi'

    actual = Controller()

    assert len(actual.views) == 2
    assert actual.views[0].__name__ == 'ritsu_view'
    assert actual.views[1].__name__ == 'yui_view'


def test_call(target_class):
    def mio_decorator(func):
        def wraped(*args, **kwargs):
            return func(*args, **kwargs) + ' x mio'
        func._wrapped = wraped
        func._order = 0
        return func

    class Controller(target_class):
        @mio_decorator
        def ritsu_view(self, request, context):
            return request + ' ritsu'

    target = Controller()

    assert target('tainaka') == 'tainaka ritsu x mio'


def test_call_not_found(target_class):
    from uiro.view import ViewNotMatched

    def not_matched_wrapped(self, request, context):
        raise ViewNotMatched

    def view_callable(request):
        return request

    target = target_class()
    view_callable._wrapped = not_matched_wrapped
    view_callable._order = 0
    target.views = [view_callable]

    actual = target('request')

    assert actual.status_code == 404
