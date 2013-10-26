import pytest


@pytest.fixture
def target():
    from uiro import template
    return template


def setup_function(function):
    target()._lookups = None


class DummyApp(object):
    def __init__(self, file_path, name):
        self.__file__ = file_path
        self.__name__ = name


class DummyLookup(object):
    def __init__(self, directories='', output_encoding='', encoding_errors=''):
        self.directories = directories
        self.output_encoding = output_encoding
        self.encoding_errors = encoding_errors

    def get_template(self, template_name):
        return template_name


def test_setup_lookups(target):
    target.setup_lookup([DummyApp('./dev/blog/__init__.py', 'blog')],
                        lookup_class=DummyLookup)

    assert len(target._lookups) == 1
    assert target._lookups['blog'].directories == ['./dev/blog/templates']
    assert target._lookups['blog'].output_encoding == 'utf-8'
    assert target._lookups['blog'].encoding_errors == 'replace'


def test_get_lookups(target):
    target._lookups = 'lookups'
    assert target.get_lookups() == 'lookups'


def test_get_app_template(target):
    target._lookups = {'blog': DummyLookup()}
    target.get_app_template('blog:home.mako') == 'home.mako'
