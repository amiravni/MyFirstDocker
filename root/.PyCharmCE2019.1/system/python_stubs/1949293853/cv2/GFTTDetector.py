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


from .Feature2D import Feature2D

class GFTTDetector(Feature2D):
    # no doc
    def create(self, maxCorners=None, qualityLevel=None, minDistance=None, blockSize=None, useHarrisDetector=None, k=None): # real signature unknown; restored from __doc__
        """
        create([, maxCorners[, qualityLevel[, minDistance[, blockSize[, useHarrisDetector[, k]]]]]]) -> retval
        .   
        
        
        
        create(maxCorners, qualityLevel, minDistance, blockSize, gradiantSize[, useHarrisDetector[, k]]) -> retval
        .
        """
        pass

    def getBlockSize(self): # real signature unknown; restored from __doc__
        """
        getBlockSize() -> retval
        .
        """
        pass

    def getDefaultName(self): # real signature unknown; restored from __doc__
        """
        getDefaultName() -> retval
        .
        """
        pass

    def getHarrisDetector(self): # real signature unknown; restored from __doc__
        """
        getHarrisDetector() -> retval
        .
        """
        pass

    def getK(self): # real signature unknown; restored from __doc__
        """
        getK() -> retval
        .
        """
        pass

    def getMaxFeatures(self): # real signature unknown; restored from __doc__
        """
        getMaxFeatures() -> retval
        .
        """
        pass

    def getMinDistance(self): # real signature unknown; restored from __doc__
        """
        getMinDistance() -> retval
        .
        """
        pass

    def getQualityLevel(self): # real signature unknown; restored from __doc__
        """
        getQualityLevel() -> retval
        .
        """
        pass

    def setBlockSize(self, blockSize): # real signature unknown; restored from __doc__
        """
        setBlockSize(blockSize) -> None
        .
        """
        pass

    def setHarrisDetector(self, val): # real signature unknown; restored from __doc__
        """
        setHarrisDetector(val) -> None
        .
        """
        pass

    def setK(self, k): # real signature unknown; restored from __doc__
        """
        setK(k) -> None
        .
        """
        pass

    def setMaxFeatures(self, maxFeatures): # real signature unknown; restored from __doc__
        """
        setMaxFeatures(maxFeatures) -> None
        .
        """
        pass

    def setMinDistance(self, minDistance): # real signature unknown; restored from __doc__
        """
        setMinDistance(minDistance) -> None
        .
        """
        pass

    def setQualityLevel(self, qlevel): # real signature unknown; restored from __doc__
        """
        setQualityLevel(qlevel) -> None
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


