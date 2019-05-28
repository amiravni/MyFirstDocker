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

class BOWImgDescriptorExtractor(object):
    # no doc
    def compute(self, image, keypoints, imgDescriptor=None): # real signature unknown; restored from __doc__
        """
        compute(image, keypoints[, imgDescriptor]) -> imgDescriptor
        .   @overload
        .   @param keypointDescriptors Computed descriptors to match with vocabulary.
        .   @param imgDescriptor Computed output image descriptor.
        .   @param pointIdxsOfClusters Indices of keypoints that belong to the cluster. This means that
        .   pointIdxsOfClusters[i] are keypoint indices that belong to the i -th cluster (word of vocabulary)
        .   returned if it is non-zero.
        """
        pass

    def descriptorSize(self): # real signature unknown; restored from __doc__
        """
        descriptorSize() -> retval
        .   @brief Returns an image descriptor size if the vocabulary is set. Otherwise, it returns 0.
        """
        pass

    def descriptorType(self): # real signature unknown; restored from __doc__
        """
        descriptorType() -> retval
        .   @brief Returns an image descriptor type.
        """
        pass

    def getVocabulary(self): # real signature unknown; restored from __doc__
        """
        getVocabulary() -> retval
        .   @brief Returns the set vocabulary.
        """
        pass

    def setVocabulary(self, vocabulary): # real signature unknown; restored from __doc__
        """
        setVocabulary(vocabulary) -> None
        .   @brief Sets a visual vocabulary.
        .   
        .   @param vocabulary Vocabulary (can be trained using the inheritor of BOWTrainer ). Each row of the
        .   vocabulary is a visual word (cluster center).
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


