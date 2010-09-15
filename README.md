Python Xapian Bindings
======================

The original bindings required being installed via Autotools and what
not which is fairly non-standard for Python. Although, completely
extracting the binding generation from the Autotools does not appear
to be as easy as I would have originally guessed.

This project exists merely to allow for installing the xapian bindings
via easy_install or pip so that they can be imported into virtual
environments.

For the moment I have only made the project compatible with the 1.0.23
branch. Going forward I will add support for the 1.2.x branch as well
as any version that people ask for (within reason).

To install via pip:

    $ pip install -e git://github.com/davisp/pyxapian.git@v1.0.23#egg=xapian

For the URL scheme you can replace git with git+http or git+ssh to use
the alternative transports.
