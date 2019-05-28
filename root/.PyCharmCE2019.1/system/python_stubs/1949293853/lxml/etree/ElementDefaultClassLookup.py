# encoding: utf-8
# module lxml.etree
# from /usr/lib/python3/dist-packages/lxml/etree.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .ElementClassLookup import ElementClassLookup

class ElementDefaultClassLookup(ElementClassLookup):
    """
    ElementDefaultClassLookup(self, element=None, comment=None, pi=None, entity=None)
        Element class lookup scheme that always returns the default Element
        class.
    
        The keyword arguments ``element``, ``comment``, ``pi`` and ``entity``
        accept the respective Element classes.
    """
    def __init__(self, element=None, comment=None, pi=None, entity=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    comment_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    element_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    entity_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pi_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



