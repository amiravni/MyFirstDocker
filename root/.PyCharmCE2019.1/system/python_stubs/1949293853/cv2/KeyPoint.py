# encoding: utf-8
# module cv2 calls itself cv2.cv2
# from /opt/ros/kinetic/lib/python2.7/dist-packages/cv2.so
# by generator 1.147
""" Python wrapper for OpenCV. """

# imports
import cv2.cv2 as  # /usr/local/lib/python3.5/dist-packages/cv2/cv2.cpython-35m-x86_64-linux-gnu.so
import cv2.detail as detail # <module 'cv2.detail'>
import cv2.ml as ml # <module 'cv2.ml'>
import os as os # /usr/lib/python3.5/os.py
import cv2.data as data # /usr/local/lib/python3.5/dist-packages/cv2/data/__init__.py
import cv2.cuda as cuda # <module 'cv2.cuda'>
import cv2.ogl as ogl # <module 'cv2.ogl'>
import cv2.samples as samples # <module 'cv2.samples'>
import cv2.Error as Error # <module 'cv2.Error'>
import cv2.ipp as ipp # <module 'cv2.ipp'>
import cv2.flann as flann # <module 'cv2.flann'>
import cv2.instr as instr # <module 'cv2.instr'>
import importlib as importlib # /usr/lib/python3.5/importlib/__init__.py
import cv2.ocl as ocl # <module 'cv2.ocl'>
import cv2.videoio_registry as videoio_registry # <module 'cv2.videoio_registry'>
import cv2.utils as utils # <module 'cv2.utils'>
import cv2.cv2 as cv2 # /usr/local/lib/python3.5/dist-packages/cv2/cv2.cpython-35m-x86_64-linux-gnu.so
import cv2.dnn as dnn # <module 'cv2.dnn'>
import cv2.fisheye as fisheye # <module 'cv2.fisheye'>
from cv2.cv2 import (createButton, createTrackbar, dnn_registerLayer, 
    dnn_unregisterLayer, redirectError, setMouseCallback)


from .object import object

class KeyPoint(object):
    # no doc
    def convert(self, keypoints, keypointIndexes=None): # real signature unknown; restored from __doc__
        """
        convert(keypoints[, keypointIndexes]) -> points2f
        .   This method converts vector of keypoints to vector of points or the reverse, where each keypoint is
        .   assigned the same size and the same orientation.
        .   
        .   @param keypoints Keypoints obtained from any feature detection algorithm like SIFT/SURF/ORB
        .   @param points2f Array of (x,y) coordinates of each keypoint
        .   @param keypointIndexes Array of indexes of keypoints to be converted to points. (Acts like a mask to
        .   convert only specified keypoints)
        
        
        
        convert(points2f[, size[, response[, octave[, class_id]]]]) -> keypoints
        .   @overload
        .   @param points2f Array of (x,y) coordinates of each keypoint
        .   @param keypoints Keypoints obtained from any feature detection algorithm like SIFT/SURF/ORB
        .   @param size keypoint diameter
        .   @param response keypoint detector response on the keypoint (that is, strength of the keypoint)
        .   @param octave pyramid octave in which the keypoint has been detected
        .   @param class_id object id
        """
        pass

    def overlap(self, kp1, kp2): # real signature unknown; restored from __doc__
        """
        overlap(kp1, kp2) -> retval
        .   This method computes overlap for pair of keypoints. Overlap is the ratio between area of keypoint
        .   regions' intersection and area of keypoint regions' union (considering keypoint region as circle).
        .   If they don't overlap, we get zero. If they coincide at same location with same size, we get 1.
        .   @param kp1 First keypoint
        .   @param kp2 Second keypoint
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

    angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """angle"""

    class_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """class_id"""

    octave = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """octave"""

    pt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """pt"""

    response = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """response"""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """size"""



