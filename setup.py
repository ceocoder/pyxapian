"""\
Simple PyPi project for the Xapian bindings so that they
can be installed via easy_install or pip.
"""

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

import errno
import subprocess as sp

def get_config():
    cmd = "xapian-config --cxxflags --libs"
    pipe = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    (stdout, stderr) = pipe.communicate()
    if pipe.wait() != 0:
        raise RuntimeError("Failed to run xapian-config. Is it on your path?")
    config = {
        "sources": ["xapian_wrap.cc"],
        "include_dirs": [],
        "library_dirs": [],
        "libraries": [],
        "extra_compile_args": [],
        "extra_link_args": []
    }
    prefixes = {
        "-I": ("include_dirs", 2),
        "-L": ("library_dirs", 2),
        "-l": ("libraries", 2)
    }
    for flag in stdout.split():
        for prefix in prefixes:
            if not flag.startswith(prefix):
                continue
            name, trim = prefixes[prefix]
            config[name].append(flag[trim:])
    return config

setup(
    name = "pyxapian",
    version = "1.0.21",
    license = "GPL v2.0",
    author = "Xapian Group",
    description = "Python bindings to Xapian",
    long_description = __doc__,
    url = "http://github.com/davisp/pyxapian",
    download_url = "http://github.com/davisp/pyxapian.git",
    
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: C',
        'Programming Language :: Python',
    ],
    
    py_modules = ["xapian"],

    ext_modules = [
        Extension("_xapian", **get_config())
    ],

    test_suite = 'nose.collector'
)

