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

class cuda_HostMem(object):
    # no doc
    def channels(self): # real signature unknown; restored from __doc__
        """
        channels() -> retval
        .
        """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """
        clone() -> retval
        .
        """
        pass

    def create(self, rows, cols, type): # real signature unknown; restored from __doc__
        """
        create(rows, cols, type) -> None
        .
        """
        pass

    def createMatHeader(self): # real signature unknown; restored from __doc__
        """
        createMatHeader() -> retval
        .
        """
        pass

    def depth(self): # real signature unknown; restored from __doc__
        """
        depth() -> retval
        .
        """
        pass

    def elemSize(self): # real signature unknown; restored from __doc__
        """
        elemSize() -> retval
        .
        """
        pass

    def elemSize1(self): # real signature unknown; restored from __doc__
        """
        elemSize1() -> retval
        .
        """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """
        empty() -> retval
        .
        """
        pass

    def isContinuous(self): # real signature unknown; restored from __doc__
        """
        isContinuous() -> retval
        .   @brief Maps CPU memory to GPU address space and creates the cuda::GpuMat header without reference counting
        .   for it.
        .   
        .   This can be done only if memory was allocated with the SHARED flag and if it is supported by the
        .   hardware. Laptops often share video and CPU memory, so address spaces can be mapped, which
        .   eliminates an extra copy.
        """
        pass

    def reshape(self, cn, rows=None): # real signature unknown; restored from __doc__
        """
        reshape(cn[, rows]) -> retval
        .
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """
        size() -> retval
        .
        """
        pass

    def step1(self): # real signature unknown; restored from __doc__
        """
        step1() -> retval
        .
        """
        pass

    def swap(self, b): # real signature unknown; restored from __doc__
        """
        swap(b) -> None
        .
        """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """
        type() -> retval
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

    step = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """step"""



