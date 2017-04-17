# -*- coding: utf-8 -*-

# Form implementation fot 'title_options.ui'
# Manually created by copy paste and editing the label_options.ui

from PyQt4 import QtCore, QtGui

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

class Ui_titleOptions(object):
    def setupUi(self, titleOptions):
        titleOptions.setObjectName(_fromUtf8("titleOptions"))
        titleOptions.resize(239, 272)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(titleOptions.sizePolicy().hasHeightForWidth())
        titleOptions.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(titleOptions)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(titleOptions)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.titleEdit = QtGui.QLineEdit(titleOptions)
        self.titleEdit.setObjectName(_fromUtf8("titleEdit"))
        self.verticalLayout_2.addWidget(self.titleEdit)
        
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_5 = QtGui.QLabel(titleOptions)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.placement = QtGui.QComboBox(titleOptions)
        self.placement.setObjectName(_fromUtf8("placement"))
        self.horizontalLayout.addWidget(self.placement)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(titleOptions)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.fontsize = QtGui.QSpinBox(titleOptions)
        self.fontsize.setObjectName(_fromUtf8("fontsize"))
        self.horizontalLayout_5.addWidget(self.fontsize)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(titleOptions)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.font = QtGui.QFontComboBox(titleOptions)
        self.font.setObjectName(_fromUtf8("font"))
        self.horizontalLayout_4.addWidget(self.font)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_6 = QtGui.QLabel(titleOptions)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.text_color = gui.QgsColorButton(titleOptions)
        self.text_color.setObjectName(_fromUtf8("text_color"))
        self.horizontalLayout_3.addWidget(self.text_color)
        self.label_7 = QtGui.QLabel(titleOptions)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.bg_color = gui.QgsColorButton(titleOptions)
        self.bg_color.setObjectName(_fromUtf8("bg_color"))
        self.horizontalLayout_3.addWidget(self.bg_color)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        
        self.verticalLayout.addLayout(self.verticalLayout_2)
        
        self.label_4 = QtGui.QLabel(titleOptions)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.buttonBox = QtGui.QDialogButtonBox(titleOptions)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(titleOptions)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), titleOptions.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), titleOptions.reject)
        QtCore.QMetaObject.connectSlotsByName(titleOptions)

    def retranslateUi(self, titleOptions):
        titleOptions.setWindowTitle(_translate("titleOptions", "Options", None))
        self.label_3.setText(_translate("titleOptions", "Title", None))
        self.titleEdit.setText(_translate("titleOptions", "", None))
        self.label.setText(_translate("titleOptions", "Font:", None))
        self.label_2.setText(_translate("titleOptions", "Font Size:", None))
        self.label_5.setText(_translate("titleOptions", "Placement Direction:", None))
        self.label_6.setText(_translate("titleOptions", "Text Color:", None))
        self.label_7.setText(_translate("titleOptions", "Bg Color:", None))

from qgis import gui

