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


class BFMatcher(__cv2.DescriptorMatcher):
    # no doc
    def create(self, normType=None, crossCheck=None): # real signature unknown; restored from __doc__
        """
        create([, normType[, crossCheck]]) -> retval
        .   @brief Brute-force matcher create method.
        .   @param normType One of NORM_L1, NORM_L2, NORM_HAMMING, NORM_HAMMING2. L1 and L2 norms are
        .   preferable choices for SIFT and SURF descriptors, NORM_HAMMING should be used with ORB, BRISK and
        .   BRIEF, NORM_HAMMING2 should be used with ORB when WTA_K==3 or 4 (see ORB::ORB constructor
        .   description).
        .   @param crossCheck If it is false, this is will be default BFMatcher behaviour when it finds the k
        .   nearest neighbors for each query descriptor. If crossCheck==true, then the knnMatch() method with
        .   k=1 will only return pairs (i,j) such that for i-th query descriptor the j-th descriptor in the
        .   matcher's collection is the nearest and vice versa, i.e. the BFMatcher will only return consistent
        .   pairs. Such technique usually produces best results with minimal number of outliers when there are
        .   enough matches. This is alternative to the ratio test, used by D. Lowe in SIFT paper.
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


