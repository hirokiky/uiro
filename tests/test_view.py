import pytest


def create_dummy_request(method):
    from collections import namedtuple
    return namedtuple('Request', ['method'])(method)


class TestViewConfig(object):
    def target(self):
        from uiro.view import view_config
        return view_config

    def makeone(self, view_callable):
        return self.target()(
            base_wrappers_getter=lambda *args: [],
        )(view_callable)

    def test_wrapping(self):
        def view_callable(request):
            return request
        target = self.makeone(view_callable)

        assert target('request') == 'request'


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


class DummyTemplate(object):
    def __init__(self, temlate_name):
        self.template_name = temlate_name

    def render(self, **res):
        res['template_name'] = self.template_name
        return res


class TestRendertemplate(object):
    @pytest.fixture
    def target(self):
        from uiro.view import render_template
        return render_template

    def test_returned_dict(self, target):
        wrapped = target(
            'blog:home.mako', DummyTemplate
        )(lambda r: {'request': r})

        actual = wrapped('request')

        assert actual['request'] == 'request'
        assert actual['template_name'] == 'blog:home.mako'
