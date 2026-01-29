# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_UI_selectcmtsheet.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QHBoxLayout, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QSize(400, 300))
        Dialog.setMaximumSize(QSize(400, 300))
        font = QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_sheet = QTableWidget(Dialog)
        if (self.table_sheet.columnCount() < 1):
            self.table_sheet.setColumnCount(1)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(220, 220, 220));
        self.table_sheet.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.table_sheet.setObjectName(u"table_sheet")
        self.table_sheet.setMinimumSize(QSize(370, 230))
        self.table_sheet.setMaximumSize(QSize(370, 230))
        self.table_sheet.setAlternatingRowColors(True)
        self.table_sheet.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_sheet.setSortingEnabled(True)
        self.table_sheet.horizontalHeader().setDefaultSectionSize(370)

        self.verticalLayout.addWidget(self.table_sheet)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMinimumSize(QSize(370, 50))
        self.buttonBox.setMaximumSize(QSize(370, 50))
        self.buttonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Select sheet with events", None))
        ___qtablewidgetitem = self.table_sheet.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"SHEET NAME", None));
    # retranslateUi

