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

class detail_ExposureCompensator(object):
    # no doc
    def apply(self, index, corner, image, mask): # real signature unknown; restored from __doc__
        """
        apply(index, corner, image, mask) -> image
        .   @brief Compensate exposure in the specified image.
        .   
        .   @param index Image index
        .   @param corner Image top-left corner
        .   @param image Image to process
        .   @param mask Image mask
        """
        pass

    def createDefault(self, type): # real signature unknown; restored from __doc__
        """
        createDefault(type) -> retval
        .
        """
        pass

    def feed(self, corners, images, masks): # real signature unknown; restored from __doc__
        """
        feed(corners, images, masks) -> None
        .   @param corners Source image top-left corners
        .   @param images Source images
        .   @param masks Image masks to update (second value in pair specifies the value which should be used
        .   to detect where image is)
        """
        pass

    def getMatGains(self, arg1=None): # real signature unknown; restored from __doc__
        """
        getMatGains([, arg1]) -> arg1
        .
        """
        pass

    def getUpdateGain(self): # real signature unknown; restored from __doc__
        """
        getUpdateGain() -> retval
        .
        """
        pass

    def setMatGains(self, arg1): # real signature unknown; restored from __doc__
        """
        setMatGains(arg1) -> None
        .
        """
        pass

    def setUpdateGain(self, b): # real signature unknown; restored from __doc__
        """
        setUpdateGain(b) -> None
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


