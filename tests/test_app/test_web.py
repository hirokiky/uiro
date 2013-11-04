import pytest
from webtest import TestApp


@pytest.fixture
def target():
    from uiro import main
    config = {
        'uiro.root_matching': 'test_app.pkgs.web_app:matching',
        'uiro.installed_apps': 'test_app.pkgs.web_app',
        'sqlalchemy.url': 'sqlite:///memory'
    }
    return TestApp(main({}, '', **config))


def test_get(target):
    resp = target.get('/work')
    resp.mustcontain(b'No more work')
