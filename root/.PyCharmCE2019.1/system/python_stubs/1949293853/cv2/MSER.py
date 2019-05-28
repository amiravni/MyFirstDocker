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


from .Feature2D import Feature2D

class MSER(Feature2D):
    # no doc
    def create(self, _delta=None, _min_area=None, _max_area=None, _max_variation=None, _min_diversity=None, _max_evolution=None, _area_threshold=None, _min_margin=None, _edge_blur_size=None): # real signature unknown; restored from __doc__
        """
        create([, _delta[, _min_area[, _max_area[, _max_variation[, _min_diversity[, _max_evolution[, _area_threshold[, _min_margin[, _edge_blur_size]]]]]]]]]) -> retval
        .   @brief Full consturctor for %MSER detector
        .   
        .   @param _delta it compares \f$(size_{i}-size_{i-delta})/size_{i-delta}\f$
        .   @param _min_area prune the area which smaller than minArea
        .   @param _max_area prune the area which bigger than maxArea
        .   @param _max_variation prune the area have similar size to its children
        .   @param _min_diversity for color image, trace back to cut off mser with diversity less than min_diversity
        .   @param _max_evolution  for color image, the evolution steps
        .   @param _area_threshold for color image, the area threshold to cause re-initialize
        .   @param _min_margin for color image, ignore too small margin
        .   @param _edge_blur_size for color image, the aperture size for edge blur
        """
        pass

    def detectRegions(self, image): # real signature unknown; restored from __doc__
        """
        detectRegions(image) -> msers, bboxes
        .   @brief Detect %MSER regions
        .   
        .   @param image input image (8UC1, 8UC3 or 8UC4, must be greater or equal than 3x3)
        .   @param msers resulting list of point sets
        .   @param bboxes resulting bounding boxes
        """
        pass

    def getDefaultName(self): # real signature unknown; restored from __doc__
        """
        getDefaultName() -> retval
        .
        """
        pass

    def getDelta(self): # real signature unknown; restored from __doc__
        """
        getDelta() -> retval
        .
        """
        pass

    def getMaxArea(self): # real signature unknown; restored from __doc__
        """
        getMaxArea() -> retval
        .
        """
        pass

    def getMinArea(self): # real signature unknown; restored from __doc__
        """
        getMinArea() -> retval
        .
        """
        pass

    def getPass2Only(self): # real signature unknown; restored from __doc__
        """
        getPass2Only() -> retval
        .
        """
        pass

    def setDelta(self, delta): # real signature unknown; restored from __doc__
        """
        setDelta(delta) -> None
        .
        """
        pass

    def setMaxArea(self, maxArea): # real signature unknown; restored from __doc__
        """
        setMaxArea(maxArea) -> None
        .
        """
        pass

    def setMinArea(self, minArea): # real signature unknown; restored from __doc__
        """
        setMinArea(minArea) -> None
        .
        """
        pass

    def setPass2Only(self, f): # real signature unknown; restored from __doc__
        """
        setPass2Only(f) -> None
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


