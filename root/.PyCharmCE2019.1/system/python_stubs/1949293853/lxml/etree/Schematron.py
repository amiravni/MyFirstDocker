# encoding: utf-8
# module lxml.etree
# from /usr/lib/python3/dist-packages/lxml/etree.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from ._Validator import _Validator

class Schematron(_Validator):
    """
    Schematron(self, etree=None, file=None)
        A Schematron validator.
    
        Pass a root Element or an ElementTree to turn it into a validator.
        Alternatively, pass a filename as keyword argument 'file' to parse from
        the file system.
    
        Schematron is a less well known, but very powerful schema language.  The main
        idea is to use the capabilities of XPath to put restrictions on the structure
        and the content of XML documents.  Here is a simple example::
    
          >>> schematron = Schematron(XML('''
          ... <schema xmlns="http://www.ascc.net/xml/schematron" >
          ...   <pattern name="id is the only permited attribute name">
          ...     <rule context="*">
          ...       <report test="@*[not(name()='id')]">Attribute
          ...         <name path="@*[not(name()='id')]"/> is forbidden<name/>
          ...       </report>
          ...     </rule>
          ...   </pattern>
          ... </schema>
          ... '''))
    
          >>> xml = XML('''
          ... <AAA name="aaa">
          ...   <BBB id="bbb"/>
          ...   <CCC color="ccc"/>
          ... </AAA>
          ... ''')
    
          >>> schematron.validate(xml)
          0
    
          >>> xml = XML('''
          ... <AAA id="aaa">
          ...   <BBB id="bbb"/>
          ...   <CCC/>
          ... </AAA>
          ... ''')
    
          >>> schematron.validate(xml)
          1
    
        Schematron was added to libxml2 in version 2.6.21.  Before version 2.6.32,
        however, Schematron lacked support for error reporting other than to stderr.
        This version is therefore required to retrieve validation warnings and
        errors in lxml.
    """
    def __call__(self, etree): # real signature unknown; restored from __doc__
        """
        __call__(self, etree)
        
                Validate doc using Schematron.
        
                Returns true if document is valid, false if not.
        """
        pass

    def __init__(self, etree=None, file=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f5df5b210c0>'


