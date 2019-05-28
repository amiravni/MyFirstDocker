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


class StereoMatcher(__cv2.Algorithm):
    # no doc
    def compute(self, left, right, disparity=None): # real signature unknown; restored from __doc__
        """
        compute(left, right[, disparity]) -> disparity
        .   @brief Computes disparity map for the specified stereo pair
        .   
        .   @param left Left 8-bit single-channel image.
        .   @param right Right image of the same size and the same type as the left one.
        .   @param disparity Output disparity map. It has the same size as the input images. Some algorithms,
        .   like StereoBM or StereoSGBM compute 16-bit fixed-point disparity map (where each disparity value
        .   has 4 fractional bits), whereas other algorithms output 32-bit floating-point disparity map.
        """
        pass

    def getBlockSize(self): # real signature unknown; restored from __doc__
        """
        getBlockSize() -> retval
        .
        """
        pass

    def getDisp12MaxDiff(self): # real signature unknown; restored from __doc__
        """
        getDisp12MaxDiff() -> retval
        .
        """
        pass

    def getMinDisparity(self): # real signature unknown; restored from __doc__
        """
        getMinDisparity() -> retval
        .
        """
        pass

    def getNumDisparities(self): # real signature unknown; restored from __doc__
        """
        getNumDisparities() -> retval
        .
        """
        pass

    def getSpeckleRange(self): # real signature unknown; restored from __doc__
        """
        getSpeckleRange() -> retval
        .
        """
        pass

    def getSpeckleWindowSize(self): # real signature unknown; restored from __doc__
        """
        getSpeckleWindowSize() -> retval
        .
        """
        pass

    def setBlockSize(self, blockSize): # real signature unknown; restored from __doc__
        """
        setBlockSize(blockSize) -> None
        .
        """
        pass

    def setDisp12MaxDiff(self, disp12MaxDiff): # real signature unknown; restored from __doc__
        """
        setDisp12MaxDiff(disp12MaxDiff) -> None
        .
        """
        pass

    def setMinDisparity(self, minDisparity): # real signature unknown; restored from __doc__
        """
        setMinDisparity(minDisparity) -> None
        .
        """
        pass

    def setNumDisparities(self, numDisparities): # real signature unknown; restored from __doc__
        """
        setNumDisparities(numDisparities) -> None
        .
        """
        pass

    def setSpeckleRange(self, speckleRange): # real signature unknown; restored from __doc__
        """
        setSpeckleRange(speckleRange) -> None
        .
        """
        pass

    def setSpeckleWindowSize(self, speckleWindowSize): # real signature unknown; restored from __doc__
        """
        setSpeckleWindowSize(speckleWindowSize) -> None
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


