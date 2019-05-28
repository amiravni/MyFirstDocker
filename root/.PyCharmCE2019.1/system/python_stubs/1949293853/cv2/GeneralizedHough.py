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


from .Algorithm import Algorithm

class GeneralizedHough(Algorithm):
    # no doc
    def detect(self, image, positions=None, votes=None): # real signature unknown; restored from __doc__
        """
        detect(image[, positions[, votes]]) -> positions, votes
        .   
        
        
        
        detect(edges, dx, dy[, positions[, votes]]) -> positions, votes
        .
        """
        pass

    def getCannyHighThresh(self): # real signature unknown; restored from __doc__
        """
        getCannyHighThresh() -> retval
        .
        """
        pass

    def getCannyLowThresh(self): # real signature unknown; restored from __doc__
        """
        getCannyLowThresh() -> retval
        .
        """
        pass

    def getDp(self): # real signature unknown; restored from __doc__
        """
        getDp() -> retval
        .
        """
        pass

    def getMaxBufferSize(self): # real signature unknown; restored from __doc__
        """
        getMaxBufferSize() -> retval
        .
        """
        pass

    def getMinDist(self): # real signature unknown; restored from __doc__
        """
        getMinDist() -> retval
        .
        """
        pass

    def setCannyHighThresh(self, cannyHighThresh): # real signature unknown; restored from __doc__
        """
        setCannyHighThresh(cannyHighThresh) -> None
        .
        """
        pass

    def setCannyLowThresh(self, cannyLowThresh): # real signature unknown; restored from __doc__
        """
        setCannyLowThresh(cannyLowThresh) -> None
        .
        """
        pass

    def setDp(self, dp): # real signature unknown; restored from __doc__
        """
        setDp(dp) -> None
        .
        """
        pass

    def setMaxBufferSize(self, maxBufferSize): # real signature unknown; restored from __doc__
        """
        setMaxBufferSize(maxBufferSize) -> None
        .
        """
        pass

    def setMinDist(self, minDist): # real signature unknown; restored from __doc__
        """
        setMinDist(minDist) -> None
        .
        """
        pass

    def setTemplate(self, templ, templCenter=None): # real signature unknown; restored from __doc__
        """
        setTemplate(templ[, templCenter]) -> None
        .   
        
        
        
        setTemplate(edges, dx, dy[, templCenter]) -> None
        .
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


