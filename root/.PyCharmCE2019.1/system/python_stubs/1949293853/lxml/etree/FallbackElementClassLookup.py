# encoding: utf-8
# module lxml.etree
# from /usr/lib/python3/dist-packages/lxml/etree.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .ElementClassLookup import ElementClassLookup

class FallbackElementClassLookup(ElementClassLookup):
    """
    FallbackElementClassLookup(self, fallback=None)
    
        Superclass of Element class lookups with additional fallback.
    """
    def set_fallback(self, lookup): # real signature unknown; restored from __doc__
        """
        set_fallback(self, lookup)
        
                Sets the fallback scheme for this lookup method.
        """
        pass

    def __init__(self, fallback=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    fallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f5df5c0c6c0>'


