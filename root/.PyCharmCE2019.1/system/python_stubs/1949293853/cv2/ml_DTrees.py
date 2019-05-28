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


from .ml_StatModel import ml_StatModel

class ml_DTrees(ml_StatModel):
    # no doc
    def create(self): # real signature unknown; restored from __doc__
        """
        create() -> retval
        .   @brief Creates the empty model
        .   
        .   The static method creates empty decision tree with the specified parameters. It should be then
        .   trained using train method (see StatModel::train). Alternatively, you can load the model from
        .   file using Algorithm::load\<DTrees\>(filename).
        """
        pass

    def getCVFolds(self): # real signature unknown; restored from __doc__
        """
        getCVFolds() -> retval
        .   @see setCVFolds
        """
        pass

    def getMaxCategories(self): # real signature unknown; restored from __doc__
        """
        getMaxCategories() -> retval
        .   @see setMaxCategories
        """
        pass

    def getMaxDepth(self): # real signature unknown; restored from __doc__
        """
        getMaxDepth() -> retval
        .   @see setMaxDepth
        """
        pass

    def getMinSampleCount(self): # real signature unknown; restored from __doc__
        """
        getMinSampleCount() -> retval
        .   @see setMinSampleCount
        """
        pass

    def getPriors(self): # real signature unknown; restored from __doc__
        """
        getPriors() -> retval
        .   @see setPriors
        """
        pass

    def getRegressionAccuracy(self): # real signature unknown; restored from __doc__
        """
        getRegressionAccuracy() -> retval
        .   @see setRegressionAccuracy
        """
        pass

    def getTruncatePrunedTree(self): # real signature unknown; restored from __doc__
        """
        getTruncatePrunedTree() -> retval
        .   @see setTruncatePrunedTree
        """
        pass

    def getUse1SERule(self): # real signature unknown; restored from __doc__
        """
        getUse1SERule() -> retval
        .   @see setUse1SERule
        """
        pass

    def getUseSurrogates(self): # real signature unknown; restored from __doc__
        """
        getUseSurrogates() -> retval
        .   @see setUseSurrogates
        """
        pass

    def load(self, filepath, nodeName=None): # real signature unknown; restored from __doc__
        """
        load(filepath[, nodeName]) -> retval
        .   @brief Loads and creates a serialized DTrees from a file
        .   *
        .   * Use DTree::save to serialize and store an DTree to disk.
        .   * Load the DTree from this file again, by calling this function with the path to the file.
        .   * Optionally specify the node for the file containing the classifier
        .   *
        .   * @param filepath path to serialized DTree
        .   * @param nodeName name of node containing the classifier
        """
        pass

    def setCVFolds(self, val): # real signature unknown; restored from __doc__
        """
        setCVFolds(val) -> None
        .   @copybrief getCVFolds @see getCVFolds
        """
        pass

    def setMaxCategories(self, val): # real signature unknown; restored from __doc__
        """
        setMaxCategories(val) -> None
        .   @copybrief getMaxCategories @see getMaxCategories
        """
        pass

    def setMaxDepth(self, val): # real signature unknown; restored from __doc__
        """
        setMaxDepth(val) -> None
        .   @copybrief getMaxDepth @see getMaxDepth
        """
        pass

    def setMinSampleCount(self, val): # real signature unknown; restored from __doc__
        """
        setMinSampleCount(val) -> None
        .   @copybrief getMinSampleCount @see getMinSampleCount
        """
        pass

    def setPriors(self, val): # real signature unknown; restored from __doc__
        """
        setPriors(val) -> None
        .   @copybrief getPriors @see getPriors
        """
        pass

    def setRegressionAccuracy(self, val): # real signature unknown; restored from __doc__
        """
        setRegressionAccuracy(val) -> None
        .   @copybrief getRegressionAccuracy @see getRegressionAccuracy
        """
        pass

    def setTruncatePrunedTree(self, val): # real signature unknown; restored from __doc__
        """
        setTruncatePrunedTree(val) -> None
        .   @copybrief getTruncatePrunedTree @see getTruncatePrunedTree
        """
        pass

    def setUse1SERule(self, val): # real signature unknown; restored from __doc__
        """
        setUse1SERule(val) -> None
        .   @copybrief getUse1SERule @see getUse1SERule
        """
        pass

    def setUseSurrogates(self, val): # real signature unknown; restored from __doc__
        """
        setUseSurrogates(val) -> None
        .   @copybrief getUseSurrogates @see getUseSurrogates
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


