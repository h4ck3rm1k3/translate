# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unknown'
#
# Created: Tue Jan 23 15:27:09 2007
#      by: PyQt4 UI code generator 4.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_frmHeader(object):
    def setupUi(self, frmHeader):
        frmHeader.setObjectName("frmHeader")
        frmHeader.resize(QtCore.QSize(QtCore.QRect(0,0,443,587).size()).expandedTo(frmHeader.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmHeader.sizePolicy().hasHeightForWidth())
        frmHeader.setSizePolicy(sizePolicy)
        frmHeader.setSizeGripEnabled(True)
        frmHeader.setModal(True)

        self.gridlayout = QtGui.QGridLayout(frmHeader)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.frame = QtGui.QFrame(frmHeader)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.gridlayout1 = QtGui.QGridLayout(self.frame)
        self.gridlayout1.setMargin(9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        spacerItem = QtGui.QSpacerItem(20,141,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem,2,1,1,1)

        self.btnDown = QtGui.QPushButton(self.frame)
        self.btnDown.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDown.sizePolicy().hasHeightForWidth())
        self.btnDown.setSizePolicy(sizePolicy)
        self.btnDown.setIcon(QtGui.QIcon("../images/down.png"))
        self.btnDown.setObjectName("btnDown")
        self.gridlayout1.addWidget(self.btnDown,1,1,1,1)

        self.btnUp = QtGui.QPushButton(self.frame)
        self.btnUp.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUp.sizePolicy().hasHeightForWidth())
        self.btnUp.setSizePolicy(sizePolicy)
        self.btnUp.setIcon(QtGui.QIcon("../images/up.png"))
        self.btnUp.setObjectName("btnUp")
        self.gridlayout1.addWidget(self.btnUp,0,1,1,1)

        self.btnInsertRow = QtGui.QPushButton(self.frame)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnInsertRow.sizePolicy().hasHeightForWidth())
        self.btnInsertRow.setSizePolicy(sizePolicy)

        font = QtGui.QFont(self.btnInsertRow.font())
        font.setFamily("Sans Serif")
        font.setPointSize(15)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.btnInsertRow.setFont(font)
        self.btnInsertRow.setIcon(QtGui.QIcon("../images/new.png"))
        self.btnInsertRow.setObjectName("btnInsertRow")
        self.gridlayout1.addWidget(self.btnInsertRow,3,1,1,1)

        self.btnDeleteRow = QtGui.QPushButton(self.frame)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDeleteRow.sizePolicy().hasHeightForWidth())
        self.btnDeleteRow.setSizePolicy(sizePolicy)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(0),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(1),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(2),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(3),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(4),QtGui.QColor(85,85,85))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(5),QtGui.QColor(199,199,199))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(6),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(7),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(8),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(9),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(10),QtGui.QColor(239,239,239))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(11),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(12),QtGui.QColor(103,141,178))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(13),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(14),QtGui.QColor(0,0,238))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(15),QtGui.QColor(82,24,139))
        palette.setColor(QtGui.QPalette.Active,QtGui.QPalette.ColorRole(16),QtGui.QColor(232,232,232))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(0),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(1),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(2),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(3),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(4),QtGui.QColor(85,85,85))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(5),QtGui.QColor(199,199,199))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(6),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(7),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(8),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(9),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(10),QtGui.QColor(239,239,239))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(11),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(12),QtGui.QColor(103,141,178))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(13),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(14),QtGui.QColor(0,0,238))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(15),QtGui.QColor(82,24,139))
        palette.setColor(QtGui.QPalette.Inactive,QtGui.QPalette.ColorRole(16),QtGui.QColor(232,232,232))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(0),QtGui.QColor(128,128,128))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(1),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(2),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(3),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(4),QtGui.QColor(85,85,85))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(5),QtGui.QColor(199,199,199))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(6),QtGui.QColor(199,199,199))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(7),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(8),QtGui.QColor(128,128,128))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(9),QtGui.QColor(239,239,239))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(10),QtGui.QColor(239,239,239))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(11),QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(12),QtGui.QColor(86,117,148))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(13),QtGui.QColor(255,255,255))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(14),QtGui.QColor(0,0,238))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(15),QtGui.QColor(82,24,139))
        palette.setColor(QtGui.QPalette.Disabled,QtGui.QPalette.ColorRole(16),QtGui.QColor(232,232,232))
        self.btnDeleteRow.setPalette(palette)

        font = QtGui.QFont(self.btnDeleteRow.font())
        font.setFamily("Sans Serif")
        font.setPointSize(15)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.btnDeleteRow.setFont(font)
        self.btnDeleteRow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnDeleteRow.setIcon(QtGui.QIcon("../images/stop.png"))
        self.btnDeleteRow.setObjectName("btnDeleteRow")
        self.gridlayout1.addWidget(self.btnDeleteRow,4,1,1,1)

        self.tableHeader = QtGui.QTableWidget(self.frame)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(7))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableHeader.sizePolicy().hasHeightForWidth())
        self.tableHeader.setSizePolicy(sizePolicy)
        self.tableHeader.setMouseTracking(False)
        self.tableHeader.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tableHeader.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableHeader.setAcceptDrops(False)
        self.tableHeader.setLineWidth(1)
        self.tableHeader.setMidLineWidth(1)
        self.tableHeader.setProperty("showDropIndicator",QtCore.QVariant(False))
        self.tableHeader.setDragEnabled(False)
        self.tableHeader.setAlternatingRowColors(True)
        self.tableHeader.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableHeader.setShowGrid(True)
        self.tableHeader.setObjectName("tableHeader")
        self.gridlayout1.addWidget(self.tableHeader,0,0,5,1)
        self.gridlayout.addWidget(self.frame,3,0,1,1)

        self.txtOtherComments = QtGui.QTextEdit(frmHeader)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(7),QtGui.QSizePolicy.Policy(3))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOtherComments.sizePolicy().hasHeightForWidth())
        self.txtOtherComments.setSizePolicy(sizePolicy)
        self.txtOtherComments.setObjectName("txtOtherComments")
        self.gridlayout.addWidget(self.txtOtherComments,1,0,1,1)

        self.label_2 = QtGui.QLabel(frmHeader)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,2,0,1,1)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.resetButton = QtGui.QPushButton(frmHeader)
        self.resetButton.setEnabled(True)
        self.resetButton.setObjectName("resetButton")
        self.hboxlayout.addWidget(self.resetButton)

        self.applyButton = QtGui.QPushButton(frmHeader)
        self.applyButton.setObjectName("applyButton")
        self.hboxlayout.addWidget(self.applyButton)

        spacerItem1 = QtGui.QSpacerItem(131,31,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)

        self.okButton = QtGui.QPushButton(frmHeader)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)

        self.cancelButton = QtGui.QPushButton(frmHeader)
        self.cancelButton.setObjectName("cancelButton")
        self.hboxlayout.addWidget(self.cancelButton)
        self.gridlayout.addLayout(self.hboxlayout,4,0,1,1)

        self.label = QtGui.QLabel(frmHeader)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        self.retranslateUi(frmHeader)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),frmHeader.accept)
        QtCore.QObject.connect(self.cancelButton,QtCore.SIGNAL("clicked()"),frmHeader.reject)
        QtCore.QMetaObject.connectSlotsByName(frmHeader)

    def tr(self, string):
        return QtGui.QApplication.translate("frmHeader", string, None, QtGui.QApplication.UnicodeUTF8)

    def retranslateUi(self, frmHeader):
        frmHeader.setWindowTitle(self.tr("Header"))
        self.btnDown.setToolTip(self.tr("Move down"))
        self.btnUp.setToolTip(self.tr("Move up"))
        self.btnInsertRow.setToolTip(self.tr("Insert row"))
        self.btnDeleteRow.setToolTip(self.tr("delete row"))
        self.tableHeader.setColumnCount(2)
        self.tableHeader.clear()
        self.tableHeader.setColumnCount(2)
        self.tableHeader.setRowCount(0)
        self.label_2.setText(self.tr("Header"))
        self.resetButton.setText(self.tr("Reset"))
        self.applyButton.setText(self.tr("Apply Settings"))
        self.okButton.setText(self.tr("OK"))
        self.cancelButton.setText(self.tr("Cancel"))
        self.label.setText(self.tr("Comment"))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    frmHeader = QtGui.QDialog()
    ui = Ui_frmHeader()
    ui.setupUi(frmHeader)
    frmHeader.show()
    sys.exit(app.exec_())
