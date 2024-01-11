# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 720))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 50, 1781, 601))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(300, 100))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/proteck.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cycleStartButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cycleStartButton.setMinimumSize(QtCore.QSize(120, 120))
        self.cycleStartButton.setMaximumSize(QtCore.QSize(120, 120))
        self.cycleStartButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/off/cyclestart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("images/on/cyclestart.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("images/disabled/cyclestart.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.cycleStartButton.setIcon(icon)
        self.cycleStartButton.setIconSize(QtCore.QSize(120, 120))
        self.cycleStartButton.setCheckable(False)
        self.cycleStartButton.setFlat(True)
        self.cycleStartButton.setObjectName("cycleStartButton")
        self.horizontalLayout_3.addWidget(self.cycleStartButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.cycleStopButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cycleStopButton.setMinimumSize(QtCore.QSize(120, 120))
        self.cycleStopButton.setMaximumSize(QtCore.QSize(120, 120))
        self.cycleStopButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/off/cyclestop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("images/on/cyclestop.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("images/disabled/cyclestop.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.cycleStopButton.setIcon(icon1)
        self.cycleStopButton.setIconSize(QtCore.QSize(120, 120))
        self.cycleStopButton.setCheckable(False)
        self.cycleStopButton.setFlat(True)
        self.cycleStopButton.setObjectName("cycleStopButton")
        self.horizontalLayout_3.addWidget(self.cycleStopButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.xButton = QtWidgets.QPushButton(self.layoutWidget)
        self.xButton.setMinimumSize(QtCore.QSize(120, 120))
        self.xButton.setMaximumSize(QtCore.QSize(120, 120))
        self.xButton.setAutoFillBackground(False)
        self.xButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/off/x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("images/on/x.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap("images/disabled/x.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.xButton.setIcon(icon2)
        self.xButton.setIconSize(QtCore.QSize(120, 120))
        self.xButton.setCheckable(True)
        self.xButton.setChecked(False)
        self.xButton.setFlat(True)
        self.xButton.setObjectName("xButton")
        self.gridLayout_2.addWidget(self.xButton, 4, 0, 1, 1)
        self.mdiButton = QtWidgets.QPushButton(self.layoutWidget)
        self.mdiButton.setMinimumSize(QtCore.QSize(120, 120))
        self.mdiButton.setMaximumSize(QtCore.QSize(120, 120))
        self.mdiButton.setAutoFillBackground(False)
        self.mdiButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/off/mdi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("images/on/mdi.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon3.addPixmap(QtGui.QPixmap("images/disabled/mdi.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.mdiButton.setIcon(icon3)
        self.mdiButton.setIconSize(QtCore.QSize(120, 120))
        self.mdiButton.setCheckable(True)
        self.mdiButton.setChecked(False)
        self.mdiButton.setFlat(True)
        self.mdiButton.setObjectName("mdiButton")
        self.gridLayout_2.addWidget(self.mdiButton, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 3, 0, 1, 1)
        self.jogButton = QtWidgets.QPushButton(self.layoutWidget)
        self.jogButton.setMinimumSize(QtCore.QSize(120, 120))
        self.jogButton.setMaximumSize(QtCore.QSize(120, 120))
        self.jogButton.setAutoFillBackground(False)
        self.jogButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/off/jog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("images/on/jog.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap("images/disabled/dryrun.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.jogButton.setIcon(icon4)
        self.jogButton.setIconSize(QtCore.QSize(120, 120))
        self.jogButton.setCheckable(True)
        self.jogButton.setChecked(False)
        self.jogButton.setFlat(True)
        self.jogButton.setObjectName("jogButton")
        self.gridLayout_2.addWidget(self.jogButton, 2, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 5, 0, 1, 1)
        self.autoButton = QtWidgets.QPushButton(self.layoutWidget)
        self.autoButton.setMinimumSize(QtCore.QSize(120, 120))
        self.autoButton.setMaximumSize(QtCore.QSize(120, 120))
        self.autoButton.setAutoFillBackground(False)
        self.autoButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/off/auto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("images/on/auto.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon5.addPixmap(QtGui.QPixmap("images/disabled/auto.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.autoButton.setIcon(icon5)
        self.autoButton.setIconSize(QtCore.QSize(120, 120))
        self.autoButton.setCheckable(True)
        self.autoButton.setChecked(False)
        self.autoButton.setFlat(True)
        self.autoButton.setObjectName("autoButton")
        self.gridLayout_2.addWidget(self.autoButton, 2, 4, 1, 1)
        self.plusButton = QtWidgets.QPushButton(self.layoutWidget)
        self.plusButton.setMinimumSize(QtCore.QSize(120, 120))
        self.plusButton.setMaximumSize(QtCore.QSize(120, 120))
        self.plusButton.setAutoFillBackground(False)
        self.plusButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/off/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap("images/on/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon6.addPixmap(QtGui.QPixmap("images/disabled/plus.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.plusButton.setIcon(icon6)
        self.plusButton.setIconSize(QtCore.QSize(120, 120))
        self.plusButton.setCheckable(False)
        self.plusButton.setChecked(False)
        self.plusButton.setFlat(True)
        self.plusButton.setObjectName("plusButton")
        self.gridLayout_2.addWidget(self.plusButton, 6, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 0, 3, 1, 1)
        self.dryRunButton = QtWidgets.QPushButton(self.layoutWidget)
        self.dryRunButton.setMinimumSize(QtCore.QSize(120, 120))
        self.dryRunButton.setMaximumSize(QtCore.QSize(120, 120))
        self.dryRunButton.setAutoFillBackground(False)
        self.dryRunButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/off/dryrun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("images/on/dryrun.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon7.addPixmap(QtGui.QPixmap("images/disabled/dryrun.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.dryRunButton.setIcon(icon7)
        self.dryRunButton.setIconSize(QtCore.QSize(120, 120))
        self.dryRunButton.setCheckable(True)
        self.dryRunButton.setChecked(False)
        self.dryRunButton.setFlat(True)
        self.dryRunButton.setObjectName("dryRunButton")
        self.gridLayout_2.addWidget(self.dryRunButton, 0, 4, 1, 1)
        self.zButton = QtWidgets.QPushButton(self.layoutWidget)
        self.zButton.setMinimumSize(QtCore.QSize(120, 120))
        self.zButton.setMaximumSize(QtCore.QSize(120, 120))
        self.zButton.setAutoFillBackground(False)
        self.zButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/off/z.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap("images/on/z.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon8.addPixmap(QtGui.QPixmap("images/disabled/z.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.zButton.setIcon(icon8)
        self.zButton.setIconSize(QtCore.QSize(120, 120))
        self.zButton.setCheckable(True)
        self.zButton.setChecked(False)
        self.zButton.setFlat(True)
        self.zButton.setObjectName("zButton")
        self.gridLayout_2.addWidget(self.zButton, 4, 4, 1, 1)
        self.minusButton = QtWidgets.QPushButton(self.layoutWidget)
        self.minusButton.setMinimumSize(QtCore.QSize(120, 120))
        self.minusButton.setMaximumSize(QtCore.QSize(120, 120))
        self.minusButton.setAutoFillBackground(False)
        self.minusButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/off/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap("images/on/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon9.addPixmap(QtGui.QPixmap("images/disabled/minus.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.minusButton.setIcon(icon9)
        self.minusButton.setIconSize(QtCore.QSize(120, 120))
        self.minusButton.setCheckable(False)
        self.minusButton.setChecked(False)
        self.minusButton.setFlat(True)
        self.minusButton.setObjectName("minusButton")
        self.gridLayout_2.addWidget(self.minusButton, 6, 4, 1, 1)
        self.vvvButton = QtWidgets.QPushButton(self.layoutWidget)
        self.vvvButton.setMinimumSize(QtCore.QSize(120, 120))
        self.vvvButton.setMaximumSize(QtCore.QSize(120, 120))
        self.vvvButton.setAutoFillBackground(False)
        self.vvvButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/off/vvv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap("images/on/vvv.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon10.addPixmap(QtGui.QPixmap("images/disabled/vvv.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.vvvButton.setIcon(icon10)
        self.vvvButton.setIconSize(QtCore.QSize(120, 120))
        self.vvvButton.setCheckable(True)
        self.vvvButton.setChecked(False)
        self.vvvButton.setFlat(True)
        self.vvvButton.setObjectName("vvvButton")
        self.gridLayout_2.addWidget(self.vvvButton, 6, 2, 1, 1)
        self.yButton = QtWidgets.QPushButton(self.layoutWidget)
        self.yButton.setMinimumSize(QtCore.QSize(120, 120))
        self.yButton.setMaximumSize(QtCore.QSize(120, 120))
        self.yButton.setAutoFillBackground(False)
        self.yButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images/off/y.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap("images/on/y.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon11.addPixmap(QtGui.QPixmap("images/disabled/y.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.yButton.setIcon(icon11)
        self.yButton.setIconSize(QtCore.QSize(120, 120))
        self.yButton.setCheckable(True)
        self.yButton.setChecked(False)
        self.yButton.setFlat(True)
        self.yButton.setObjectName("yButton")
        self.gridLayout_2.addWidget(self.yButton, 4, 2, 1, 1)
        self.zLockButton = QtWidgets.QPushButton(self.layoutWidget)
        self.zLockButton.setMinimumSize(QtCore.QSize(120, 120))
        self.zLockButton.setMaximumSize(QtCore.QSize(120, 120))
        self.zLockButton.setAutoFillBackground(False)
        self.zLockButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("images/off/zlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon12.addPixmap(QtGui.QPixmap("images/on/zlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon12.addPixmap(QtGui.QPixmap("images/disabled/zlock.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.zLockButton.setIcon(icon12)
        self.zLockButton.setIconSize(QtCore.QSize(120, 120))
        self.zLockButton.setCheckable(True)
        self.zLockButton.setChecked(False)
        self.zLockButton.setFlat(True)
        self.zLockButton.setObjectName("zLockButton")
        self.gridLayout_2.addWidget(self.zLockButton, 0, 2, 1, 1)
        self.drvButton = QtWidgets.QPushButton(self.layoutWidget)
        self.drvButton.setMinimumSize(QtCore.QSize(120, 120))
        self.drvButton.setMaximumSize(QtCore.QSize(120, 120))
        self.drvButton.setAutoFillBackground(False)
        self.drvButton.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("images/off/drv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon13.addPixmap(QtGui.QPixmap("images/on/drv.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon13.addPixmap(QtGui.QPixmap("images/disabled/drv.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.drvButton.setIcon(icon13)
        self.drvButton.setIconSize(QtCore.QSize(120, 120))
        self.drvButton.setCheckable(True)
        self.drvButton.setChecked(False)
        self.drvButton.setFlat(True)
        self.drvButton.setObjectName("drvButton")
        self.gridLayout_2.addWidget(self.drvButton, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ncRefButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ncRefButton.setMinimumSize(QtCore.QSize(120, 120))
        self.ncRefButton.setMaximumSize(QtCore.QSize(120, 120))
        self.ncRefButton.setAutoFillBackground(False)
        self.ncRefButton.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("images/off/ncref.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon14.addPixmap(QtGui.QPixmap("images/on/ncref.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon14.addPixmap(QtGui.QPixmap("images/disabled/ncref.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.ncRefButton.setIcon(icon14)
        self.ncRefButton.setIconSize(QtCore.QSize(120, 120))
        self.ncRefButton.setCheckable(True)
        self.ncRefButton.setChecked(False)
        self.ncRefButton.setFlat(True)
        self.ncRefButton.setObjectName("ncRefButton")
        self.gridLayout_3.addWidget(self.ncRefButton, 0, 0, 1, 1)
        self.ncOffsetButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ncOffsetButton.setMinimumSize(QtCore.QSize(120, 120))
        self.ncOffsetButton.setMaximumSize(QtCore.QSize(120, 120))
        self.ncOffsetButton.setAutoFillBackground(False)
        self.ncOffsetButton.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("images/off/ncoffset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon15.addPixmap(QtGui.QPixmap("images/on/ncoffset.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon15.addPixmap(QtGui.QPixmap("images/disabled/ncoffset.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.ncOffsetButton.setIcon(icon15)
        self.ncOffsetButton.setIconSize(QtCore.QSize(120, 120))
        self.ncOffsetButton.setCheckable(True)
        self.ncOffsetButton.setChecked(False)
        self.ncOffsetButton.setFlat(True)
        self.ncOffsetButton.setObjectName("ncOffsetButton")
        self.gridLayout_3.addWidget(self.ncOffsetButton, 2, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem12, 3, 0, 1, 1)
        self.retRevButton = QtWidgets.QPushButton(self.layoutWidget)
        self.retRevButton.setMinimumSize(QtCore.QSize(120, 120))
        self.retRevButton.setMaximumSize(QtCore.QSize(120, 120))
        self.retRevButton.setAutoFillBackground(False)
        self.retRevButton.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("images/off/retrev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon16.addPixmap(QtGui.QPixmap("images/on/retrev.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon16.addPixmap(QtGui.QPixmap("images/disabled/retrev.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.retRevButton.setIcon(icon16)
        self.retRevButton.setIconSize(QtCore.QSize(120, 120))
        self.retRevButton.setCheckable(False)
        self.retRevButton.setChecked(False)
        self.retRevButton.setFlat(True)
        self.retRevButton.setObjectName("retRevButton")
        self.gridLayout_3.addWidget(self.retRevButton, 6, 0, 1, 1)
        self.retForButton = QtWidgets.QPushButton(self.layoutWidget)
        self.retForButton.setMinimumSize(QtCore.QSize(120, 120))
        self.retForButton.setMaximumSize(QtCore.QSize(120, 120))
        self.retForButton.setAutoFillBackground(False)
        self.retForButton.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("images/off/retfor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon17.addPixmap(QtGui.QPixmap("images/on/retfor.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon17.addPixmap(QtGui.QPixmap("images/disabled/retfor.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.retForButton.setIcon(icon17)
        self.retForButton.setIconSize(QtCore.QSize(120, 120))
        self.retForButton.setCheckable(False)
        self.retForButton.setChecked(False)
        self.retForButton.setFlat(True)
        self.retForButton.setObjectName("retForButton")
        self.gridLayout_3.addWidget(self.retForButton, 4, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem13, 5, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem14, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem15)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem16)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem17, 5, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem18, 3, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem19, 1, 0, 1, 1)
        self.lockRstButton = QtWidgets.QPushButton(self.layoutWidget)
        self.lockRstButton.setMinimumSize(QtCore.QSize(120, 120))
        self.lockRstButton.setMaximumSize(QtCore.QSize(120, 120))
        self.lockRstButton.setAutoFillBackground(False)
        self.lockRstButton.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("images/off/lockrst.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon18.addPixmap(QtGui.QPixmap("images/on/lockrst.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon18.addPixmap(QtGui.QPixmap("images/disabled/lockrst.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.lockRstButton.setIcon(icon18)
        self.lockRstButton.setIconSize(QtCore.QSize(120, 120))
        self.lockRstButton.setCheckable(False)
        self.lockRstButton.setChecked(False)
        self.lockRstButton.setFlat(True)
        self.lockRstButton.setObjectName("lockRstButton")
        self.gridLayout_4.addWidget(self.lockRstButton, 6, 0, 1, 1)
        self.almOvrButton = QtWidgets.QPushButton(self.layoutWidget)
        self.almOvrButton.setMinimumSize(QtCore.QSize(120, 120))
        self.almOvrButton.setMaximumSize(QtCore.QSize(120, 120))
        self.almOvrButton.setAutoFillBackground(False)
        self.almOvrButton.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("images/off/almovr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon19.addPixmap(QtGui.QPixmap("images/on/almovr.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon19.addPixmap(QtGui.QPixmap("images/disabled/almovr.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.almOvrButton.setIcon(icon19)
        self.almOvrButton.setIconSize(QtCore.QSize(120, 120))
        self.almOvrButton.setCheckable(False)
        self.almOvrButton.setChecked(False)
        self.almOvrButton.setFlat(True)
        self.almOvrButton.setObjectName("almOvrButton")
        self.gridLayout_4.addWidget(self.almOvrButton, 2, 0, 1, 1)
        self.prcEndButton = QtWidgets.QPushButton(self.layoutWidget)
        self.prcEndButton.setMinimumSize(QtCore.QSize(120, 120))
        self.prcEndButton.setMaximumSize(QtCore.QSize(120, 120))
        self.prcEndButton.setAutoFillBackground(False)
        self.prcEndButton.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("images/off/prcend.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon20.addPixmap(QtGui.QPixmap("images/on/prcend.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon20.addPixmap(QtGui.QPixmap("images/disabled/prcend.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.prcEndButton.setIcon(icon20)
        self.prcEndButton.setIconSize(QtCore.QSize(120, 120))
        self.prcEndButton.setCheckable(False)
        self.prcEndButton.setChecked(False)
        self.prcEndButton.setFlat(True)
        self.prcEndButton.setObjectName("prcEndButton")
        self.gridLayout_4.addWidget(self.prcEndButton, 0, 0, 1, 1)
        self.almRstButton = QtWidgets.QPushButton(self.layoutWidget)
        self.almRstButton.setMinimumSize(QtCore.QSize(120, 120))
        self.almRstButton.setMaximumSize(QtCore.QSize(120, 120))
        self.almRstButton.setAutoFillBackground(False)
        self.almRstButton.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("images/off/almrst.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon21.addPixmap(QtGui.QPixmap("images/on/almrst.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon21.addPixmap(QtGui.QPixmap("images/disabled/almrst.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.almRstButton.setIcon(icon21)
        self.almRstButton.setIconSize(QtCore.QSize(120, 120))
        self.almRstButton.setCheckable(False)
        self.almRstButton.setChecked(False)
        self.almRstButton.setFlat(True)
        self.almRstButton.setObjectName("almRstButton")
        self.gridLayout_4.addWidget(self.almRstButton, 4, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem20)
        self.line_4 = QtWidgets.QFrame(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.line_4.setFont(font)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem21)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.laserOnButton = QtWidgets.QPushButton(self.layoutWidget)
        self.laserOnButton.setMinimumSize(QtCore.QSize(130, 130))
        self.laserOnButton.setMaximumSize(QtCore.QSize(130, 130))
        self.laserOnButton.setAutoFillBackground(False)
        self.laserOnButton.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("images/off/laseron.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon22.addPixmap(QtGui.QPixmap("images/on/laseron.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon22.addPixmap(QtGui.QPixmap("images/disabled/laseron.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.laserOnButton.setIcon(icon22)
        self.laserOnButton.setIconSize(QtCore.QSize(130, 130))
        self.laserOnButton.setCheckable(True)
        self.laserOnButton.setChecked(False)
        self.laserOnButton.setFlat(True)
        self.laserOnButton.setObjectName("laserOnButton")
        self.gridLayout_5.addWidget(self.laserOnButton, 1, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem22, 4, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem23, 0, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem24, 2, 0, 1, 1)
        self.laserReadyLamp = QtWidgets.QLabel(self.layoutWidget)
        self.laserReadyLamp.setMinimumSize(QtCore.QSize(130, 130))
        self.laserReadyLamp.setMaximumSize(QtCore.QSize(130, 130))
        self.laserReadyLamp.setText("")
        self.laserReadyLamp.setPixmap(QtGui.QPixmap("images/laserready_off.png"))
        self.laserReadyLamp.setAlignment(QtCore.Qt.AlignCenter)
        self.laserReadyLamp.setObjectName("laserReadyLamp")
        self.gridLayout_5.addWidget(self.laserReadyLamp, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_5)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem25)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Machine Control Panel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
