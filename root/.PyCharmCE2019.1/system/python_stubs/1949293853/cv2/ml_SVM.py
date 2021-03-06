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


from .ml_StatModel import ml_StatModel

class ml_SVM(ml_StatModel):
    # no doc
    def create(self): # real signature unknown; restored from __doc__
        """
        create() -> retval
        .   Creates empty model.
        .   Use StatModel::train to train the model. Since %SVM has several parameters, you may want to
        .   find the best parameters for your problem, it can be done with SVM::trainAuto.
        """
        pass

    def getC(self): # real signature unknown; restored from __doc__
        """
        getC() -> retval
        .   @see setC
        """
        pass

    def getClassWeights(self): # real signature unknown; restored from __doc__
        """
        getClassWeights() -> retval
        .   @see setClassWeights
        """
        pass

    def getCoef0(self): # real signature unknown; restored from __doc__
        """
        getCoef0() -> retval
        .   @see setCoef0
        """
        pass

    def getDecisionFunction(self, i, alpha=None, svidx=None): # real signature unknown; restored from __doc__
        """
        getDecisionFunction(i[, alpha[, svidx]]) -> retval, alpha, svidx
        .   @brief Retrieves the decision function
        .   
        .   @param i the index of the decision function. If the problem solved is regression, 1-class or
        .   2-class classification, then there will be just one decision function and the index should
        .   always be 0. Otherwise, in the case of N-class classification, there will be \f$N(N-1)/2\f$
        .   decision functions.
        .   @param alpha the optional output vector for weights, corresponding to different support vectors.
        .   In the case of linear %SVM all the alpha's will be 1's.
        .   @param svidx the optional output vector of indices of support vectors within the matrix of
        .   support vectors (which can be retrieved by SVM::getSupportVectors). In the case of linear
        .   %SVM each decision function consists of a single "compressed" support vector.
        .   
        .   The method returns rho parameter of the decision function, a scalar subtracted from the weighted
        .   sum of kernel responses.
        """
        pass

    def getDefaultGridPtr(self, param_id): # real signature unknown; restored from __doc__
        """
        getDefaultGridPtr(param_id) -> retval
        .   @brief Generates a grid for %SVM parameters.
        .   
        .   @param param_id %SVM parameters IDs that must be one of the SVM::ParamTypes. The grid is
        .   generated for the parameter with this ID.
        .   
        .   The function generates a grid pointer for the specified parameter of the %SVM algorithm.
        .   The grid may be passed to the function SVM::trainAuto.
        """
        pass

    def getDegree(self): # real signature unknown; restored from __doc__
        """
        getDegree() -> retval
        .   @see setDegree
        """
        pass

    def getGamma(self): # real signature unknown; restored from __doc__
        """
        getGamma() -> retval
        .   @see setGamma
        """
        pass

    def getKernelType(self): # real signature unknown; restored from __doc__
        """
        getKernelType() -> retval
        .   Type of a %SVM kernel.
        .   See SVM::KernelTypes. Default value is SVM::RBF.
        """
        pass

    def getNu(self): # real signature unknown; restored from __doc__
        """
        getNu() -> retval
        .   @see setNu
        """
        pass

    def getP(self): # real signature unknown; restored from __doc__
        """
        getP() -> retval
        .   @see setP
        """
        pass

    def getSupportVectors(self): # real signature unknown; restored from __doc__
        """
        getSupportVectors() -> retval
        .   @brief Retrieves all the support vectors
        .   
        .   The method returns all the support vectors as a floating-point matrix, where support vectors are
        .   stored as matrix rows.
        """
        pass

    def getTermCriteria(self): # real signature unknown; restored from __doc__
        """
        getTermCriteria() -> retval
        .   @see setTermCriteria
        """
        pass

    def getType(self): # real signature unknown; restored from __doc__
        """
        getType() -> retval
        .   @see setType
        """
        pass

    def getUncompressedSupportVectors(self): # real signature unknown; restored from __doc__
        """
        getUncompressedSupportVectors() -> retval
        .   @brief Retrieves all the uncompressed support vectors of a linear %SVM
        .   
        .   The method returns all the uncompressed support vectors of a linear %SVM that the compressed
        .   support vector, used for prediction, was derived from. They are returned in a floating-point
        .   matrix, where the support vectors are stored as matrix rows.
        """
        pass

    def load(self, filepath): # real signature unknown; restored from __doc__
        """
        load(filepath) -> retval
        .   @brief Loads and creates a serialized svm from a file
        .   *
        .   * Use SVM::save to serialize and store an SVM to disk.
        .   * Load the SVM from this file again, by calling this function with the path to the file.
        .   *
        .   * @param filepath path to serialized svm
        """
        pass

    def setC(self, val): # real signature unknown; restored from __doc__
        """
        setC(val) -> None
        .   @copybrief getC @see getC
        """
        pass

    def setClassWeights(self, val): # real signature unknown; restored from __doc__
        """
        setClassWeights(val) -> None
        .   @copybrief getClassWeights @see getClassWeights
        """
        pass

    def setCoef0(self, val): # real signature unknown; restored from __doc__
        """
        setCoef0(val) -> None
        .   @copybrief getCoef0 @see getCoef0
        """
        pass

    def setDegree(self, val): # real signature unknown; restored from __doc__
        """
        setDegree(val) -> None
        .   @copybrief getDegree @see getDegree
        """
        pass

    def setGamma(self, val): # real signature unknown; restored from __doc__
        """
        setGamma(val) -> None
        .   @copybrief getGamma @see getGamma
        """
        pass

    def setKernel(self, kernelType): # real signature unknown; restored from __doc__
        """
        setKernel(kernelType) -> None
        .   Initialize with one of predefined kernels.
        .   See SVM::KernelTypes.
        """
        pass

    def setNu(self, val): # real signature unknown; restored from __doc__
        """
        setNu(val) -> None
        .   @copybrief getNu @see getNu
        """
        pass

    def setP(self, val): # real signature unknown; restored from __doc__
        """
        setP(val) -> None
        .   @copybrief getP @see getP
        """
        pass

    def setTermCriteria(self, val): # real signature unknown; restored from __doc__
        """
        setTermCriteria(val) -> None
        .   @copybrief getTermCriteria @see getTermCriteria
        """
        pass

    def setType(self, val): # real signature unknown; restored from __doc__
        """
        setType(val) -> None
        .   @copybrief getType @see getType
        """
        pass

    def trainAuto(self, samples, layout, responses, kFold=None, Cgrid=None, gammaGrid=None, pGrid=None, nuGrid=None, coeffGrid=None, degreeGrid=None, balanced=None): # real signature unknown; restored from __doc__
        """
        trainAuto(samples, layout, responses[, kFold[, Cgrid[, gammaGrid[, pGrid[, nuGrid[, coeffGrid[, degreeGrid[, balanced]]]]]]]]) -> retval
        .   @brief Trains an %SVM with optimal parameters
        .   
        .   @param samples training samples
        .   @param layout See ml::SampleTypes.
        .   @param responses vector of responses associated with the training samples.
        .   @param kFold Cross-validation parameter. The training set is divided into kFold subsets. One
        .   subset is used to test the model, the others form the train set. So, the %SVM algorithm is
        .   @param Cgrid grid for C
        .   @param gammaGrid grid for gamma
        .   @param pGrid grid for p
        .   @param nuGrid grid for nu
        .   @param coeffGrid grid for coeff
        .   @param degreeGrid grid for degree
        .   @param balanced If true and the problem is 2-class classification then the method creates more
        .   balanced cross-validation subsets that is proportions between classes in subsets are close
        .   to such proportion in the whole train dataset.
        .   
        .   The method trains the %SVM model automatically by choosing the optimal parameters C, gamma, p,
        .   nu, coef0, degree. Parameters are considered optimal when the cross-validation
        .   estimate of the test set error is minimal.
        .   
        .   This function only makes use of SVM::getDefaultGrid for parameter optimization and thus only
        .   offers rudimentary parameter options.
        .   
        .   This function works for the classification (SVM::C_SVC or SVM::NU_SVC) as well as for the
        .   regression (SVM::EPS_SVR or SVM::NU_SVR). If it is SVM::ONE_CLASS, no optimization is made and
        .   the usual %SVM with parameters specified in params is executed.
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


