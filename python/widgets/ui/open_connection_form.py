# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open_connection_form.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_OpenConnectionForm(object):
    def setupUi(self, OpenConnectionForm):
        OpenConnectionForm.setObjectName("OpenConnectionForm")
        OpenConnectionForm.resize(461, 238)
        self.verticalLayout = QtGui.QVBoxLayout(OpenConnectionForm)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtGui.QLabel(OpenConnectionForm)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_8 = QtGui.QLabel(OpenConnectionForm)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.server_label = QtGui.QLabel(OpenConnectionForm)
        self.server_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.server_label.setObjectName("server_label")
        self.gridLayout_4.addWidget(self.server_label, 0, 1, 1, 1)
        self.label_9 = QtGui.QLabel(OpenConnectionForm)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)
        self.user_label = QtGui.QLabel(OpenConnectionForm)
        self.user_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.user_label.setObjectName("user_label")
        self.gridLayout_4.addWidget(self.user_label, 1, 1, 1, 1)
        self.gridLayout_4.setColumnMinimumWidth(0, 80)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        spacerItem = QtGui.QSpacerItem(1, 12, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_12 = QtGui.QLabel(OpenConnectionForm)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.workspace_edit = QtGui.QLineEdit(OpenConnectionForm)
        self.workspace_edit.setObjectName("workspace_edit")
        self.gridLayout_3.addWidget(self.workspace_edit, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(OpenConnectionForm)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.workspace_browse_btn = QtGui.QPushButton(OpenConnectionForm)
        self.workspace_browse_btn.setObjectName("workspace_browse_btn")
        self.gridLayout_3.addWidget(self.workspace_browse_btn, 0, 2, 1, 1)
        self.gridLayout_3.setColumnMinimumWidth(0, 80)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.break_line = QtGui.QFrame(OpenConnectionForm)
        self.break_line.setFrameShape(QtGui.QFrame.HLine)
        self.break_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.break_line.setObjectName("break_line")
        self.verticalLayout.addWidget(self.break_line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(12, 8, 12, 12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.cancel_btn = QtGui.QPushButton(OpenConnectionForm)
        self.cancel_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        self.ok_btn = QtGui.QPushButton(OpenConnectionForm)
        self.ok_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.ok_btn.setDefault(True)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout_3.addWidget(self.ok_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(OpenConnectionForm)
        QtCore.QMetaObject.connectSlotsByName(OpenConnectionForm)
        OpenConnectionForm.setTabOrder(self.cancel_btn, self.ok_btn)

    def retranslateUi(self, OpenConnectionForm):
        OpenConnectionForm.setWindowTitle(QtGui.QApplication.translate("OpenConnectionForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("OpenConnectionForm", "<html><head/><body><p><span style=\" font-size:large;\">Your Perforce connection settings are:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("OpenConnectionForm", "Server:", None, QtGui.QApplication.UnicodeUTF8))
        self.server_label.setText(QtGui.QApplication.translate("OpenConnectionForm", "[server]:[port]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("OpenConnectionForm", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.user_label.setText(QtGui.QApplication.translate("OpenConnectionForm", "[user]", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("OpenConnectionForm", "<html><head/><body><p><span style=\" font-size:large;\">Choose the Workspace to use for this connection:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("OpenConnectionForm", "Workspace:", None, QtGui.QApplication.UnicodeUTF8))
        self.workspace_browse_btn.setText(QtGui.QApplication.translate("OpenConnectionForm", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("OpenConnectionForm", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("OpenConnectionForm", "Connect", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
