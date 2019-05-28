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


class ml_Boost(__cv2.ml_DTrees):
    # no doc
    def create(self): # real signature unknown; restored from __doc__
        """
        create() -> retval
        .   Creates the empty model.
        .   Use StatModel::train to train the model, Algorithm::load\<Boost\>(filename) to load the pre-trained model.
        """
        pass

    def getBoostType(self): # real signature unknown; restored from __doc__
        """
        getBoostType() -> retval
        .   @see setBoostType
        """
        pass

    def getWeakCount(self): # real signature unknown; restored from __doc__
        """
        getWeakCount() -> retval
        .   @see setWeakCount
        """
        pass

    def getWeightTrimRate(self): # real signature unknown; restored from __doc__
        """
        getWeightTrimRate() -> retval
        .   @see setWeightTrimRate
        """
        pass

    def load(self, filepath, nodeName=None): # real signature unknown; restored from __doc__
        """
        load(filepath[, nodeName]) -> retval
        .   @brief Loads and creates a serialized Boost from a file
        .   *
        .   * Use Boost::save to serialize and store an RTree to disk.
        .   * Load the Boost from this file again, by calling this function with the path to the file.
        .   * Optionally specify the node for the file containing the classifier
        .   *
        .   * @param filepath path to serialized Boost
        .   * @param nodeName name of node containing the classifier
        """
        pass

    def setBoostType(self, val): # real signature unknown; restored from __doc__
        """
        setBoostType(val) -> None
        .   @copybrief getBoostType @see getBoostType
        """
        pass

    def setWeakCount(self, val): # real signature unknown; restored from __doc__
        """
        setWeakCount(val) -> None
        .   @copybrief getWeakCount @see getWeakCount
        """
        pass

    def setWeightTrimRate(self, val): # real signature unknown; restored from __doc__
        """
        setWeightTrimRate(val) -> None
        .   @copybrief getWeightTrimRate @see getWeightTrimRate
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


