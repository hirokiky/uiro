import pytest


class DummyApp(object):
    def __init__(self, file, name):
        self.__file__ = file
        self.__name__ = name


class DummyDirectoryServeApp(object):
    def __init__(self, directory, **kwargs):
        self.directory = directory


@pytest.fixture
def target():
    from uiro import static
    return static


def test_generate_static_matching(target):
    dummy_app = DummyApp('./dev/blog/__init__.py', 'blog')
    actual = target.generate_static_matching(dummy_app, DummyDirectoryServeApp)

    actual_app, matched_dict = actual['/static/blog/image/logo.png']
    assert isinstance(actual_app, DummyDirectoryServeApp)
    assert actual_app.directory == './dev/blog/static'
    assert matched_dict == {'path': ['image', 'logo.png']}
    assert actual.reverse(
        'blog:static',
        path=['image', 'logo.png']
    ) == '/static/blog/image/logo.png'


def test_generate_static_matching_directiory_not_found(target):
    def os_error_app(directory, **kwargs):
        raise OSError

    dummy_app = DummyApp('./dev/blog/kadoom', 'blog')
    actual = target.generate_static_matching(dummy_app, os_error_app)

    assert actual is None
