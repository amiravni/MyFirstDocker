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

class cuda_Stream(object):
    # no doc
    def Null(self): # real signature unknown; restored from __doc__
        """
        Null() -> retval
        .   @brief Adds a callback to be called on the host after all currently enqueued items in the stream have
        .   completed.
        .   
        .   @note Callbacks must not make any CUDA API calls. Callbacks must not perform any synchronization
        .   that may depend on outstanding device work or other callbacks that are not mandated to run earlier.
        .   Callbacks without a mandated order (in independent streams) execute in undefined order and may be
        .   serialized.
        """
        pass

    def queryIfComplete(self): # real signature unknown; restored from __doc__
        """
        queryIfComplete() -> retval
        .   @brief Returns true if the current stream queue is finished. Otherwise, it returns false.
        """
        pass

    def waitEvent(self, event): # real signature unknown; restored from __doc__
        """
        waitEvent(event) -> None
        .   @brief Makes a compute stream wait on an event.
        """
        pass

    def waitForCompletion(self): # real signature unknown; restored from __doc__
        """
        waitForCompletion() -> None
        .   @brief Blocks the current CPU thread until all operations in the stream are complete.
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


