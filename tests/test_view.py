import pytest


def create_dummy_request(method):
    from collections import namedtuple
    return namedtuple('Request', ['method'])(method)


class TestViewConfig(object):
    def target(self):
        from uiro.view import view_config
        return view_config

    def makeone(self, method, view_callable):
        return self.target()(method=method)(view_callable)

    def test_wrapping(self):
        from uiro.view import ViewNotMatched

        def view_callable(request):
            return request
        target = self.makeone('get', view_callable)

        assert target('request') == 'request'
        with pytest.raises(ViewNotMatched):
            target._wrapped(create_dummy_request('post'))


class TestPreserveView(object):
    @pytest.fixture
    def target(self):
        from uiro.view import preserve_view
        return preserve_view

    def test_matched(self, target):
        actual = target(lambda r: True, lambda r: True)(lambda r: r)

        assert actual('request') == 'request'

    def test_not_matched(self, target):
        from uiro.view import ViewNotMatched
        actual = target(lambda r: False, lambda r: True)(lambda r: r)

        with pytest.raises(ViewNotMatched):
            actual('request')


class TestMethodPredicate(object):
    @pytest.fixture
    def target(self):
        from uiro.view import MethodPredicate
        return MethodPredicate

    @pytest.mark.parametrize('request', [create_dummy_request('get'),
                                         create_dummy_request('GET')])
    @pytest.mark.parametrize('method', ['get', 'GET'])
    def test_matched(self, target, request, method):
        assert target(method)(request)
