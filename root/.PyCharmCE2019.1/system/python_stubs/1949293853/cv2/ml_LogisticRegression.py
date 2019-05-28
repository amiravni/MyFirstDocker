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

class ml_LogisticRegression(ml_StatModel):
    # no doc
    def create(self): # real signature unknown; restored from __doc__
        """
        create() -> retval
        .   @brief Creates empty model.
        .   
        .   Creates Logistic Regression model with parameters given.
        """
        pass

    def getIterations(self): # real signature unknown; restored from __doc__
        """
        getIterations() -> retval
        .   @see setIterations
        """
        pass

    def getLearningRate(self): # real signature unknown; restored from __doc__
        """
        getLearningRate() -> retval
        .   @see setLearningRate
        """
        pass

    def getMiniBatchSize(self): # real signature unknown; restored from __doc__
        """
        getMiniBatchSize() -> retval
        .   @see setMiniBatchSize
        """
        pass

    def getRegularization(self): # real signature unknown; restored from __doc__
        """
        getRegularization() -> retval
        .   @see setRegularization
        """
        pass

    def getTermCriteria(self): # real signature unknown; restored from __doc__
        """
        getTermCriteria() -> retval
        .   @see setTermCriteria
        """
        pass

    def getTrainMethod(self): # real signature unknown; restored from __doc__
        """
        getTrainMethod() -> retval
        .   @see setTrainMethod
        """
        pass

    def get_learnt_thetas(self): # real signature unknown; restored from __doc__
        """
        get_learnt_thetas() -> retval
        .   @brief This function returns the trained parameters arranged across rows.
        .   
        .   For a two class classifcation problem, it returns a row matrix. It returns learnt parameters of
        .   the Logistic Regression as a matrix of type CV_32F.
        """
        pass

    def load(self, filepath, nodeName=None): # real signature unknown; restored from __doc__
        """
        load(filepath[, nodeName]) -> retval
        .   @brief Loads and creates a serialized LogisticRegression from a file
        .   *
        .   * Use LogisticRegression::save to serialize and store an LogisticRegression to disk.
        .   * Load the LogisticRegression from this file again, by calling this function with the path to the file.
        .   * Optionally specify the node for the file containing the classifier
        .   *
        .   * @param filepath path to serialized LogisticRegression
        .   * @param nodeName name of node containing the classifier
        """
        pass

    def predict(self, samples, results=None, flags=None): # real signature unknown; restored from __doc__
        """
        predict(samples[, results[, flags]]) -> retval, results
        .   @brief Predicts responses for input samples and returns a float type.
        .   
        .   @param samples The input data for the prediction algorithm. Matrix [m x n], where each row
        .   contains variables (features) of one object being classified. Should have data type CV_32F.
        .   @param results Predicted labels as a column matrix of type CV_32S.
        .   @param flags Not used.
        """
        pass

    def setIterations(self, val): # real signature unknown; restored from __doc__
        """
        setIterations(val) -> None
        .   @copybrief getIterations @see getIterations
        """
        pass

    def setLearningRate(self, val): # real signature unknown; restored from __doc__
        """
        setLearningRate(val) -> None
        .   @copybrief getLearningRate @see getLearningRate
        """
        pass

    def setMiniBatchSize(self, val): # real signature unknown; restored from __doc__
        """
        setMiniBatchSize(val) -> None
        .   @copybrief getMiniBatchSize @see getMiniBatchSize
        """
        pass

    def setRegularization(self, val): # real signature unknown; restored from __doc__
        """
        setRegularization(val) -> None
        .   @copybrief getRegularization @see getRegularization
        """
        pass

    def setTermCriteria(self, val): # real signature unknown; restored from __doc__
        """
        setTermCriteria(val) -> None
        .   @copybrief getTermCriteria @see getTermCriteria
        """
        pass

    def setTrainMethod(self, val): # real signature unknown; restored from __doc__
        """
        setTrainMethod(val) -> None
        .   @copybrief getTrainMethod @see getTrainMethod
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


