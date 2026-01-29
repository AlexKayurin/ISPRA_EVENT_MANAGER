# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_UI_merge.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1075, 684)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.b_selectevt = QPushButton(self.centralwidget)
        self.b_selectevt.setObjectName(u"b_selectevt")
        self.b_selectevt.setMinimumSize(QSize(150, 50))
        self.b_selectevt.setMaximumSize(QSize(150, 50))
        self.b_selectevt.setFont(font)

        self.horizontalLayout.addWidget(self.b_selectevt)

        self.b_selectdvix = QPushButton(self.centralwidget)
        self.b_selectdvix.setObjectName(u"b_selectdvix")
        self.b_selectdvix.setMinimumSize(QSize(150, 50))
        self.b_selectdvix.setMaximumSize(QSize(150, 50))
        self.b_selectdvix.setFont(font)

        self.horizontalLayout.addWidget(self.b_selectdvix)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b_selectcmt = QPushButton(self.centralwidget)
        self.b_selectcmt.setObjectName(u"b_selectcmt")
        self.b_selectcmt.setMinimumSize(QSize(150, 50))
        self.b_selectcmt.setMaximumSize(QSize(150, 50))
        self.b_selectcmt.setFont(font)

        self.horizontalLayout.addWidget(self.b_selectcmt)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lab_0 = QLabel(self.centralwidget)
        self.lab_0.setObjectName(u"lab_0")
        self.lab_0.setMinimumSize(QSize(0, 20))
        self.lab_0.setMaximumSize(QSize(150, 20))
        self.lab_0.setFont(font)

        self.horizontalLayout_3.addWidget(self.lab_0)

        self.sp_maxvar = QSpinBox(self.centralwidget)
        self.sp_maxvar.setObjectName(u"sp_maxvar")
        self.sp_maxvar.setMinimumSize(QSize(100, 20))
        self.sp_maxvar.setMaximumSize(QSize(100, 20))
        self.sp_maxvar.setFont(font)
        self.sp_maxvar.setMinimum(1)
        self.sp_maxvar.setMaximum(9999)
        self.sp_maxvar.setValue(20)

        self.horizontalLayout_3.addWidget(self.sp_maxvar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.lab_1 = QLabel(self.centralwidget)
        self.lab_1.setObjectName(u"lab_1")
        self.lab_1.setMinimumSize(QSize(0, 20))
        self.lab_1.setMaximumSize(QSize(200, 20))
        self.lab_1.setFont(font)
        self.lab_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lab_1)

        self.lineed_colsfrom = QLineEdit(self.centralwidget)
        self.lineed_colsfrom.setObjectName(u"lineed_colsfrom")
        self.lineed_colsfrom.setMinimumSize(QSize(100, 20))
        self.lineed_colsfrom.setMaximumSize(QSize(100, 20))
        self.lineed_colsfrom.setFont(font)

        self.horizontalLayout_3.addWidget(self.lineed_colsfrom)

        self.lab_2 = QLabel(self.centralwidget)
        self.lab_2.setObjectName(u"lab_2")
        self.lab_2.setMinimumSize(QSize(0, 20))
        self.lab_2.setMaximumSize(QSize(150, 20))
        self.lab_2.setSizeIncrement(QSize(0, 0))
        self.lab_2.setFont(font)
        self.lab_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lab_2)

        self.sp_colto = QSpinBox(self.centralwidget)
        self.sp_colto.setObjectName(u"sp_colto")
        self.sp_colto.setMinimumSize(QSize(75, 20))
        self.sp_colto.setMaximumSize(QSize(75, 20))
        self.sp_colto.setMinimum(1)

        self.horizontalLayout_3.addWidget(self.sp_colto)

        self.lab_3 = QLabel(self.centralwidget)
        self.lab_3.setObjectName(u"lab_3")
        self.lab_3.setMinimumSize(QSize(0, 20))
        self.lab_3.setMaximumSize(QSize(120, 20))
        self.lab_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lab_3)

        self.lineed_separator = QLineEdit(self.centralwidget)
        self.lineed_separator.setObjectName(u"lineed_separator")
        self.lineed_separator.setMinimumSize(QSize(50, 20))
        self.lineed_separator.setMaximumSize(QSize(50, 20))

        self.horizontalLayout_3.addWidget(self.lineed_separator)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.lab_4 = QLabel(self.centralwidget)
        self.lab_4.setObjectName(u"lab_4")
        self.lab_4.setMinimumSize(QSize(0, 20))
        self.lab_4.setMaximumSize(QSize(100, 20))
        self.lab_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lab_4)

        self.combo_filter = QComboBox(self.centralwidget)
        self.combo_filter.setObjectName(u"combo_filter")
        self.combo_filter.setMinimumSize(QSize(200, 20))
        self.combo_filter.setMaximumSize(QSize(200, 20))

        self.horizontalLayout_2.addWidget(self.combo_filter)

        self.lab_5 = QLabel(self.centralwidget)
        self.lab_5.setObjectName(u"lab_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_5.sizePolicy().hasHeightForWidth())
        self.lab_5.setSizePolicy(sizePolicy)
        self.lab_5.setMinimumSize(QSize(0, 20))
        self.lab_5.setMaximumSize(QSize(75, 20))
        self.lab_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lab_5)

        self.lineed_filter = QLineEdit(self.centralwidget)
        self.lineed_filter.setObjectName(u"lineed_filter")
        self.lineed_filter.setMinimumSize(QSize(150, 20))
        self.lineed_filter.setMaximumSize(QSize(150, 20))

        self.horizontalLayout_2.addWidget(self.lineed_filter)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.table_evts = QTableWidget(self.splitter)
        self.table_evts.setObjectName(u"table_evts")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.table_evts.sizePolicy().hasHeightForWidth())
        self.table_evts.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(8)
        self.table_evts.setFont(font1)
        self.table_evts.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.table_evts.setAlternatingRowColors(True)
        self.table_evts.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_evts.setSortingEnabled(True)
        self.splitter.addWidget(self.table_evts)
        self.table_cmts = QTableWidget(self.splitter)
        self.table_cmts.setObjectName(u"table_cmts")
        sizePolicy1.setHeightForWidth(self.table_cmts.sizePolicy().hasHeightForWidth())
        self.table_cmts.setSizePolicy(sizePolicy1)
        self.table_cmts.setFont(font1)
        self.table_cmts.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_cmts.setAlternatingRowColors(True)
        self.table_cmts.setSortingEnabled(True)
        self.splitter.addWidget(self.table_cmts)

        self.verticalLayout.addWidget(self.splitter)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.b_merge = QPushButton(self.centralwidget)
        self.b_merge.setObjectName(u"b_merge")
        self.b_merge.setMinimumSize(QSize(150, 50))
        self.b_merge.setMaximumSize(QSize(150, 50))
        self.b_merge.setFont(font)

        self.horizontalLayout_5.addWidget(self.b_merge)

        self.b_saveevts = QPushButton(self.centralwidget)
        self.b_saveevts.setObjectName(u"b_saveevts")
        self.b_saveevts.setMinimumSize(QSize(150, 50))
        self.b_saveevts.setMaximumSize(QSize(150, 50))
        self.b_saveevts.setFont(font)

        self.horizontalLayout_5.addWidget(self.b_saveevts)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1075, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Manage events", None))
        self.b_selectevt.setText(QCoreApplication.translate("MainWindow", u"Select Events file", None))
        self.b_selectdvix.setText(QCoreApplication.translate("MainWindow", u"Select DV ix (opt)", None))
        self.b_selectcmt.setText(QCoreApplication.translate("MainWindow", u"Select Comments file", None))
        self.lab_0.setText(QCoreApplication.translate("MainWindow", u"Max time variation (sec)", None))
        self.lab_1.setText(QCoreApplication.translate("MainWindow", u"Merge 'comments' colums:", None))
        self.lab_2.setText(QCoreApplication.translate("MainWindow", u"to 'events' column:", None))
        self.lab_3.setText(QCoreApplication.translate("MainWindow", u"with separator:", None))
        self.lineed_separator.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.lab_4.setText(QCoreApplication.translate("MainWindow", u"Filter column:", None))
        self.lab_5.setText(QCoreApplication.translate("MainWindow", u"by value:", None))
        self.b_merge.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
        self.b_saveevts.setText(QCoreApplication.translate("MainWindow", u"Save to Excel", None))
    # retranslateUi

