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

class ORB(Feature2D):
    # no doc
    def create(self, nfeatures=None, scaleFactor=None, nlevels=None, edgeThreshold=None, firstLevel=None, WTA_K=None, scoreType=None, patchSize=None, fastThreshold=None): # real signature unknown; restored from __doc__
        """
        create([, nfeatures[, scaleFactor[, nlevels[, edgeThreshold[, firstLevel[, WTA_K[, scoreType[, patchSize[, fastThreshold]]]]]]]]]) -> retval
        .   @brief The ORB constructor
        .   
        .   @param nfeatures The maximum number of features to retain.
        .   @param scaleFactor Pyramid decimation ratio, greater than 1. scaleFactor==2 means the classical
        .   pyramid, where each next level has 4x less pixels than the previous, but such a big scale factor
        .   will degrade feature matching scores dramatically. On the other hand, too close to 1 scale factor
        .   will mean that to cover certain scale range you will need more pyramid levels and so the speed
        .   will suffer.
        .   @param nlevels The number of pyramid levels. The smallest level will have linear size equal to
        .   input_image_linear_size/pow(scaleFactor, nlevels - firstLevel).
        .   @param edgeThreshold This is size of the border where the features are not detected. It should
        .   roughly match the patchSize parameter.
        .   @param firstLevel The level of pyramid to put source image to. Previous layers are filled
        .   with upscaled source image.
        .   @param WTA_K The number of points that produce each element of the oriented BRIEF descriptor. The
        .   default value 2 means the BRIEF where we take a random point pair and compare their brightnesses,
        .   so we get 0/1 response. Other possible values are 3 and 4. For example, 3 means that we take 3
        .   random points (of course, those point coordinates are random, but they are generated from the
        .   pre-defined seed, so each element of BRIEF descriptor is computed deterministically from the pixel
        .   rectangle), find point of maximum brightness and output index of the winner (0, 1 or 2). Such
        .   output will occupy 2 bits, and therefore it will need a special variant of Hamming distance,
        .   denoted as NORM_HAMMING2 (2 bits per bin). When WTA_K=4, we take 4 random points to compute each
        .   bin (that will also occupy 2 bits with possible values 0, 1, 2 or 3).
        .   @param scoreType The default HARRIS_SCORE means that Harris algorithm is used to rank features
        .   (the score is written to KeyPoint::score and is used to retain best nfeatures features);
        .   FAST_SCORE is alternative value of the parameter that produces slightly less stable keypoints,
        .   but it is a little faster to compute.
        .   @param patchSize size of the patch used by the oriented BRIEF descriptor. Of course, on smaller
        .   pyramid layers the perceived image area covered by a feature will be larger.
        .   @param fastThreshold
        """
        pass

    def getDefaultName(self): # real signature unknown; restored from __doc__
        """
        getDefaultName() -> retval
        .
        """
        pass

    def getEdgeThreshold(self): # real signature unknown; restored from __doc__
        """
        getEdgeThreshold() -> retval
        .
        """
        pass

    def getFastThreshold(self): # real signature unknown; restored from __doc__
        """
        getFastThreshold() -> retval
        .
        """
        pass

    def getFirstLevel(self): # real signature unknown; restored from __doc__
        """
        getFirstLevel() -> retval
        .
        """
        pass

    def getMaxFeatures(self): # real signature unknown; restored from __doc__
        """
        getMaxFeatures() -> retval
        .
        """
        pass

    def getNLevels(self): # real signature unknown; restored from __doc__
        """
        getNLevels() -> retval
        .
        """
        pass

    def getPatchSize(self): # real signature unknown; restored from __doc__
        """
        getPatchSize() -> retval
        .
        """
        pass

    def getScaleFactor(self): # real signature unknown; restored from __doc__
        """
        getScaleFactor() -> retval
        .
        """
        pass

    def getScoreType(self): # real signature unknown; restored from __doc__
        """
        getScoreType() -> retval
        .
        """
        pass

    def getWTA_K(self): # real signature unknown; restored from __doc__
        """
        getWTA_K() -> retval
        .
        """
        pass

    def setEdgeThreshold(self, edgeThreshold): # real signature unknown; restored from __doc__
        """
        setEdgeThreshold(edgeThreshold) -> None
        .
        """
        pass

    def setFastThreshold(self, fastThreshold): # real signature unknown; restored from __doc__
        """
        setFastThreshold(fastThreshold) -> None
        .
        """
        pass

    def setFirstLevel(self, firstLevel): # real signature unknown; restored from __doc__
        """
        setFirstLevel(firstLevel) -> None
        .
        """
        pass

    def setMaxFeatures(self, maxFeatures): # real signature unknown; restored from __doc__
        """
        setMaxFeatures(maxFeatures) -> None
        .
        """
        pass

    def setNLevels(self, nlevels): # real signature unknown; restored from __doc__
        """
        setNLevels(nlevels) -> None
        .
        """
        pass

    def setPatchSize(self, patchSize): # real signature unknown; restored from __doc__
        """
        setPatchSize(patchSize) -> None
        .
        """
        pass

    def setScaleFactor(self, scaleFactor): # real signature unknown; restored from __doc__
        """
        setScaleFactor(scaleFactor) -> None
        .
        """
        pass

    def setScoreType(self, scoreType): # real signature unknown; restored from __doc__
        """
        setScoreType(scoreType) -> None
        .
        """
        pass

    def setWTA_K(self, wta_k): # real signature unknown; restored from __doc__
        """
        setWTA_K(wta_k) -> None
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


