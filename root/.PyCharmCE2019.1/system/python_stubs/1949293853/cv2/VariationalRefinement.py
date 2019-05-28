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

class VariationalRefinement(DenseOpticalFlow):
    # no doc
    def calcUV(self, I0, I1, flow_u, flow_v): # real signature unknown; restored from __doc__
        """
        calcUV(I0, I1, flow_u, flow_v) -> flow_u, flow_v
        .   @brief @ref calc function overload to handle separate horizontal (u) and vertical (v) flow components
        .   (to avoid extra splits/merges)
        """
        pass

    def create(self): # real signature unknown; restored from __doc__
        """
        create() -> retval
        .   @brief Creates an instance of VariationalRefinement
        """
        pass

    def getAlpha(self): # real signature unknown; restored from __doc__
        """
        getAlpha() -> retval
        .   @brief Weight of the smoothness term
        .   @see setAlpha
        """
        pass

    def getDelta(self): # real signature unknown; restored from __doc__
        """
        getDelta() -> retval
        .   @brief Weight of the color constancy term
        .   @see setDelta
        """
        pass

    def getFixedPointIterations(self): # real signature unknown; restored from __doc__
        """
        getFixedPointIterations() -> retval
        .   @brief Number of outer (fixed-point) iterations in the minimization procedure.
        .   @see setFixedPointIterations
        """
        pass

    def getGamma(self): # real signature unknown; restored from __doc__
        """
        getGamma() -> retval
        .   @brief Weight of the gradient constancy term
        .   @see setGamma
        """
        pass

    def getOmega(self): # real signature unknown; restored from __doc__
        """
        getOmega() -> retval
        .   @brief Relaxation factor in SOR
        .   @see setOmega
        """
        pass

    def getSorIterations(self): # real signature unknown; restored from __doc__
        """
        getSorIterations() -> retval
        .   @brief Number of inner successive over-relaxation (SOR) iterations
        .   in the minimization procedure to solve the respective linear system.
        .   @see setSorIterations
        """
        pass

    def setAlpha(self, val): # real signature unknown; restored from __doc__
        """
        setAlpha(val) -> None
        .   @copybrief getAlpha @see getAlpha
        """
        pass

    def setDelta(self, val): # real signature unknown; restored from __doc__
        """
        setDelta(val) -> None
        .   @copybrief getDelta @see getDelta
        """
        pass

    def setFixedPointIterations(self, val): # real signature unknown; restored from __doc__
        """
        setFixedPointIterations(val) -> None
        .   @copybrief getFixedPointIterations @see getFixedPointIterations
        """
        pass

    def setGamma(self, val): # real signature unknown; restored from __doc__
        """
        setGamma(val) -> None
        .   @copybrief getGamma @see getGamma
        """
        pass

    def setOmega(self, val): # real signature unknown; restored from __doc__
        """
        setOmega(val) -> None
        .   @copybrief getOmega @see getOmega
        """
        pass

    def setSorIterations(self, val): # real signature unknown; restored from __doc__
        """
        setSorIterations(val) -> None
        .   @copybrief getSorIterations @see getSorIterations
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


