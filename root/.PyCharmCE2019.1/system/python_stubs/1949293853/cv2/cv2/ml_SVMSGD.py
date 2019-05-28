# encoding: utf-8
# module cv2.cv2
# from /usr/local/lib/python3.5/dist-packages/cv2/cv2.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" Python wrapper for OpenCV. """

# imports
import cv2.cv2 as  # /usr/local/lib/python3.5/dist-packages/cv2/cv2.cpython-35m-x86_64-linux-gnu.so
import cv2.instr as instr # <module 'cv2.instr'>
import cv2.videoio_registry as videoio_registry # <module 'cv2.videoio_registry'>
import cv2.dnn as dnn # <module 'cv2.dnn'>
import cv2.fisheye as fisheye # <module 'cv2.fisheye'>
import cv2.samples as samples # <module 'cv2.samples'>
import cv2.ocl as ocl # <module 'cv2.ocl'>
import cv2.utils as utils # <module 'cv2.utils'>
import cv2.cuda as cuda # <module 'cv2.cuda'>
import cv2.detail as detail # <module 'cv2.detail'>
import cv2.flann as flann # <module 'cv2.flann'>
import cv2.ml as ml # <module 'cv2.ml'>
import cv2.Error as Error # <module 'cv2.Error'>
import cv2.ogl as ogl # <module 'cv2.ogl'>
import cv2.ipp as ipp # <module 'cv2.ipp'>
import cv2 as __cv2


class ml_SVMSGD(__cv2.ml_StatModel):
    # no doc
    def create(self): # real signature unknown; restored from __doc__
        """
        create() -> retval
        .   @brief Creates empty model.
        .   * Use StatModel::train to train the model. Since %SVMSGD has several parameters, you may want to
        .   * find the best parameters for your problem or use setOptimalParameters() to set some default parameters.
        """
        pass

    def getInitialStepSize(self): # real signature unknown; restored from __doc__
        """
        getInitialStepSize() -> retval
        .   @see setInitialStepSize
        """
        pass

    def getMarginRegularization(self): # real signature unknown; restored from __doc__
        """
        getMarginRegularization() -> retval
        .   @see setMarginRegularization
        """
        pass

    def getMarginType(self): # real signature unknown; restored from __doc__
        """
        getMarginType() -> retval
        .   @see setMarginType
        """
        pass

    def getShift(self): # real signature unknown; restored from __doc__
        """
        getShift() -> retval
        .   * @return the shift of the trained model (decision function f(x) = weights * x + shift).
        """
        pass

    def getStepDecreasingPower(self): # real signature unknown; restored from __doc__
        """
        getStepDecreasingPower() -> retval
        .   @see setStepDecreasingPower
        """
        pass

    def getSvmsgdType(self): # real signature unknown; restored from __doc__
        """
        getSvmsgdType() -> retval
        .   @see setSvmsgdType
        """
        pass

    def getTermCriteria(self): # real signature unknown; restored from __doc__
        """
        getTermCriteria() -> retval
        .   @see setTermCriteria
        """
        pass

    def getWeights(self): # real signature unknown; restored from __doc__
        """
        getWeights() -> retval
        .   * @return the weights of the trained model (decision function f(x) = weights * x + shift).
        """
        pass

    def load(self, filepath, nodeName=None): # real signature unknown; restored from __doc__
        """
        load(filepath[, nodeName]) -> retval
        .   @brief Loads and creates a serialized SVMSGD from a file
        .   *
        .   * Use SVMSGD::save to serialize and store an SVMSGD to disk.
        .   * Load the SVMSGD from this file again, by calling this function with the path to the file.
        .   * Optionally specify the node for the file containing the classifier
        .   *
        .   * @param filepath path to serialized SVMSGD
        .   * @param nodeName name of node containing the classifier
        """
        pass

    def setInitialStepSize(self, InitialStepSize): # real signature unknown; restored from __doc__
        """
        setInitialStepSize(InitialStepSize) -> None
        .   @copybrief getInitialStepSize @see getInitialStepSize
        """
        pass

    def setMarginRegularization(self, marginRegularization): # real signature unknown; restored from __doc__
        """
        setMarginRegularization(marginRegularization) -> None
        .   @copybrief getMarginRegularization @see getMarginRegularization
        """
        pass

    def setMarginType(self, marginType): # real signature unknown; restored from __doc__
        """
        setMarginType(marginType) -> None
        .   @copybrief getMarginType @see getMarginType
        """
        pass

    def setOptimalParameters(self, svmsgdType=None, marginType=None): # real signature unknown; restored from __doc__
        """
        setOptimalParameters([, svmsgdType[, marginType]]) -> None
        .   @brief Function sets optimal parameters values for chosen SVM SGD model.
        .   * @param svmsgdType is the type of SVMSGD classifier.
        .   * @param marginType is the type of margin constraint.
        """
        pass

    def setStepDecreasingPower(self, stepDecreasingPower): # real signature unknown; restored from __doc__
        """
        setStepDecreasingPower(stepDecreasingPower) -> None
        .   @copybrief getStepDecreasingPower @see getStepDecreasingPower
        """
        pass

    def setSvmsgdType(self, svmsgdType): # real signature unknown; restored from __doc__
        """
        setSvmsgdType(svmsgdType) -> None
        .   @copybrief getSvmsgdType @see getSvmsgdType
        """
        pass

    def setTermCriteria(self, val): # real signature unknown; restored from __doc__
        """
        setTermCriteria(val) -> None
        .   @copybrief getTermCriteria @see getTermCriteria
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


