====================
ORB Content Platform
====================

For documentation visit: http://mpowering.readthedocs.org

For information on mPowering visit: http://mpoweringhealth.org

Development
===========

To simplify development including creating migrations and running the
devserver, the bundled `manage.py` file can be used with the settings and
configuration in the `config` module.::

    ./manage.py makemigrations orb
    ./manage.py migrate
    ./manage.py runserver

Configuration
-------------

All custom settings should be placed in `config/local_settings.py`. This file
is not source controlled. It should be written in the same format as any other
Django settings file. The primary settings file will try a naked import from
this file at the end of the main settings file, overriding any other settings
specified and adding any new ones.

The settings included are designed to be as simple and sensible for baseline
development as possible. It is *highly* recommended that the local settings
file be used to specify database settings.

Testing
=======

The tests for the ORB platform can be run using the current Python path (or
currently activated virtual environment) using the command::

    make test-django

The project is also configured to use `tox
<http://tox.readthedocs.org/en/latest/>`_ for isolated testing and test
environment matrices. This ensures that the full test environment can be
created *outside* and apart from the development environment and that tests can
be run against the application with different dependency versions, including
Django and even different Python versions. To use tox first install it::

    pip install tox

And then run the command::

    tox

This will run all specified tests against all specified environments in
sequence. Alternatively, you can specify one or more environments using the
`-e` argument::

    tox -e deployed

This particular environment will run tests using the frozen requirements for
the deployed environment.

Using the `-r` flag will recreate the test environment from scratch.::

    tox -r
    tox -e deployed -r

For running a large matrix of tests, consider using the `detox
<https://pypi.python.org/pypi/detox>`_ tool which parallelizes tests based on
the number of available cores.::

    pip install detox
    detox

Environments
------------

The `flake8` environment is limited to running `flake8` for linting and basic
static analysis.

The `deployed` environment uses the frozen requirements file to ensure that
every dependency is pinned to the same requirements used to deploy the
application. (Note that this still requires settings updates to ensure that the
same database backend is used.)

The remaining environments are designed to work around different versions of
Django, to allow testing against future Django versions. The requirements here
should be loose enough to allow newer versions of the dependency to be used.
