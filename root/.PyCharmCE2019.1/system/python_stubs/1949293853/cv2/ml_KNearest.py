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

class ml_KNearest(ml_StatModel):
    # no doc
    def create(self): # real signature unknown; restored from __doc__
        """
        create() -> retval
        .   @brief Creates the empty model
        .   
        .   The static method creates empty %KNearest classifier. It should be then trained using StatModel::train method.
        """
        pass

    def findNearest(self, samples, k, results=None, neighborResponses=None, dist=None): # real signature unknown; restored from __doc__
        """
        findNearest(samples, k[, results[, neighborResponses[, dist]]]) -> retval, results, neighborResponses, dist
        .   @brief Finds the neighbors and predicts responses for input vectors.
        .   
        .   @param samples Input samples stored by rows. It is a single-precision floating-point matrix of
        .   `<number_of_samples> * k` size.
        .   @param k Number of used nearest neighbors. Should be greater than 1.
        .   @param results Vector with results of prediction (regression or classification) for each input
        .   sample. It is a single-precision floating-point vector with `<number_of_samples>` elements.
        .   @param neighborResponses Optional output values for corresponding neighbors. It is a single-
        .   precision floating-point matrix of `<number_of_samples> * k` size.
        .   @param dist Optional output distances from the input vectors to the corresponding neighbors. It
        .   is a single-precision floating-point matrix of `<number_of_samples> * k` size.
        .   
        .   For each input vector (a row of the matrix samples), the method finds the k nearest neighbors.
        .   In case of regression, the predicted result is a mean value of the particular vector's neighbor
        .   responses. In case of classification, the class is determined by voting.
        .   
        .   For each input vector, the neighbors are sorted by their distances to the vector.
        .   
        .   In case of C++ interface you can use output pointers to empty matrices and the function will
        .   allocate memory itself.
        .   
        .   If only a single input vector is passed, all output matrices are optional and the predicted
        .   value is returned by the method.
        .   
        .   The function is parallelized with the TBB library.
        """
        pass

    def getAlgorithmType(self): # real signature unknown; restored from __doc__
        """
        getAlgorithmType() -> retval
        .   @see setAlgorithmType
        """
        pass

    def getDefaultK(self): # real signature unknown; restored from __doc__
        """
        getDefaultK() -> retval
        .   @see setDefaultK
        """
        pass

    def getEmax(self): # real signature unknown; restored from __doc__
        """
        getEmax() -> retval
        .   @see setEmax
        """
        pass

    def getIsClassifier(self): # real signature unknown; restored from __doc__
        """
        getIsClassifier() -> retval
        .   @see setIsClassifier
        """
        pass

    def setAlgorithmType(self, val): # real signature unknown; restored from __doc__
        """
        setAlgorithmType(val) -> None
        .   @copybrief getAlgorithmType @see getAlgorithmType
        """
        pass

    def setDefaultK(self, val): # real signature unknown; restored from __doc__
        """
        setDefaultK(val) -> None
        .   @copybrief getDefaultK @see getDefaultK
        """
        pass

    def setEmax(self, val): # real signature unknown; restored from __doc__
        """
        setEmax(val) -> None
        .   @copybrief getEmax @see getEmax
        """
        pass

    def setIsClassifier(self, val): # real signature unknown; restored from __doc__
        """
        setIsClassifier(val) -> None
        .   @copybrief getIsClassifier @see getIsClassifier
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


