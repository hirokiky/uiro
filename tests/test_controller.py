import pytest


@pytest.fixture
def target_class():
    from uiro.controller import BaseController
    return BaseController


def test_init(target_class):
    class Controller(target_class):
        def ritsu_view(self):
            return 'ritsu'

        def get_mio(self):
            return 'mio'

        def _mugi_view(self):
            return 'mugi'

    actual = Controller()

    assert len(actual.views) == 1
    assert actual.views[0]() == 'ritsu'


def test_call(target_class):
    def mio_decorator(func):
        def wraped(*args, **kwargs):
            return func(*args, **kwargs) + ' x mio'
        func._wrapped = wraped
        return func

    class Controller(target_class):
        @mio_decorator
        def ritsu_view(self, request):
            return request + ' ritsu'

    target = Controller()

    assert target('tainaka') == 'tainaka ritsu x mio'


def test_call_not_found(target_class):
    from uiro.view import ViewNotMatched

    def not_matched_wrapped(self, request):
        raise ViewNotMatched

    def view_callable(request):
        return request

    target = target_class()
    view_callable._wrapped = not_matched_wrapped
    target.views = [view_callable]

    actual = target('request')

    assert actual.status_code == 404
