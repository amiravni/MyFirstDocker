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

class VideoWriter(object):
    # no doc
    def fourcc(self, c1, c2, c3, c4): # real signature unknown; restored from __doc__
        """
        fourcc(c1, c2, c3, c4) -> retval
        .   @brief Concatenates 4 chars to a fourcc code
        .   
        .   @return a fourcc code
        .   
        .   This static method constructs the fourcc code of the codec to be used in the constructor
        .   VideoWriter::VideoWriter or VideoWriter::open.
        """
        pass

    def get(self, propId): # real signature unknown; restored from __doc__
        """
        get(propId) -> retval
        .   @brief Returns the specified VideoWriter property
        .   
        .   @param propId Property identifier from cv::VideoWriterProperties (eg. cv::VIDEOWRITER_PROP_QUALITY)
        .   or one of @ref videoio_flags_others
        .   
        .   @return Value for the specified property. Value 0 is returned when querying a property that is
        .   not supported by the backend used by the VideoWriter instance.
        """
        pass

    def getBackendName(self): # real signature unknown; restored from __doc__
        """
        getBackendName() -> retval
        .   @brief Returns used backend API name
        .   
        .   @note Stream should be opened.
        """
        pass

    def isOpened(self): # real signature unknown; restored from __doc__
        """
        isOpened() -> retval
        .   @brief Returns true if video writer has been successfully initialized.
        """
        pass

    def open(self, filename, fourcc, fps, frameSize, isColor=None): # real signature unknown; restored from __doc__
        """
        open(filename, fourcc, fps, frameSize[, isColor]) -> retval
        .   @brief Initializes or reinitializes video writer.
        .   
        .   The method opens video writer. Parameters are the same as in the constructor
        .   VideoWriter::VideoWriter.
        .   @return `true` if video writer has been successfully initialized
        .   
        .   The method first calls VideoWriter::release to close the already opened file.
        
        
        
        open(filename, apiPreference, fourcc, fps, frameSize[, isColor]) -> retval
        .   @overload
        """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """
        release() -> None
        .   @brief Closes the video writer.
        .   
        .   The method is automatically called by subsequent VideoWriter::open and by the VideoWriter
        .   destructor.
        """
        pass

    def set(self, propId, value): # real signature unknown; restored from __doc__
        """
        set(propId, value) -> retval
        .   @brief Sets a property in the VideoWriter.
        .   
        .   @param propId Property identifier from cv::VideoWriterProperties (eg. cv::VIDEOWRITER_PROP_QUALITY)
        .   or one of @ref videoio_flags_others
        .   
        .   @param value Value of the property.
        .   @return  `true` if the property is supported by the backend used by the VideoWriter instance.
        """
        pass

    def write(self, image): # real signature unknown; restored from __doc__
        """
        write(image) -> None
        .   @brief Writes the next video frame
        .   
        .   @param image The written frame. In general, color images are expected in BGR format.
        .   
        .   The function/method writes the specified image to video file. It must have the same size as has
        .   been specified when opening the video writer.
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


