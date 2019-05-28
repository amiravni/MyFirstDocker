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


class dnn_Layer(__cv2.Algorithm):
    # no doc
    def finalize(self, inputs, outputs=None): # real signature unknown; restored from __doc__
        """
        finalize(inputs[, outputs]) -> outputs
        .   @brief Computes and sets internal parameters according to inputs, outputs and blobs.
        .   *  @param[in]  inputs  vector of already allocated input blobs
        .   *  @param[out] outputs vector of already allocated output blobs
        .   *
        .   * If this method is called after network has allocated all memory for input and output blobs
        .   * and before inferencing.
        """
        pass

    def outputNameToIndex(self, outputName): # real signature unknown; restored from __doc__
        """
        outputNameToIndex(outputName) -> retval
        .   @brief Returns index of output blob in output array.
        .   *  @see inputNameToIndex()
        """
        pass

    def run(self, inputs, internals, outputs=None): # real signature unknown; restored from __doc__
        """
        run(inputs, internals[, outputs]) -> outputs, internals
        .   @brief Allocates layer and computes output.
        .   *  @deprecated This method will be removed in the future release.
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

    blobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """blobs"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name"""

    preferableTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """preferableTarget"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """type"""



