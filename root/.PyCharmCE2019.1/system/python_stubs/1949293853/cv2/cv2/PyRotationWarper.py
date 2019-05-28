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

class PyRotationWarper(object):
    # no doc
    def buildMaps(self, src_size, K, R, xmap=None, ymap=None): # real signature unknown; restored from __doc__
        """
        buildMaps(src_size, K, R[, xmap[, ymap]]) -> retval, xmap, ymap
        .   @brief Builds the projection maps according to the given camera data.
        .   
        .   @param src_size Source image size
        .   @param K Camera intrinsic parameters
        .   @param R Camera rotation matrix
        .   @param xmap Projection map for the x axis
        .   @param ymap Projection map for the y axis
        .   @return Projected image minimum bounding box
        """
        pass

    def getScale(self): # real signature unknown; restored from __doc__
        """
        getScale() -> retval
        .
        """
        pass

    def setScale(self, arg1): # real signature unknown; restored from __doc__
        """
        setScale(arg1) -> None
        .
        """
        pass

    def warp(self, src, K, R, interp_mode, border_mode, dst=None): # real signature unknown; restored from __doc__
        """
        warp(src, K, R, interp_mode, border_mode[, dst]) -> retval, dst
        .   @brief Projects the image.
        .   
        .   @param src Source image
        .   @param K Camera intrinsic parameters
        .   @param R Camera rotation matrix
        .   @param interp_mode Interpolation mode
        .   @param border_mode Border extrapolation mode
        .   @param dst Projected image
        .   @return Project image top-left corner
        """
        pass

    def warpBackward(self, src, K, R, interp_mode, border_mode, dst_size, dst=None): # real signature unknown; restored from __doc__
        """
        warpBackward(src, K, R, interp_mode, border_mode, dst_size[, dst]) -> dst
        .   @brief Projects the image backward.
        .   
        .   @param src Projected image
        .   @param K Camera intrinsic parameters
        .   @param R Camera rotation matrix
        .   @param interp_mode Interpolation mode
        .   @param border_mode Border extrapolation mode
        .   @param dst_size Backward-projected image size
        .   @param dst Backward-projected image
        """
        pass

    def warpPoint(self, pt, K, R): # real signature unknown; restored from __doc__
        """
        warpPoint(pt, K, R) -> retval
        .   @brief Projects the image point.
        .   
        .   @param pt Source point
        .   @param K Camera intrinsic parameters
        .   @param R Camera rotation matrix
        .   @return Projected point
        """
        pass

    def warpRoi(self, src_size, K, R): # real signature unknown; restored from __doc__
        """
        warpRoi(src_size, K, R) -> retval
        .   @param src_size Source image bounding box
        .   @param K Camera intrinsic parameters
        .   @param R Camera rotation matrix
        .   @return Projected image minimum bounding box
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


