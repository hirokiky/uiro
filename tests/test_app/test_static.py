import pytest
from webtest import TestApp


@pytest.fixture
def target():
    from matcha import make_wsgi_app
    from uiro.static import generate_static_matching
    from .pkgs import static_app

    matching = generate_static_matching(static_app)
    return TestApp(make_wsgi_app(matching))


def test_static(target):
    resp = target.get('/static/static_app/test.txt')
    resp.mustcontain('No more work')
