# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(516, 359)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.gen_button = QtWidgets.QPushButton(self.centralwidget)
        self.gen_button.setGeometry(QtCore.QRect(170, 160, 91, 41))
        self.gen_button.setObjectName("gen_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(main)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(main)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(main)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "MainWindow"))
        self.gen_button.setText(_translate("main", "GENERATE"))
        self.label.setText(_translate("main", "Not generated yet"))
        self.menuFile.setTitle(_translate("main", "File"))
        self.actionLoad.setText(_translate("main", "Load"))
        self.actionSave.setText(_translate("main", "Save"))
        self.actionNew.setText(_translate("main", "New"))