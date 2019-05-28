# encoding: utf-8
# module lxml.etree
# from /usr/lib/python3/dist-packages/lxml/etree.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class ErrorDomains(object):
    """ Libxml2 error domains """
    def _getName(self, *args, **kwargs): # real signature unknown
        """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BUFFER = 29
    C14N = 21
    CATALOG = 20
    CHECK = 24
    DATATYPE = 15
    DTD = 4
    FTP = 9
    HTML = 5
    HTTP = 10
    I18N = 27
    IO = 8
    MEMORY = 6
    MODULE = 26
    NAMESPACE = 3
    NONE = 0
    OUTPUT = 7
    PARSER = 1
    REGEXP = 14
    RELAXNGP = 18
    RELAXNGV = 19
    SCHEMASP = 16
    SCHEMASV = 17
    SCHEMATRONV = 28
    TREE = 2
    URI = 30
    VALID = 23
    WRITER = 25
    XINCLUDE = 11
    XPATH = 12
    XPOINTER = 13
    XSLT = 22
    _names = {
        0: 'NONE',
        1: 'PARSER',
        2: 'TREE',
        3: 'NAMESPACE',
        4: 'DTD',
        5: 'HTML',
        6: 'MEMORY',
        7: 'OUTPUT',
        8: 'IO',
        9: 'FTP',
        10: 'HTTP',
        11: 'XINCLUDE',
        12: 'XPATH',
        13: 'XPOINTER',
        14: 'REGEXP',
        15: 'DATATYPE',
        16: 'SCHEMASP',
        17: 'SCHEMASV',
        18: 'RELAXNGP',
        19: 'RELAXNGV',
        20: 'CATALOG',
        21: 'C14N',
        22: 'XSLT',
        23: 'VALID',
        24: 'CHECK',
        25: 'WRITER',
        26: 'MODULE',
        27: 'I18N',
        28: 'SCHEMATRONV',
        29: 'BUFFER',
        30: 'URI',
    }
    __dict__ = None # (!) real value is "mappingproxy({'HTML': 5, 'MODULE': 26, 'SCHEMATRONV': 28, 'URI': 30, 'NONE': 0, 'NAMESPACE': 3, 'REGEXP': 14, 'SCHEMASP': 16, 'I18N': 27, 'XSLT': 22, '_getName': <built-in method get of dict object at 0x7f5df5b27a08>, '__dict__': <attribute '__dict__' of 'ErrorDomains' objects>, '__module__': 'lxml.etree', 'HTTP': 10, 'XINCLUDE': 11, 'SCHEMASV': 17, '_names': {0: 'NONE', 1: 'PARSER', 2: 'TREE', 3: 'NAMESPACE', 4: 'DTD', 5: 'HTML', 6: 'MEMORY', 7: 'OUTPUT', 8: 'IO', 9: 'FTP', 10: 'HTTP', 11: 'XINCLUDE', 12: 'XPATH', 13: 'XPOINTER', 14: 'REGEXP', 15: 'DATATYPE', 16: 'SCHEMASP', 17: 'SCHEMASV', 18: 'RELAXNGP', 19: 'RELAXNGV', 20: 'CATALOG', 21: 'C14N', 22: 'XSLT', 23: 'VALID', 24: 'CHECK', 25: 'WRITER', 26: 'MODULE', 27: 'I18N', 28: 'SCHEMATRONV', 29: 'BUFFER', 30: 'URI'}, 'RELAXNGV': 19, 'CHECK': 24, 'IO': 8, 'MEMORY': 6, 'WRITER': 25, 'FTP': 9, 'OUTPUT': 7, 'DTD': 4, 'XPOINTER': 13, 'PARSER': 1, 'RELAXNGP': 18, 'XPATH': 12, 'BUFFER': 29, '__doc__': 'Libxml2 error domains', 'TREE': 2, 'CATALOG': 20, 'VALID': 23, 'DATATYPE': 15, '__weakref__': <attribute '__weakref__' of 'ErrorDomains' objects>, 'C14N': 21})"


