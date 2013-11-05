"""
Testing for basic scaffold template

* Creating a tmp directory
* Unfolding a scaffold
* Running tests in unfolded package
"""


def setup_module(module):
    import os
    import tempfile

    tmpdir = tempfile.mkdtemp(dir='.')
    module.tmpdir = tmpdir
    os.chdir(tmpdir)


def test_scaffold():
    import subprocess

    subprocess.call(('gearbox', 'create', '-n', 'testing', '-o', '.'))
    result = subprocess.call(('py.test'))

    assert result == 0


def teardown_module(module):
    import os
    import shutil

    os.chdir('..')
    shutil.rmtree(module.tmpdir)
