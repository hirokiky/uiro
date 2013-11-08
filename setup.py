import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = ''
    CHANGES = ''

version = "0.2"

setup(name='uiro',
      version=version,
      description="le Web framework.",
      long_description=README + '\n' + CHANGES,
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: Implementation :: CPython",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI",
          "License :: OSI Approved :: MIT License",
      ],
      keywords='web wsgi',
      author='Hiroki KIYOHARA',
      author_email='hirokiky@gmail.com',
      url='https://github.com/hirokiky/uiro/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'webob==1.2.3',
          'gearbox==0.0.2',
          'mako==0.9.0',
          'matcha==0.3',
          'SQLAlchemy==0.8.3',
          'zope.sqlalchemy==0.7.3',
      ],
      tests_require=[
          'pytest',
          'WebTest',
      ],
      entry_points={
          'gearbox.commands': [
              'initdb=uiro.commands.initdb:InitDBCommand',
              'shell=uiro.commands.shell:ShellCommand',
              'create=uiro.commands.create:CreateCommand',
          ]
      }
      )
