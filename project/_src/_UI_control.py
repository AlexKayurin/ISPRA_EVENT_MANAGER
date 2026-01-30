# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_UI_control.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 420)
        MainWindow.setMinimumSize(QSize(530, 420))
        MainWindow.setMaximumSize(QSize(530, 420))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.b_selectproj = QPushButton(self.centralwidget)
        self.b_selectproj.setObjectName(u"b_selectproj")
        self.b_selectproj.setMinimumSize(QSize(150, 50))
        self.b_selectproj.setMaximumSize(QSize(150, 50))

        self.verticalLayout.addWidget(self.b_selectproj)

        self.lab_0 = QLabel(self.centralwidget)
        self.lab_0.setObjectName(u"lab_0")
        self.lab_0.setMinimumSize(QSize(500, 20))
        self.lab_0.setMaximumSize(QSize(500, 20))

        self.verticalLayout.addWidget(self.lab_0)

        self.table_cameras = QTableWidget(self.centralwidget)
        if (self.table_cameras.columnCount() < 1):
            self.table_cameras.setColumnCount(1)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(220, 220, 220));
        self.table_cameras.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.table_cameras.setObjectName(u"table_cameras")
        self.table_cameras.setMinimumSize(QSize(500, 200))
        self.table_cameras.setMaximumSize(QSize(500, 200))
        self.table_cameras.setToolTipDuration(-7)
        self.table_cameras.setAlternatingRowColors(True)
        self.table_cameras.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_cameras.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_cameras.setSortingEnabled(True)
        self.table_cameras.horizontalHeader().setDefaultSectionSize(500)

        self.verticalLayout.addWidget(self.table_cameras)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.b_run = QPushButton(self.centralwidget)
        self.b_run.setObjectName(u"b_run")
        self.b_run.setMinimumSize(QSize(150, 50))
        self.b_run.setMaximumSize(QSize(150, 50))

        self.horizontalLayout.addWidget(self.b_run)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b_comments = QPushButton(self.centralwidget)
        self.b_comments.setObjectName(u"b_comments")
        self.b_comments.setMinimumSize(QSize(150, 50))
        self.b_comments.setMaximumSize(QSize(150, 50))

        self.horizontalLayout.addWidget(self.b_comments)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lab_1 = QLabel(self.centralwidget)
        self.lab_1.setObjectName(u"lab_1")
        self.lab_1.setMinimumSize(QSize(200, 20))
        self.lab_1.setMaximumSize(QSize(200, 20))
        font2 = QFont()
        font2.setPointSize(6)
        font2.setBold(True)
        self.lab_1.setFont(font2)

        self.verticalLayout.addWidget(self.lab_1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Event Manager", None))
        self.b_selectproj.setText(QCoreApplication.translate("MainWindow", u"Select VS project", None))
        self.lab_0.setText(QCoreApplication.translate("MainWindow", u"Select camera in:", None))
        ___qtablewidgetitem = self.table_cameras.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CAMERA NAME", None));
        self.b_run.setText(QCoreApplication.translate("MainWindow", u"Save track and events", None))
        self.b_comments.setText(QCoreApplication.translate("MainWindow", u"Manage events", None))
        self.lab_1.setText(QCoreApplication.translate("MainWindow", u"30/01/2026   v1.4", None))
    # retranslateUi

