
# Class defining all GUI elements for Gamma input window
class InputDialogGuiClass(QtGui.QDialog):

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