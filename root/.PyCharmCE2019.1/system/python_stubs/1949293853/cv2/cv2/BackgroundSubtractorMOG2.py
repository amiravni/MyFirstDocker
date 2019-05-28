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


class BackgroundSubtractorMOG2(__cv2.BackgroundSubtractor):
    # no doc
    def apply(self, image, fgmask=None, learningRate=None): # real signature unknown; restored from __doc__
        """
        apply(image[, fgmask[, learningRate]]) -> fgmask
        .   @brief Computes a foreground mask.
        .   
        .   @param image Next video frame. Floating point frame will be used without scaling and should be in range \f$[0,255]\f$.
        .   @param fgmask The output foreground mask as an 8-bit binary image.
        .   @param learningRate The value between 0 and 1 that indicates how fast the background model is
        .   learnt. Negative parameter value makes the algorithm to use some automatically chosen learning
        .   rate. 0 means that the background model is not updated at all, 1 means that the background model
        .   is completely reinitialized from the last frame.
        """
        pass

    def getBackgroundRatio(self): # real signature unknown; restored from __doc__
        """
        getBackgroundRatio() -> retval
        .   @brief Returns the "background ratio" parameter of the algorithm
        .   
        .   If a foreground pixel keeps semi-constant value for about backgroundRatio\*history frames, it's
        .   considered background and added to the model as a center of a new component. It corresponds to TB
        .   parameter in the paper.
        """
        pass

    def getComplexityReductionThreshold(self): # real signature unknown; restored from __doc__
        """
        getComplexityReductionThreshold() -> retval
        .   @brief Returns the complexity reduction threshold
        .   
        .   This parameter defines the number of samples needed to accept to prove the component exists. CT=0.05
        .   is a default value for all the samples. By setting CT=0 you get an algorithm very similar to the
        .   standard Stauffer&Grimson algorithm.
        """
        pass

    def getDetectShadows(self): # real signature unknown; restored from __doc__
        """
        getDetectShadows() -> retval
        .   @brief Returns the shadow detection flag
        .   
        .   If true, the algorithm detects shadows and marks them. See createBackgroundSubtractorMOG2 for
        .   details.
        """
        pass

    def getHistory(self): # real signature unknown; restored from __doc__
        """
        getHistory() -> retval
        .   @brief Returns the number of last frames that affect the background model
        """
        pass

    def getNMixtures(self): # real signature unknown; restored from __doc__
        """
        getNMixtures() -> retval
        .   @brief Returns the number of gaussian components in the background model
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

    def getVarInit(self): # real signature unknown; restored from __doc__
        """
        getVarInit() -> retval
        .   @brief Returns the initial variance of each gaussian component
        """
        pass

    def getVarMax(self): # real signature unknown; restored from __doc__
        """
        getVarMax() -> retval
        .
        """
        pass

    def getVarMin(self): # real signature unknown; restored from __doc__
        """
        getVarMin() -> retval
        .
        """
        pass

    def getVarThreshold(self): # real signature unknown; restored from __doc__
        """
        getVarThreshold() -> retval
        .   @brief Returns the variance threshold for the pixel-model match
        .   
        .   The main threshold on the squared Mahalanobis distance to decide if the sample is well described by
        .   the background model or not. Related to Cthr from the paper.
        """
        pass

    def getVarThresholdGen(self): # real signature unknown; restored from __doc__
        """
        getVarThresholdGen() -> retval
        .   @brief Returns the variance threshold for the pixel-model match used for new mixture component generation
        .   
        .   Threshold for the squared Mahalanobis distance that helps decide when a sample is close to the
        .   existing components (corresponds to Tg in the paper). If a pixel is not close to any component, it
        .   is considered foreground or added as a new component. 3 sigma =\> Tg=3\*3=9 is default. A smaller Tg
        .   value generates more components. A higher Tg value may result in a small number of components but
        .   they can grow too large.
        """
        pass

    def setBackgroundRatio(self, ratio): # real signature unknown; restored from __doc__
        """
        setBackgroundRatio(ratio) -> None
        .   @brief Sets the "background ratio" parameter of the algorithm
        """
        pass

    def setComplexityReductionThreshold(self, ct): # real signature unknown; restored from __doc__
        """
        setComplexityReductionThreshold(ct) -> None
        .   @brief Sets the complexity reduction threshold
        """
        pass

    def setDetectShadows(self, detectShadows): # real signature unknown; restored from __doc__
        """
        setDetectShadows(detectShadows) -> None
        .   @brief Enables or disables shadow detection
        """
        pass

    def setHistory(self, history): # real signature unknown; restored from __doc__
        """
        setHistory(history) -> None
        .   @brief Sets the number of last frames that affect the background model
        """
        pass

    def setNMixtures(self, nmixtures): # real signature unknown; restored from __doc__
        """
        setNMixtures(nmixtures) -> None
        .   @brief Sets the number of gaussian components in the background model.
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

    def setVarInit(self, varInit): # real signature unknown; restored from __doc__
        """
        setVarInit(varInit) -> None
        .   @brief Sets the initial variance of each gaussian component
        """
        pass

    def setVarMax(self, varMax): # real signature unknown; restored from __doc__
        """
        setVarMax(varMax) -> None
        .
        """
        pass

    def setVarMin(self, varMin): # real signature unknown; restored from __doc__
        """
        setVarMin(varMin) -> None
        .
        """
        pass

    def setVarThreshold(self, varThreshold): # real signature unknown; restored from __doc__
        """
        setVarThreshold(varThreshold) -> None
        .   @brief Sets the variance threshold for the pixel-model match
        """
        pass

    def setVarThresholdGen(self, varThresholdGen): # real signature unknown; restored from __doc__
        """
        setVarThresholdGen(varThresholdGen) -> None
        .   @brief Sets the variance threshold for the pixel-model match used for new mixture component generation
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


