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

class BOWTrainer(object):
    # no doc
    def add(self, descriptors): # real signature unknown; restored from __doc__
        """
        add(descriptors) -> None
        .   @brief Adds descriptors to a training set.
        .   
        .   @param descriptors Descriptors to add to a training set. Each row of the descriptors matrix is a
        .   descriptor.
        .   
        .   The training set is clustered using clustermethod to construct the vocabulary.
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """
        clear() -> None
        .
        """
        pass

    def cluster(self): # real signature unknown; restored from __doc__
        """
        cluster() -> retval
        .   @overload
        
        
        
        cluster(descriptors) -> retval
        .   @brief Clusters train descriptors.
        .   
        .   @param descriptors Descriptors to cluster. Each row of the descriptors matrix is a descriptor.
        .   Descriptors are not added to the inner train descriptor set.
        .   
        .   The vocabulary consists of cluster centers. So, this method returns the vocabulary. In the first
        .   variant of the method, train descriptors stored in the object are clustered. In the second variant,
        .   input descriptors are clustered.
        """
        pass

    def descriptorsCount(self): # real signature unknown; restored from __doc__
        """
        descriptorsCount() -> retval
        .   @brief Returns the count of all descriptors stored in the training set.
        """
        pass

    def getDescriptors(self): # real signature unknown; restored from __doc__
        """
        getDescriptors() -> retval
        .   @brief Returns a training set of descriptors.
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


