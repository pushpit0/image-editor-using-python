#-------------------------------------------------------------#
# __name__ = "BasicImageEditor"
# __author__ = "Puspendra singh chauhan"
# __version__ = "1.0"
# __email__ = "pushpitsingh43@gmail.com"
# __status__ = "Development_in_progress"
# ---------------------------------------------------------------#


# PyQt5 libraries are used for GUI
from PyQt5 import QtCore, QtGui 


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# Class defining all GUI elements for Main application window
class ImageEditorGuiClass(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(886, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Dyuthi"))
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)

        # define layouts for the window
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.verticalLayout.addWidget(self.line_7)

        # define image display area
        self.imageDisplayLabel = QtGui.QLabel(self.centralwidget)
        self.imageDisplayLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageDisplayLabel.sizePolicy().hasHeightForWidth())
        self.imageDisplayLabel.setSizePolicy(sizePolicy)
        self.imageDisplayLabel.setAutoFillBackground(False)
        self.imageDisplayLabel.setStyleSheet(_fromUtf8("background-color: ","rgb(255, 255, 255);"))
        self.imageDisplayLabel.setText(_fromUtf8(""))
        self.imageDisplayLabel.setObjectName(_fromUtf8("imageDisplayLabel"))
        self.verticalLayout.addWidget(self.imageDisplayLabel)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 3, 2, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        # define Open button
        self.openImageButton = QtGui.QPushButton(self.centralwidget)
        self.openImageButton.setObjectName(_fromUtf8("openImageButton"))
        self.horizontalLayout.addWidget(self.openImageButton)

        # define Save button
        self.saveImageButton = QtGui.QPushButton(self.centralwidget)
        self.saveImageButton.setObjectName(_fromUtf8("saveImageButton"))
        self.saveImageButton.setEnabled(False)
        self.horizontalLayout.addWidget(self.saveImageButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout_3.addWidget(self.line_6)

        # define Histogram Equalization button
        self.histogramEqualizationButton = QtGui.QPushButton(self.centralwidget)
        self.histogramEqualizationButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogramEqualizationButton.sizePolicy().hasHeightForWidth())
        self.histogramEqualizationButton.setSizePolicy(sizePolicy)
        self.histogramEqualizationButton.setObjectName(_fromUtf8("histogramEqualizationButton"))
        self.verticalLayout_3.addWidget(self.histogramEqualizationButton)

        # define View Histogram button
        self.viewHistogramButton = QtGui.QPushButton(self.centralwidget)
        self.viewHistogramButton.setObjectName(_fromUtf8("viewHistogramButton"))
        self.verticalLayout_3.addWidget(self.viewHistogramButton)

        self.line_10 = QtGui.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.verticalLayout_3.addWidget(self.line_10)

        # define Gamma Correction button
        self.gammaCorrectionButton = QtGui.QPushButton(self.centralwidget)
        self.gammaCorrectionButton.setObjectName(_fromUtf8("gammaCorrectionButton"))
        self.gammaCorrectionButton.setEnabled(False)
        self.verticalLayout_3.addWidget(self.gammaCorrectionButton)

        # define Log Transform button
        self.logTransformButton = QtGui.QPushButton(self.centralwidget)
        self.logTransformButton.setObjectName(_fromUtf8("logTransformButton"))
        self.logTransformButton.setEnabled(False)
        self.verticalLayout_3.addWidget(self.logTransformButton)

        # define Image Negative button
        self.negativeButton = QtGui.QPushButton(self.centralwidget)
        self.negativeButton.setObjectName(_fromUtf8("negativeButton"))
        self.negativeButton.setEnabled(False)
        self.verticalLayout_3.addWidget(self.negativeButton)

        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))

        # define Blur Slider Name label
        self.blurLabel = QtGui.QLabel(self.centralwidget)
        self.blurLabel.setObjectName(_fromUtf8("blurLabel"))
        self.horizontalLayout_9.addWidget(self.blurLabel)

        self.blurValueLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blurValueLabel.sizePolicy().hasHeightForWidth())

        # define Blur Slider Value label
        self.blurValueLabel.setSizePolicy(sizePolicy)
        self.blurValueLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.blurValueLabel.setObjectName(_fromUtf8("blurValueLabel"))
        self.horizontalLayout_9.addWidget(self.blurValueLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        # define blur slider
        self.blurExtendInputSlider = QtGui.QSlider(self.centralwidget)
        self.blurExtendInputSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blurExtendInputSlider.setObjectName(_fromUtf8("blurExtendInputSlider"))
        self.blurExtendInputSlider.setRange(0,10)
        self.blurExtendInputSlider.setEnabled(False)
        self.verticalLayout_3.addWidget(self.blurExtendInputSlider)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_3.addWidget(self.line_3)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))

        # define Sharpen Slider Name label
        self.sharpenLabel = QtGui.QLabel(self.centralwidget)
        self.sharpenLabel.setObjectName(_fromUtf8("sharpenLabel"))
        self.horizontalLayout_10.addWidget(self.sharpenLabel)

        self.sharpenValueLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sharpenValueLabel.sizePolicy().hasHeightForWidth())

        # define Sharpen Slider Value label
        self.sharpenValueLabel.setSizePolicy(sizePolicy)
        self.sharpenValueLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sharpenValueLabel.setObjectName(_fromUtf8("sharpenValueLabel"))
        self.horizontalLayout_10.addWidget(self.sharpenValueLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        # define Sharpen Slider
        self.sharpenExtendInputSlider = QtGui.QSlider(self.centralwidget)
        self.sharpenExtendInputSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sharpenExtendInputSlider.setObjectName(_fromUtf8("sharpenExtendInputSlider"))
        self.sharpenExtendInputSlider.setRange(0, 10)
        self.sharpenExtendInputSlider.setEnabled(False)
        self.verticalLayout_3.addWidget(self.sharpenExtendInputSlider)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_3.addWidget(self.line_4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))

        # define Undo button
        self.undoButton = QtGui.QPushButton(self.centralwidget)
        self.undoButton.setObjectName(_fromUtf8("undoButton"))
        self.undoButton.setEnabled(False)
        self.horizontalLayout_4.addWidget(self.undoButton)

        # define Undo All button
        self.undoAllButton = QtGui.QPushButton(self.centralwidget)
        self.undoAllButton.setObjectName(_fromUtf8("undoAllButton"))
        self.undoAllButton.setEnabled(False)
        self.horizontalLayout_4.addWidget(self.undoAllButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)

        # define Edge Detection button
        self.detectEdgeButton = QtGui.QPushButton(self.centralwidget)
        self.detectEdgeButton.setObjectName(_fromUtf8("detectEdgeButton"))
        self.verticalLayout_3.addWidget(self.detectEdgeButton)

        self.line_9 = QtGui.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.verticalLayout_3.addWidget(self.line_9)

        self.detectEdgeButton.setEnabled(False)
        self.viewHistogramButton.setEnabled(False)

        # progress label is not used
        self.progressLabel = QtGui.QLabel(self.centralwidget)
        self.progressLabel.setText(_fromUtf8(""))
        self.progressLabel.setObjectName(_fromUtf8("progressLabel"))
        self.verticalLayout_3.addWidget(self.progressLabel)

        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 0, 1, 2)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))

        self.gridLayout_2.addWidget(self.line_5, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 886, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # Name all GUI elements
        MainWindow.setWindowTitle(_translate("MainWindow", "EE610 - Basic Image Editor", None))
        self.openImageButton.setText(_translate("MainWindow", "Open", None))
        self.saveImageButton.setText(_translate("MainWindow", "Save", None))
        self.histogramEqualizationButton.setText(_translate("MainWindow", "Histogram Equalization", None))
        self.gammaCorrectionButton.setText(_translate("MainWindow", "Gamma Correction", None))
        self.logTransformButton.setText(_translate("MinWindow", "Log Transform", None))
        self.negativeButton.setText(_translate("MainWindow", "Image Negative", None))
        self.blurLabel.\
            setText(_translate("MainWindow","<html><head/><body><p>Blur Image</p></body></html>", None))
        self.blurValueLabel.setText(_translate("MainWindow", "0", None))
        self.sharpenLabel.setText(_translate("MainWindow", "Sharpen Image", None))
        self.sharpenValueLabel.setText(_translate("MainWindow", "0", None))
        self.undoButton.setText(_translate("MainWindow", "Undo", None))
        self.undoAllButton.setText(_translate("MainWindow", "Undo All", None))
        self.detectEdgeButton.setText(_translate("MainWindow", "Edge Detection", None))
        self.viewHistogramButton.setText(_translate("MainWindow", "View Histogram", None))



        # Class defining all GUI elements for Gamma input window
    class InputDialogGuiClass(QtGui.tkFieDialog):

    # define class variable to store  integer value of gamma entered by user
        gamma = 1.0

        def __init__(self, parent):
            super(InputDialogGuiClass, self).__init__(parent)
            self.setupUi(self)

        # link functions with OK and Cancel button clicks
        self.cancelButton.clicked.connect(lambda: self.close_window())
        self.okButton.clicked.connect(lambda: self.accept_value())

    def setupUi(self, InputDialogGuiClass):
        InputDialogGuiClass.setObjectName(_fromUtf8("InputDialogGuiClass"))
        InputDialogGuiClass.setWindowModality(QtCore.Qt.WindowModal)
        InputDialogGuiClass.setFixedWidth(360)
        InputDialogGuiClass.setFixedHeight(140)
        self.verticalLayout = QtGui.QVBoxLayout(InputDialogGuiClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(InputDialogGuiClass)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.gammaInput = QtGui.QLineEdit(InputDialogGuiClass)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gammaInput.sizePolicy().hasHeightForWidth())
        self.gammaInput.setSizePolicy(sizePolicy)
        self.gammaInput.setObjectName(_fromUtf8("lineEdit"))
        self.gammaInput.setText('1.00')
        self.gammaInput.setValidator(QtGui.QDoubleValidator(0, 10.0, 2, self.gammaInput))
        self.horizontalLayout_2.addWidget(self.gammaInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(InputDialogGuiClass)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancelButton = QtGui.QPushButton(InputDialogGuiClass)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.okButton = QtGui.QPushButton(InputDialogGuiClass)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_3.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(InputDialogGuiClass)
        QtCore.QMetaObject.connectSlotsByName(InputDialogGuiClass)

    # close window on Close or Cancel button click
    def close_window(self):
        self.close()

    # update class variable when OK button clicked and close the window
    def accept_value(self):
        if self.gammaInput.text() and float(self.gammaInput.text()) <= 10.0:
            self.gamma = float(self.gammaInput.text())
            self.close()
            return True
        else:
            self.label_2.setStyleSheet("color: rgb(255, 0, 0);")


    def retranslateUi(self, InputDialogGuiClass):
        InputDialogGuiClass.setWindowTitle(_translate("InputDialogGuiClass","Enter Gamma Value", None))
        self.label.setText(_translate("InputDialogGuiClass", "Gamma", None))
        self.label_2.setText(_translate("InputDialog","NB: Enter a value between 0 and 10", None))
        self.cancelButton.setText(_translate("InputDialog", "Cancel", None))
        self.okButton.setText(_translate("InputDialog", "OK", None))


#178  
#imageProcessingFns.py
#@@ -0,0 +1,178 @@
# ---------------------------------------------------------------#
# __name__ = "BasicImageEditor_Assignment"
# __author__ = "Pushpendra singh"
# __version__ = "1.0"
# __email__ = "pushpitsingh43@gmail.com"
# __status__ = "Development_in_progress"
# ---------------------------------------------------------------#

# All array operations are performed using numpy library
import numpy as np
# OpenCV2 library is used for color space conversion only
import cv2

# This class defines the implementation of all image processing functions
class ImageProcessorClass(object):

    # compute negative of the image passed as ndarray
    def image_negative(self, image):
        # find no of rows and columns in the ndarray of image passed
        image_row = image.shape[0]
        image_column = image.shape[1]

        # convert image from HSV space to BGR space
        image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
        # create an array equivalent to image array with all values as 255
        output = np.uint8(255 * np.ones((image_row, image_column, 3)))
        # deduct image from the array of 255 i.e. each pixel is inverted
        output = output - image
        # convert image back to HSV from BGR
        output = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)

        #  return the computed image
        return output

    # compute histogram equalization of the image passed as ndarray
    def histogram_equalization(self, image):
        # find no of rows and columns in the ndarray of image passed
        image_row = image.shape[0]
        image_column = image.shape[1]

        # count the no of values corresponding to each value in the V channel of image
        # matrix give a minimum length of 256 to the counting to ensure all 256 pixel
        # values are covered or pixel values not available in image are set to zero
        pmf = np.bincount(image.ravel(), minlength=256)
        # compute pmf by dividing histogram by total no of pixels in image
        pmf = pmf / (image_row * image_column)
        # compute cdf as cumulative sum of pmf
        cdf = pmf.cumsum()
        # derive lookup for pixel values by multiplying cdf with 255 (max pixel value)
        # round the lookup to lower integer to avoid the pixel value 256
        pmf_lookup = np.uint8(np.floor(cdf * 255))

        # create a copy of input image
        output = image.copy()

        # for each pixel value replace the value with the corresponding value in
        # lookup generated
        for r in range(256):
            output[image == r] = pmf_lookup[r]

        #  return the computed image
        return output

    # compute gamma correction of the image passed as ndarray based on gamma value passed
    def gamma_correction(self, image, gamma):
        # to keep image pixel values in the range 0 to 255 define a
        # constant = 255/ (max value in gamma correction)
        normalization_const = 255.0 / np.float_power(255, gamma)

        # compute output = constant * in^gamma
        # float_power used to accommodate large values in in^gamma
        output = np.uint8(normalization_const * np.float_power(image, gamma))

        #  return the computed image
        return output

    # compute log transform of the image passed as ndarray
    def log_transform(self, image):
        # find no of rows and columns in the ndarray of image passed
        image_row = len(image)
        image_column = len(image[0])

        # to keep image pixel values in the range 0 to 255 define a
        # constant = 255/ (max value in log transform)
        normalization_const = 255 / (np.log2(256))

        # compute output = constant * log(input + 1)
        # 1 is added to input to avoid log(0)
        output = np.int8(normalization_const *np.log2(image + np.ones((image_row, image_column))))

        #  return the computed image
        return output

    # compute blurred image for the image passed as ndarray based on
    # window size passed
    def blur(self, image, window_size):
        # define blur window as square matrix of all 1s with
        # matrix size = window size passed
        window = np.ones((window_size, window_size), dtype=np.uint8)
        # perform convolution of image and window
        output = self.convolution(image, window)
        #  return the computed image
        return output

    # compute sharpened image for the image passed as ndarray based on
    # sharpen constant passed
    def sharp(self, image, sharp_const):
        # define window as standard 3x3 Laplacian
        window = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
        # compute output as image - constant * correlation of image and window
        output = image - sharp_const * self.correlation(image, window)

        # keep output pixels in range 0 to 255
        # replace pixels with value < 0 in output with 0
        output[output < 0] = 0
        # replace pixels with value > 255 in output with 255
        output[output > 255] = 255

        #  return the computed image
        return output

    # compute edges of the image passed as ndarray
    def edge_detection(self, image):
        # define window as standard 3x3 Laplacian
        window = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
        # perform correlation of image and window
        output = self.correlation(image, window)

        # keep output pixels in range 0 to 255
        # replace pixels with value < 0 in output with 0
        output[output < 0] = 0
        # replace pixels with value > 255 in output with 255
        output[output > 255] = 255

        #  return the computed image
        return output

    # compute convolution operation on image and window passed as ndarray
    # also normalizes output values by dividing with sum of window elements
    def convolution(self, image, window):
        # to perform convolution, flip the window and compute correlation
        window = np.flipud(np.fliplr(window))
        output = self.correlation(image, window)
        # divide the output with sum of window elements
        output = np.uint8(output / window.sum())
        #  return the computed image
        return output

    # compute correlation operation on image and window passed as ndarray
    # does not normalize output values by dividing with sum of window elements
    def correlation(self, image, window):
        output = np.zeros_like(image)
        # find no of rows and columns in the ndarray of image passed
        image_row = image.shape[0]
        image_column = image.shape[1]

        # compute window size from window passed
        window_size = window.shape[0]
        # compute zero padding requirements and offset to be used during convolution
        zero_padding = window_size - 1
        offset = int(zero_padding / 2)

        # create the zero padded image
        image_zero_padded = \
            np.zeros((image_row + zero_padding, image_column + zero_padding))
        image_zero_padded[offset:(-1 * offset), offset:(-1 * offset)] = image

        # loop through the window elements
        # computes correlation as shifted sum of image elements by keeping
        # window stationary
        for r in range(window_size):
            for c in range(window_size):
                output = output + window[r][c] * \
                         image_zero_padded[r:r + image_row, c:c + image_column]

        #  return the computed image
        return output
 #453  
#main.py
#@@ -0,0 +1,453 @@
# ---------------------------------------------------------------#
# __name__ = "BasicImageEditor_EE610_Assignment"
# __author__ = "Shyama P"
# __version__ = "1.0"
# __email__ = "183079031@iitb.ac.in"
# __status__ = "Development"
# ---------------------------------------------------------------#

# main.py contains the code for initializing and running the code for GUI
import sys
# PyQt5 libraries are used for GUI
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# OpenCV2 library is used for reading/ writing of images and color space
# conversion only
import cv2
# All array operations are performed using numpy library
import numpy as np
# Matplotlib library is used for histogram plots
import  matplotlib.pyplot as plt

# The GUI structure definition is provided in gui.py
from PyQt5 import *   ######################################little chane for pyqt5 here was gui
# Image processing logic is defined in imageProcessingFns.py
from PIL import imageProcessing as ip 

# class ImageEditorClass implements the GUI main window class
class ImageEditorClass(object):

    # stores a copy of original image for use in Undo All functionality
    originalImage = [0]
    # stores the current image being displayed/ processed
    currentImage = [0]
    # stores the previous image for use in Undo operation
    previousImage = [0]

    # stores a copy of image being blurred
    imageBlur = [0]
    # stores a copy of image being sharpened
    imageSharpen = [0]

    # stores current image height and width
    imageWidth = 0
    imageHeight = 0

    # initializes an object of ImageProcessorClass from imageProcessingFns.py
    imageLib = ip.ImageProcessorClass()

    # stores code of current operation
    currentOperationCode = -1

    # ------------------------------#
    # Histogram Equalization => 0   #
    # Gamma Correction => 1         #
    # Log Transform => 2            #
    # Negative => 3                 #
    # Blur => 4                     #
    # Sharpen => 5                  #
    # Edge detection => 6           #
    # ------------------------------#


    # GUI initialization
    def __init__(self, parent=None):
        super(ImageEditorClass, self).__init__()
        object.__init__(self, parent)
        self.ui = ImageEditorGuiClass()
        self.ui.setupUi(self)

        # Assigning functions to be called on all button clicked events and
        # slider value changed events
        self.ui.openImageButton.clicked.connect(lambda: self.open_image())
        self.ui.saveImageButton.clicked.connect(lambda: self.save_image())

        self.ui.histogramEqualizationButton.clicked.connect\
            (lambda: self.histogram_equalization())
        self.ui.logTransformButton.clicked.connect(lambda: self.log_transform())
        self.ui.gammaCorrectionButton.clicked.connect(lambda: self.gamma_correction())
        self.ui.negativeButton.clicked.connect(lambda: self.image_negative())

        self.ui.blurExtendInputSlider.valueChanged.connect(lambda: self.blur())
        self.ui.sharpenExtendInputSlider.valueChanged.connect(lambda: self.sharpen())

        self.ui.undoButton.clicked.connect(lambda: self.undo())
        self.ui.undoAllButton.clicked.connect(lambda: self.undoAll())

        self.ui.viewHistogramButton.clicked.connect(lambda: self.view_histogram())
        self.ui.detectEdgeButton.clicked.connect(lambda: self.edge_detection())

        # initiaize and input dialog box gui for input of gamma value
        self.newDialog = InputDialogGuiClass(self)
    # called when Open button is clicked
    def open_image(self):
        # set_default_slider function resets blur and sharpen sliders to initial
        # position
        self.set_default_slider()

        # open a new Open Image dialog box and capture path of file selected
        from tkinter import tkFileDialog
        open_image_window = tkFileDialog()
        image_path = tkFileDialog.getOpenFileName\
            (open_image_window, 'Open Image', '/')

        # check if image path is not null or empty
        if image_path:
            # initialize class variables
            self.currentImage = [0]
            self.currentOperationCode = -1

            # read image at selected path to a numpy ndarray object as color image
            self.currentImage = cv2.imread(image_path, 1)
            # convert the image read to HSV format from default BGR format
            self.currentImage = cv2.cvtColor(self.currentImage, cv2.COLOR_BGR2HSV)

            # set image specific class variables based on current image
            self.imageWidth = self.currentImage.shape[1]
            self.imageHeight = self.currentImage.shape[0]

            self.originalImage = self.currentImage.copy()
            self.previousImage = self.currentImage.copy()

            # displayImage converts current image from ndarry format to
            # pixmap and assigns it to image display label
            self.displayImage()
            # enable_options enable all buttons and sliders in the window.
            # Only Open button is enabled on start
            self.enable_options()

    # called when Save button is clicked
    def save_image(self):
        # configure the save image dialog box to use .jpg extension for image if
        # not provided in file name
        from tkinter import tkFileDialog
        dialog = tkFileDialog()
        dialog.setDefaultSuffix('jpg')
        dialog.setAcceptMode(tkFileDialog.AcceptSave)

        # open the save dialog box and wait until user clicks 'Save'
        # button in the dialog box
        from tkinter import tkDialog
        if dialog.exec_() == tkDialog.Accepted:
            # select the first path in the selected files list as image save
            # location
            save_image_filename = dialog.selectedFiles()[0]
            # write current image to the file path selected by user
            cv2.imwrite(save_image_filename,
                        cv2.cvtColor(self.currentImage, cv2.COLOR_HSV2BGR))

    # called when Histogram Equalization button is clicked
    def histogram_equalization(self):
        # updatePreviousImage function updates the previous image class variable
        #  with current image
        self.updatePreviousImage()
        # update current operation code class variable
        self.currentOperationCode = 0
        # set_default_slider function resets blur and sharpen sliders to initial
        #  position
        self.set_default_slider()

        # update V channel of the current image with histogram equallized matrix
        self.currentImage[:, :, 2] = self.imageLib.histogram_equalization\
            (self.currentImage[:, :, 2])
        # displayImage converts current image from ndarry format to pixmap
        # and assigns it to image display label
        self.displayImage()

    def gamma_correction(self):
        # updatePreviousImage function updates the previous image class
        # variable with current image
        self.updatePreviousImage()
        # update current operation code class variable
        self.currentOperationCode = 1
        # set_default_slider function resets blur and sharpen sliders to
        # initial position
        self.set_default_slider()

        # open gamma input dialog box and wait for dialog box to exit
        if self.newDialog.exec() == 0:
            # read gamma value from gamma input dialog box class
            gamma_value = self.newDialog.gamma
            # reset the value of gamma in gamma input dialog box to 1
            self.newDialog.gammaInput.setText('1.00')
            self.newDialog.gamma = 1.0
            # perform gamma correction for positive gamma values
            # gamma range is restricted to 0 to 10 in the gamma input
            # dialog box
            if gamma_value > 0:
                # update V channel of the current image with gamma corrected
                # matrix
                self.currentImage[:, :, 2] = self.imageLib.gamma_correction\
                    (self.currentImage[:, :, 2], gamma_value)

        # displayImage converts current image from ndarry format to pixmap
        # and assigns it to image display label
        self.displayImage()

    def log_transform(self):
        # updatePreviousImage function updates the previous image class
        # variable with current image
        self.updatePreviousImage()
        # update current operation code class variable
        self.currentOperationCode = 2
        # set_default_slider function resets blur and sharpen sliders to
        # initial position
        self.set_default_slider()

        # update V channel of the current image with log transformed matrix
        self.currentImage[:, :, 2] = \
            self.imageLib.log_transform(self.currentImage[:, :, 2])

        # displayImage converts current image from ndarry format to
        # pixmap and assigns it to image display label
        self.displayImage()

    def image_negative(self):
        # updatePreviousImage function updates the previous image class
        # variable with current image
        self.updatePreviousImage()
        # update current operation code class variable
        self.currentOperationCode = 3
        # set_default_slider function resets blur and sharpen sliders to
        # initial position
        self.set_default_slider()

        # update current image with negative of current image
        self.currentImage = self.imageLib.image_negative(self.currentImage)

        # displayImage converts current image from ndarry format to pixmap
        # and assigns it to image display label
        self.displayImage()

    def blur(self):
        # updatePreviousImage function updates the previous image class
        # variable with current image
        self.updatePreviousImage()

        # disconnect, initialize and reconnect the sharpen slider value
        # changed event
        # this is to avoid calling of sharpen function when sharpen slider
        # value is reset
        self.ui.sharpenExtendInputSlider.valueChanged.disconnect()
        self.ui.sharpenExtendInputSlider.setValue(0)
        self.ui.sharpenExtendInputSlider.valueChanged.connect(lambda:self.sharpen())
        self.ui.sharpenValueLabel.setText('0')

        # read current blur value from slider and compute blur window size as
        # (2 * slider value + 1)
        blur_value = int(np.floor(self.ui.blurExtendInputSlider.value()))
        blur_window_size = (blur_value * 2) + 1

        # if the operation being performed currently is blur, use initial image
        # passed to blur function
        # else set current image as initial image for blur
        if self.currentOperationCode == 4:
            self.currentImage = self.imageBlur.copy()
        else:
            self.imageBlur = self.currentImage.copy()

        if blur_value > 0:
            # enable undo button
            self.ui.undoButton.setEnabled(True)
            # update V channel of the current image with blurred V matrix
            self.currentImage[:, :, 2] = \
                self.imageLib.blur(self.currentImage[:, :, 2], blur_window_size)

        # update current operation code class variable
        self.currentOperationCode = 4

        self.ui.blurValueLabel.setText(str(blur_value))
        # displayImage converts current image from ndarry format to pixmap and
        # assigns it to image display label
        self.displayImage()

    def sharpen(self):
        # updatePreviousImage function updates the previous image class variable
        # with current image
        self.updatePreviousImage()

        # disconnect, initialize and reconnect the blur slider value changed event
        # this is to avoid calling of blur function when blur slider value is reset
        self.ui.blurExtendInputSlider.valueChanged.disconnect()
        self.ui.blurExtendInputSlider.setValue(0)
        self.ui.blurExtendInputSlider.valueChanged.\
            connect(lambda: self.blur())
        self.ui.blurValueLabel.setText('0')

        # read current sharpen value from slider and compute
        # sharpen constant as (slider value/10)
        sharpen_value = self.ui.sharpenExtendInputSlider.value()
        sharpen_const = sharpen_value / 10.0

        # if the operation being performed currently is sharpen, use
        # initial image passed to sharpen function
        # else set current image as initial image for sharpen
        if self.currentOperationCode == 5:
            self.currentImage = self.imageSharpen.copy()
        else:
            self.imageSharpen = self.currentImage.copy()

        if sharpen_const > 0:
            # enable undo button
            self.ui.undoButton.setEnabled(True)
            # update V channel of the current image with sharpened V
            # channel matrix
            self.currentImage[:, :, 2] = \
                np.uint8(self.imageLib.sharp(self.currentImage[:, :, 2], sharpen_const))

        # update current operation code class variable
        self.currentOperationCode = 5

        self.ui.sharpenValueLabel.setText(str(sharpen_value))
        # displayImage converts current image from ndarry format to
        # pixmap and assigns it to image display label
        self.displayImage()

    def undo(self):
        self.ui.undoButton.setEnabled(False)
        self.currentImage = self.previousImage.copy()
        # displayImage converts current image from ndarry format to pixmap and
        # assigns it to image display label
        self.displayImage()

    def undoAll(self):
        # set_default_slider function resets blur and sharpen sliders to initial
        # position
        self.set_default_slider()
        self.currentImage = self.originalImage.copy()
        # displayImage converts current image from ndarry format to pixmap and
        # assigns it to image display label
        self.displayImage()
        self.ui.undoButton.setEnabled(False)

    def view_histogram(self):
        # count the no of values corresponding to each value in the V channel of
        # image matrix give a minimum length of 256 to the counting to ensure all 256 pixel
        # values are covered or pixel values not available in image are set to zero
        histogram = np.bincount(self.currentImage[:, :, 2].ravel(), minlength=256)
        # start a new figure to show histogram - assign title and axes label
        plt.figure(num='Image Histogram')
        # assign a discrete plot of histogram to figure
        plt.stem(histogram)
        plt.xlabel('Intensity levels')
        plt.ylabel('No. of pixels')
        # show the stem plot
        plt.show()

    def edge_detection(self):
        # updatePreviousImage function updates the previous image class variable with
        # current image
        self.updatePreviousImage()
        # update current operation code class variable
        self.currentOperationCode = 6
        # set_default_slider function resets blur and sharpen sliders to initial
        # position
        self.set_default_slider()

        # update V channel of the current image with edge detected V channel matrix
        self.currentImage[:, :, 2] \
            = self.imageLib.edge_detection(self.currentImage[:, :, 2])

        # displayImage converts current image from ndarry format to
        # pixmap and assigns it to image display label
        self.displayImage()

    # displayImage converts current image from ndarry format to pixmap and
    # assigns it to image display label
    def displayImage(self):
        # set display size to size of the image display label
        display_size = self.ui.imageDisplayLabel.size()
        # copy current image to temporary variable for processing pixmap
        image = np.array(self.currentImage.copy())
        zero = np.array([0])

        # display image if image is not [0] array
        if not np.array_equal(image, zero):
            # convert HSV image to RGB format for display in label
            image = cv2.cvtColor(image, cv2.COLOR_HSV2RGB)
            # ndarray cannot be directly converted to QPixmap format required
            # by image display label
            # so ndarray is first converted to QImage and then QImage to QPixmap
            # convert image ndarray to QImage format
            qImage = QImage(image, self.imageWidth, self.imageHeight,
                            self.imageWidth * 3, QImage.Format_RGB888)

            # convert QImage to QPixmap for loading in image display label
            pixmap = QPixmap()
            QPixmap.convertFromImage(pixmap, qImage)
            pixmap = pixmap.scaled(display_size, Qt.KeepAspectRatio,Qt.SmoothTransformation)
            # set pixmap to image display label in GUI
            self.ui.imageDisplayLabel.setPixmap(pixmap)

    # enable_options enable all buttons and sliders in the window. Only
    # Open button is enabled on start
    # Undo button remains disabled until an operation is performed
    def enable_options(self):
        self.ui.histogramEqualizationButton.setEnabled(True)
        self.ui.gammaCorrectionButton.setEnabled(True)
        self.ui.logTransformButton.setEnabled(True)
        self.ui.negativeButton.setEnabled(True)

        self.ui.blurExtendInputSlider.setEnabled(True)
        self.ui.sharpenExtendInputSlider.setEnabled(True)

        self.ui.saveImageButton.setEnabled(True)
        self.ui.undoAllButton.setEnabled(True)
        self.ui.undoButton.setEnabled(False)

        self.ui.viewHistogramButton.setEnabled(True)
        self.ui.detectEdgeButton.setEnabled(True)

    # set_default_slider function resets blur and sharpen sliders to initial
    # position
    def set_default_slider(self):
        # disconnect the value changed event of sliders from the functions
        # assigned this prevents calling the blur and sharpen function on
        # resetting of sliders
        self.ui.sharpenExtendInputSlider.valueChanged.disconnect()
        self.ui.blurExtendInputSlider.valueChanged.disconnect()

        # update slider values to initial position i.e. 0
        # update slider value labels to 0
        self.ui.blurExtendInputSlider.setValue(0)
        self.ui.blurValueLabel.setText('0')
        self.ui.sharpenExtendInputSlider.setValue(0)
        self.ui.sharpenValueLabel.setText('0')

        # reconnect the value changed event of sliders to blur and sharpen
        # functions
        self.ui.blurExtendInputSlider.valueChanged.connect(lambda: self.blur())
        self.ui.sharpenExtendInputSlider.valueChanged.connect(lambda: self.sharpen())

        # reset values of blur and sharpen image class variables
        self.imageBlur = [0]
        self.imageSharpen = [0]

        # enable Undo button only if an operation was performed previosly
        # i.e. current operation code is a valid code
        if (self.currentOperationCode >= 0) and \
            not self.ui.undoButton.isEnabled():self.ui.undoButton.setEnabled(True)

    # updatePreviousImage function updates the previous image class variable
    # with current image
    def updatePreviousImage(self):
        self.previousImage = self.currentImage.copy()

        # initialize the ImageEditorClass and run the application
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = ImageEditorClass()
    myapp.showMaximized()
    sys.exit(app.exec_())
