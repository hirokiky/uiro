import pytest


@pytest.fixture
def target_class():
    from uiro.controller import BaseController
    return BaseController


def create_dummy_view(wrapped):
    def view(request):
        return 'kadoom'
    view._wrapped = wrapped
    return view


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
    target = target_class()
    target.views = [create_dummy_view(lambda x: x)]

    assert target('request') == 'request'


def test_call_not_found(target_class):
    from uiro.view import ViewNotMatched
    target = target_class()

    def not_matched_wrapped(request):
        raise ViewNotMatched
    target.views = [create_dummy_view(not_matched_wrapped)]

    actual = target('request')

    assert actual.status_code == 404
