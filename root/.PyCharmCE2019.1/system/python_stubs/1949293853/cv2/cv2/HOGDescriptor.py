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


from .object import object

class HOGDescriptor(object):
    # no doc
    def checkDetectorSize(self): # real signature unknown; restored from __doc__
        """
        checkDetectorSize() -> retval
        .   @brief Checks if detector size equal to descriptor size.
        """
        pass

    def compute(self, img, winStride=None, padding=None, locations=None): # real signature unknown; restored from __doc__
        """
        compute(img[, winStride[, padding[, locations]]]) -> descriptors
        .   @brief Computes HOG descriptors of given image.
        .   @param img Matrix of the type CV_8U containing an image where HOG features will be calculated.
        .   @param descriptors Matrix of the type CV_32F
        .   @param winStride Window stride. It must be a multiple of block stride.
        .   @param padding Padding
        .   @param locations Vector of Point
        """
        pass

    def computeGradient(self, img, grad, angleOfs, paddingTL=None, paddingBR=None): # real signature unknown; restored from __doc__
        """
        computeGradient(img, grad, angleOfs[, paddingTL[, paddingBR]]) -> grad, angleOfs
        .   @brief  Computes gradients and quantized gradient orientations.
        .   @param img Matrix contains the image to be computed
        .   @param grad Matrix of type CV_32FC2 contains computed gradients
        .   @param angleOfs Matrix of type CV_8UC2 contains quantized gradient orientations
        .   @param paddingTL Padding from top-left
        .   @param paddingBR Padding from bottom-right
        """
        pass

    def detect(self, img, hitThreshold=None, winStride=None, padding=None, searchLocations=None): # real signature unknown; restored from __doc__
        """
        detect(img[, hitThreshold[, winStride[, padding[, searchLocations]]]]) -> foundLocations, weights
        .   @brief Performs object detection without a multi-scale window.
        .   @param img Matrix of the type CV_8U or CV_8UC3 containing an image where objects are detected.
        .   @param foundLocations Vector of point where each point contains left-top corner point of detected object boundaries.
        .   @param weights Vector that will contain confidence values for each detected object.
        .   @param hitThreshold Threshold for the distance between features and SVM classifying plane.
        .   Usually it is 0 and should be specified in the detector coefficients (as the last free coefficient).
        .   But if the free coefficient is omitted (which is allowed), you can specify it manually here.
        .   @param winStride Window stride. It must be a multiple of block stride.
        .   @param padding Padding
        .   @param searchLocations Vector of Point includes set of requested locations to be evaluated.
        """
        pass

    def detectMultiScale(self, img, hitThreshold=None, winStride=None, padding=None, scale=None, finalThreshold=None, useMeanshiftGrouping=None): # real signature unknown; restored from __doc__
        """
        detectMultiScale(img[, hitThreshold[, winStride[, padding[, scale[, finalThreshold[, useMeanshiftGrouping]]]]]]) -> foundLocations, foundWeights
        .   @brief Detects objects of different sizes in the input image. The detected objects are returned as a list
        .   of rectangles.
        .   @param img Matrix of the type CV_8U or CV_8UC3 containing an image where objects are detected.
        .   @param foundLocations Vector of rectangles where each rectangle contains the detected object.
        .   @param foundWeights Vector that will contain confidence values for each detected object.
        .   @param hitThreshold Threshold for the distance between features and SVM classifying plane.
        .   Usually it is 0 and should be specified in the detector coefficients (as the last free coefficient).
        .   But if the free coefficient is omitted (which is allowed), you can specify it manually here.
        .   @param winStride Window stride. It must be a multiple of block stride.
        .   @param padding Padding
        .   @param scale Coefficient of the detection window increase.
        .   @param finalThreshold Final threshold
        .   @param useMeanshiftGrouping indicates grouping algorithm
        """
        pass

    def getDaimlerPeopleDetector(self): # real signature unknown; restored from __doc__
        """
        getDaimlerPeopleDetector() -> retval
        .   @brief Returns coefficients of the classifier trained for people detection (for 48x96 windows).
        """
        pass

    def getDefaultPeopleDetector(self): # real signature unknown; restored from __doc__
        """
        getDefaultPeopleDetector() -> retval
        .   @brief Returns coefficients of the classifier trained for people detection (for 64x128 windows).
        """
        pass

    def getDescriptorSize(self): # real signature unknown; restored from __doc__
        """
        getDescriptorSize() -> retval
        .   @brief Returns the number of coefficients required for the classification.
        """
        pass

    def getWinSigma(self): # real signature unknown; restored from __doc__
        """
        getWinSigma() -> retval
        .   @brief Returns winSigma value
        """
        pass

    def load(self, filename, objname=None): # real signature unknown; restored from __doc__
        """
        load(filename[, objname]) -> retval
        .   @brief loads HOGDescriptor parameters and coefficients for the linear SVM classifier from a file.
        .   @param filename Path of the file to read.
        .   @param objname The optional name of the node to read (if empty, the first top-level node will be used).
        """
        pass

    def save(self, filename, objname=None): # real signature unknown; restored from __doc__
        """
        save(filename[, objname]) -> None
        .   @brief saves HOGDescriptor parameters and coefficients for the linear SVM classifier to a file
        .   @param filename File name
        .   @param objname Object name
        """
        pass

    def setSVMDetector(self, svmdetector): # real signature unknown; restored from __doc__
        """
        setSVMDetector(svmdetector) -> None
        .   @brief Sets coefficients for the linear SVM classifier.
        .   @param svmdetector coefficients for the linear SVM classifier.
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

    blockSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """blockSize"""

    blockStride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """blockStride"""

    cellSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """cellSize"""

    derivAperture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """derivAperture"""

    gammaCorrection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """gammaCorrection"""

    histogramNormType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """histogramNormType"""

    L2HysThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """L2HysThreshold"""

    nbins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """nbins"""

    nlevels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """nlevels"""

    signedGradient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """signedGradient"""

    svmDetector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """svmDetector"""

    winSigma = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """winSigma"""

    winSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """winSize"""



