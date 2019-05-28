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

class Stitcher(object):
    # no doc
    def composePanorama(self, pano=None): # real signature unknown; restored from __doc__
        """
        composePanorama([, pano]) -> retval, pano
        .   @overload
        """
        pass

    def compositingResol(self): # real signature unknown; restored from __doc__
        """
        compositingResol() -> retval
        .
        """
        pass

    def create(self, mode=None): # real signature unknown; restored from __doc__
        """
        create([, mode]) -> retval
        .   @brief Creates a Stitcher configured in one of the stitching modes.
        .   
        .   @param mode Scenario for stitcher operation. This is usually determined by source of images
        .   to stitch and their transformation. Default parameters will be chosen for operation in given
        .   scenario.
        .   @return Stitcher class instance.
        """
        pass

    def estimateTransform(self, images, masks=None): # real signature unknown; restored from __doc__
        """
        estimateTransform(images[, masks]) -> retval
        .   @brief These functions try to match the given images and to estimate rotations of each camera.
        .   
        .   @note Use the functions only if you're aware of the stitching pipeline, otherwise use
        .   Stitcher::stitch.
        .   
        .   @param images Input images.
        .   @param masks Masks for each input image specifying where to look for keypoints (optional).
        .   @return Status code.
        """
        pass

    def interpolationFlags(self): # real signature unknown; restored from __doc__
        """
        interpolationFlags() -> retval
        .
        """
        pass

    def panoConfidenceThresh(self): # real signature unknown; restored from __doc__
        """
        panoConfidenceThresh() -> retval
        .
        """
        pass

    def registrationResol(self): # real signature unknown; restored from __doc__
        """
        registrationResol() -> retval
        .
        """
        pass

    def seamEstimationResol(self): # real signature unknown; restored from __doc__
        """
        seamEstimationResol() -> retval
        .
        """
        pass

    def setCompositingResol(self, resol_mpx): # real signature unknown; restored from __doc__
        """
        setCompositingResol(resol_mpx) -> None
        .
        """
        pass

    def setInterpolationFlags(self, interp_flags): # real signature unknown; restored from __doc__
        """
        setInterpolationFlags(interp_flags) -> None
        .
        """
        pass

    def setPanoConfidenceThresh(self, conf_thresh): # real signature unknown; restored from __doc__
        """
        setPanoConfidenceThresh(conf_thresh) -> None
        .
        """
        pass

    def setRegistrationResol(self, resol_mpx): # real signature unknown; restored from __doc__
        """
        setRegistrationResol(resol_mpx) -> None
        .
        """
        pass

    def setSeamEstimationResol(self, resol_mpx): # real signature unknown; restored from __doc__
        """
        setSeamEstimationResol(resol_mpx) -> None
        .
        """
        pass

    def setWaveCorrection(self, flag): # real signature unknown; restored from __doc__
        """
        setWaveCorrection(flag) -> None
        .
        """
        pass

    def stitch(self, images, pano=None): # real signature unknown; restored from __doc__
        """
        stitch(images[, pano]) -> retval, pano
        .   @overload
        
        
        
        stitch(images, masks[, pano]) -> retval, pano
        .   @brief These functions try to stitch the given images.
        .   
        .   @param images Input images.
        .   @param masks Masks for each input image specifying where to look for keypoints (optional).
        .   @param pano Final pano.
        .   @return Status code.
        """
        pass

    def waveCorrection(self): # real signature unknown; restored from __doc__
        """
        waveCorrection() -> retval
        .
        """
        pass

    def workScale(self): # real signature unknown; restored from __doc__
        """
        workScale() -> retval
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


