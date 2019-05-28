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


from .DenseOpticalFlow import DenseOpticalFlow

class FarnebackOpticalFlow(DenseOpticalFlow):
    # no doc
    def create(self, numLevels=None, pyrScale=None, fastPyramids=None, winSize=None, numIters=None, polyN=None, polySigma=None, flags=None): # real signature unknown; restored from __doc__
        """
        create([, numLevels[, pyrScale[, fastPyramids[, winSize[, numIters[, polyN[, polySigma[, flags]]]]]]]]) -> retval
        .
        """
        pass

    def getFastPyramids(self): # real signature unknown; restored from __doc__
        """
        getFastPyramids() -> retval
        .
        """
        pass

    def getFlags(self): # real signature unknown; restored from __doc__
        """
        getFlags() -> retval
        .
        """
        pass

    def getNumIters(self): # real signature unknown; restored from __doc__
        """
        getNumIters() -> retval
        .
        """
        pass

    def getNumLevels(self): # real signature unknown; restored from __doc__
        """
        getNumLevels() -> retval
        .
        """
        pass

    def getPolyN(self): # real signature unknown; restored from __doc__
        """
        getPolyN() -> retval
        .
        """
        pass

    def getPolySigma(self): # real signature unknown; restored from __doc__
        """
        getPolySigma() -> retval
        .
        """
        pass

    def getPyrScale(self): # real signature unknown; restored from __doc__
        """
        getPyrScale() -> retval
        .
        """
        pass

    def getWinSize(self): # real signature unknown; restored from __doc__
        """
        getWinSize() -> retval
        .
        """
        pass

    def setFastPyramids(self, fastPyramids): # real signature unknown; restored from __doc__
        """
        setFastPyramids(fastPyramids) -> None
        .
        """
        pass

    def setFlags(self, flags): # real signature unknown; restored from __doc__
        """
        setFlags(flags) -> None
        .
        """
        pass

    def setNumIters(self, numIters): # real signature unknown; restored from __doc__
        """
        setNumIters(numIters) -> None
        .
        """
        pass

    def setNumLevels(self, numLevels): # real signature unknown; restored from __doc__
        """
        setNumLevels(numLevels) -> None
        .
        """
        pass

    def setPolyN(self, polyN): # real signature unknown; restored from __doc__
        """
        setPolyN(polyN) -> None
        .
        """
        pass

    def setPolySigma(self, polySigma): # real signature unknown; restored from __doc__
        """
        setPolySigma(polySigma) -> None
        .
        """
        pass

    def setPyrScale(self, pyrScale): # real signature unknown; restored from __doc__
        """
        setPyrScale(pyrScale) -> None
        .
        """
        pass

    def setWinSize(self, winSize): # real signature unknown; restored from __doc__
        """
        setWinSize(winSize) -> None
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


