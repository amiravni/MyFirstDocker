# encoding: utf-8
# module cv2 calls itself cv2.cv2
# from /opt/ros/kinetic/lib/python2.7/dist-packages/cv2.so
# by generator 1.147
""" Python wrapper for OpenCV. """

# imports
import cv2.cv2 as  # /usr/local/lib/python3.5/dist-packages/cv2/cv2.cpython-35m-x86_64-linux-gnu.so
import cv2.detail as detail # <module 'cv2.detail'>
import cv2.ml as ml # <module 'cv2.ml'>
import os as os # /usr/lib/python3.5/os.py
import cv2.data as data # /usr/local/lib/python3.5/dist-packages/cv2/data/__init__.py
import cv2.cuda as cuda # <module 'cv2.cuda'>
import cv2.ogl as ogl # <module 'cv2.ogl'>
import cv2.samples as samples # <module 'cv2.samples'>
import cv2.Error as Error # <module 'cv2.Error'>
import cv2.ipp as ipp # <module 'cv2.ipp'>
import cv2.flann as flann # <module 'cv2.flann'>
import cv2.instr as instr # <module 'cv2.instr'>
import importlib as importlib # /usr/lib/python3.5/importlib/__init__.py
import cv2.ocl as ocl # <module 'cv2.ocl'>
import cv2.videoio_registry as videoio_registry # <module 'cv2.videoio_registry'>
import cv2.utils as utils # <module 'cv2.utils'>
import cv2.cv2 as cv2 # /usr/local/lib/python3.5/dist-packages/cv2/cv2.cpython-35m-x86_64-linux-gnu.so
import cv2.dnn as dnn # <module 'cv2.dnn'>
import cv2.fisheye as fisheye # <module 'cv2.fisheye'>
from cv2.cv2 import (createButton, createTrackbar, dnn_registerLayer, 
    dnn_unregisterLayer, redirectError, setMouseCallback)


from .object import object

class FileNode(object):
    # no doc
    def at(self, i): # real signature unknown; restored from __doc__
        """
        at(i) -> retval
        .   @overload
        .   @param i Index of an element in the sequence node.
        """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """
        empty() -> retval
        .
        """
        pass

    def getNode(self, nodename): # real signature unknown; restored from __doc__
        """
        getNode(nodename) -> retval
        .   @overload
        .   @param nodename Name of an element in the mapping node.
        """
        pass

    def isInt(self): # real signature unknown; restored from __doc__
        """
        isInt() -> retval
        .
        """
        pass

    def isMap(self): # real signature unknown; restored from __doc__
        """
        isMap() -> retval
        .
        """
        pass

    def isNamed(self): # real signature unknown; restored from __doc__
        """
        isNamed() -> retval
        .
        """
        pass

    def isNone(self): # real signature unknown; restored from __doc__
        """
        isNone() -> retval
        .
        """
        pass

    def isReal(self): # real signature unknown; restored from __doc__
        """
        isReal() -> retval
        .
        """
        pass

    def isSeq(self): # real signature unknown; restored from __doc__
        """
        isSeq() -> retval
        .
        """
        pass

    def isString(self): # real signature unknown; restored from __doc__
        """
        isString() -> retval
        .
        """
        pass

    def keys(self): # real signature unknown; restored from __doc__
        """
        keys() -> retval
        .   @brief Returns keys of a mapping node.
        .   @returns Keys of a mapping node.
        """
        pass

    def mat(self): # real signature unknown; restored from __doc__
        """
        mat() -> retval
        .
        """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """
        name() -> retval
        .
        """
        pass

    def rawSize(self): # real signature unknown; restored from __doc__
        """
        rawSize() -> retval
        .
        """
        pass

    def real(self): # real signature unknown; restored from __doc__
        """
        real() -> retval
        .   Internal method used when reading FileStorage.
        .   Sets the type (int, real or string) and value of the previously created node.
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """
        size() -> retval
        .
        """
        pass

    def string(self): # real signature unknown; restored from __doc__
        """
        string() -> retval
        .
        """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """
        type() -> retval
        .   @brief Returns type of the node.
        .   @returns Type of the node. See FileNode::Type
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


