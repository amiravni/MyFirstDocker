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


class BackgroundSubtractorKNN(__cv2.BackgroundSubtractor):
    # no doc
    def getDetectShadows(self): # real signature unknown; restored from __doc__
        """
        getDetectShadows() -> retval
        .   @brief Returns the shadow detection flag
        .   
        .   If true, the algorithm detects shadows and marks them. See createBackgroundSubtractorKNN for
        .   details.
        """
        pass

    def getDist2Threshold(self): # real signature unknown; restored from __doc__
        """
        getDist2Threshold() -> retval
        .   @brief Returns the threshold on the squared distance between the pixel and the sample
        .   
        .   The threshold on the squared distance between the pixel and the sample to decide whether a pixel is
        .   close to a data sample.
        """
        pass

    def getHistory(self): # real signature unknown; restored from __doc__
        """
        getHistory() -> retval
        .   @brief Returns the number of last frames that affect the background model
        """
        pass

    def getkNNSamples(self): # real signature unknown; restored from __doc__
        """
        getkNNSamples() -> retval
        .   @brief Returns the number of neighbours, the k in the kNN.
        .   
        .   K is the number of samples that need to be within dist2Threshold in order to decide that that
        .   pixel is matching the kNN background model.
        """
        pass

    def getNSamples(self): # real signature unknown; restored from __doc__
        """
        getNSamples() -> retval
        .   @brief Returns the number of data samples in the background model
        """
        pass

    def getShadowThreshold(self): # real signature unknown; restored from __doc__
        """
        getShadowThreshold() -> retval
        .   @brief Returns the shadow threshold
        .   
        .   A shadow is detected if pixel is a darker version of the background. The shadow threshold (Tau in
        .   the paper) is a threshold defining how much darker the shadow can be. Tau= 0.5 means that if a pixel
        .   is more than twice darker then it is not shadow. See Prati, Mikic, Trivedi and Cucchiara,
        .   *Detecting Moving Shadows...*, IEEE PAMI,2003.
        """
        pass

    def getShadowValue(self): # real signature unknown; restored from __doc__
        """
        getShadowValue() -> retval
        .   @brief Returns the shadow value
        .   
        .   Shadow value is the value used to mark shadows in the foreground mask. Default value is 127. Value 0
        .   in the mask always means background, 255 means foreground.
        """
        pass

    def setDetectShadows(self, detectShadows): # real signature unknown; restored from __doc__
        """
        setDetectShadows(detectShadows) -> None
        .   @brief Enables or disables shadow detection
        """
        pass

    def setDist2Threshold(self, _dist2Threshold): # real signature unknown; restored from __doc__
        """
        setDist2Threshold(_dist2Threshold) -> None
        .   @brief Sets the threshold on the squared distance
        """
        pass

    def setHistory(self, history): # real signature unknown; restored from __doc__
        """
        setHistory(history) -> None
        .   @brief Sets the number of last frames that affect the background model
        """
        pass

    def setkNNSamples(self, _nkNN): # real signature unknown; restored from __doc__
        """
        setkNNSamples(_nkNN) -> None
        .   @brief Sets the k in the kNN. How many nearest neighbours need to match.
        """
        pass

    def setNSamples(self, _nN): # real signature unknown; restored from __doc__
        """
        setNSamples(_nN) -> None
        .   @brief Sets the number of data samples in the background model.
        .   
        .   The model needs to be reinitalized to reserve memory.
        """
        pass

    def setShadowThreshold(self, threshold): # real signature unknown; restored from __doc__
        """
        setShadowThreshold(threshold) -> None
        .   @brief Sets the shadow threshold
        """
        pass

    def setShadowValue(self, value): # real signature unknown; restored from __doc__
        """
        setShadowValue(value) -> None
        .   @brief Sets the shadow value
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


