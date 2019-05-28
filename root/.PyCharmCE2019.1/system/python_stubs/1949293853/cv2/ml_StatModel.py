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

class ml_StatModel(Algorithm):
    # no doc
    def calcError(self, data, test, resp=None): # real signature unknown; restored from __doc__
        """
        calcError(data, test[, resp]) -> retval, resp
        .   @brief Computes error on the training or test dataset
        .   
        .   @param data the training data
        .   @param test if true, the error is computed over the test subset of the data, otherwise it's
        .   computed over the training subset of the data. Please note that if you loaded a completely
        .   different dataset to evaluate already trained classifier, you will probably want not to set
        .   the test subset at all with TrainData::setTrainTestSplitRatio and specify test=false, so
        .   that the error is computed for the whole new set. Yes, this sounds a bit confusing.
        .   @param resp the optional output responses.
        .   
        .   The method uses StatModel::predict to compute the error. For regression models the error is
        .   computed as RMS, for classifiers - as a percent of missclassified samples (0%-100%).
        """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """
        empty() -> retval
        .
        """
        pass

    def getVarCount(self): # real signature unknown; restored from __doc__
        """
        getVarCount() -> retval
        .   @brief Returns the number of variables in training samples
        """
        pass

    def isClassifier(self): # real signature unknown; restored from __doc__
        """
        isClassifier() -> retval
        .   @brief Returns true if the model is classifier
        """
        pass

    def isTrained(self): # real signature unknown; restored from __doc__
        """
        isTrained() -> retval
        .   @brief Returns true if the model is trained
        """
        pass

    def predict(self, samples, results=None, flags=None): # real signature unknown; restored from __doc__
        """
        predict(samples[, results[, flags]]) -> retval, results
        .   @brief Predicts response(s) for the provided sample(s)
        .   
        .   @param samples The input samples, floating-point matrix
        .   @param results The optional output matrix of results.
        .   @param flags The optional flags, model-dependent. See cv::ml::StatModel::Flags.
        """
        pass

    def train(self, trainData, flags=None): # real signature unknown; restored from __doc__
        """
        train(trainData[, flags]) -> retval
        .   @brief Trains the statistical model
        .   
        .   @param trainData training data that can be loaded from file using TrainData::loadFromCSV or
        .   created with TrainData::create.
        .   @param flags optional flags, depending on the model. Some of the models can be updated with the
        .   new training samples, not completely overwritten (such as NormalBayesClassifier or ANN_MLP).
        
        
        
        train(samples, layout, responses) -> retval
        .   @brief Trains the statistical model
        .   
        .   @param samples training samples
        .   @param layout See ml::SampleTypes.
        .   @param responses vector of responses associated with the training samples.
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


