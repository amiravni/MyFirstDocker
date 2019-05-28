# encoding: utf-8
# module apt_pkg
# from /usr/lib/python3/dist-packages/apt_pkg.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
"""
Classes and functions wrapping the apt-pkg library.

The apt_pkg module provides several classes and functions for accessing
the functionality provided by the apt-pkg library. Typical uses might
include reading APT index files and configuration files and installing
or removing packages.
"""
# no imports

from .ValueError import ValueError

class CacheMismatchError(ValueError):
    """
    Raised when passing an object from a different cache to
    :class:`apt_pkg.DepCache` methods
    
    .. versionadded:: 1.6.1
    
    .. versionadded:: 1.4.0~beta1ubuntu0.16.04.2
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



