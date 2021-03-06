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

class detail_FeaturesMatcher(object):
    # no doc
    def apply(self, features1, features2): # real signature unknown; restored from __doc__
        """
        apply(features1, features2) -> matches_info
        .   @overload
        .   @param features1 First image features
        .   @param features2 Second image features
        .   @param matches_info Found matches
        """
        pass

    def apply2(self, features, mask=None): # real signature unknown; restored from __doc__
        """
        apply2(features[, mask]) -> pairwise_matches
        .   @brief Performs images matching.
        .   
        .   @param features Features of the source images
        .   @param pairwise_matches Found pairwise matches
        .   @param mask Mask indicating which image pairs must be matched
        .   
        .   The function is parallelized with the TBB library.
        .   
        .   @sa detail::MatchesInfo
        """
        pass

    def collectGarbage(self): # real signature unknown; restored from __doc__
        """
        collectGarbage() -> None
        .   @brief Frees unused memory allocated before if there is any.
        """
        pass

    def isThreadSafe(self): # real signature unknown; restored from __doc__
        """
        isThreadSafe() -> retval
        .   @return True, if it's possible to use the same matcher instance in parallel, false otherwise
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


