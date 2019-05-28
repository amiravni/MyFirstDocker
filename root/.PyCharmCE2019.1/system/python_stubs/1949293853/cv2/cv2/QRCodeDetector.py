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

class QRCodeDetector(object):
    # no doc
    def decode(self, img, points, straight_qrcode=None): # real signature unknown; restored from __doc__
        """
        decode(img, points[, straight_qrcode]) -> retval, straight_qrcode
        .   @brief Decodes QR code in image once it's found by the detect() method.
        .   Returns UTF8-encoded output string or empty string if the code cannot be decoded.
        .   
        .   @param img grayscale or color (BGR) image containing QR code.
        .   @param points Quadrangle vertices found by detect() method (or some other algorithm).
        .   @param straight_qrcode The optional output image containing rectified and binarized QR code
        """
        pass

    def detect(self, img, points=None): # real signature unknown; restored from __doc__
        """
        detect(img[, points]) -> retval, points
        .   @brief Detects QR code in image and returns the quadrangle containing the code.
        .   @param img grayscale or color (BGR) image containing (or not) QR code.
        .   @param points Output vector of vertices of the minimum-area quadrangle containing the code.
        """
        pass

    def detectAndDecode(self, img, points=None, straight_qrcode=None): # real signature unknown; restored from __doc__
        """
        detectAndDecode(img[, points[, straight_qrcode]]) -> retval, points, straight_qrcode
        .   @brief Both detects and decodes QR code
        .   
        .   @param img grayscale or color (BGR) image containing QR code.
        .   @param points opiotnal output array of vertices of the found QR code quadrangle. Will be empty if not found.
        .   @param straight_qrcode The optional output image containing rectified and binarized QR code
        """
        pass

    def setEpsX(self, epsX): # real signature unknown; restored from __doc__
        """
        setEpsX(epsX) -> None
        .   @brief sets the epsilon used during the horizontal scan of QR code stop marker detection.
        .   @param epsX Epsilon neighborhood, which allows you to determine the horizontal pattern
        .   of the scheme 1:1:3:1:1 according to QR code standard.
        """
        pass

    def setEpsY(self, epsY): # real signature unknown; restored from __doc__
        """
        setEpsY(epsY) -> None
        .   @brief sets the epsilon used during the vertical scan of QR code stop marker detection.
        .   @param epsY Epsilon neighborhood, which allows you to determine the vertical pattern
        .   of the scheme 1:1:3:1:1 according to QR code standard.
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


