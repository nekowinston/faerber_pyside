# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

from qt.QClickDropLabel import QClickDropLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(810, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        MainWindow.setPalette(palette)
        self.act_exit = QAction(MainWindow)
        self.act_exit.setObjectName(u"act_exit")
        self.act_save = QAction(MainWindow)
        self.act_save.setObjectName(u"act_save")
        self.act_save.setEnabled(False)
        self.act_pref = QAction(MainWindow)
        self.act_pref.setObjectName(u"act_pref")
        self.act_support = QAction(MainWindow)
        self.act_support.setObjectName(u"act_support")
        self.act_about = QAction(MainWindow)
        self.act_about.setObjectName(u"act_about")
        self.act_open = QAction(MainWindow)
        self.act_open.setObjectName(u"act_open")
        self.wgt_central = QWidget(MainWindow)
        self.wgt_central.setObjectName(u"wgt_central")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wgt_central.sizePolicy().hasHeightForWidth())
        self.wgt_central.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.wgt_central)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.wgt_stacked = QStackedWidget(self.wgt_central)
        self.wgt_stacked.setObjectName(u"wgt_stacked")
        self.wgt_stacked.setAcceptDrops(False)
        self.wgt_stacked.setFrameShape(QFrame.NoFrame)
        self.pnl_empty = QWidget()
        self.pnl_empty.setObjectName(u"pnl_empty")
        self.pnl_empty.setAcceptDrops(False)
        self.verticalLayout_2 = QVBoxLayout(self.pnl_empty)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_open_image = QClickDropLabel(self.pnl_empty)
        self.lbl_open_image.setObjectName(u"lbl_open_image")
        self.lbl_open_image.setAcceptDrops(True)
        self.lbl_open_image.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_2.addWidget(self.lbl_open_image)

        self.wgt_stacked.addWidget(self.pnl_empty)
        self.pnl_view = QWidget()
        self.pnl_view.setObjectName(u"pnl_view")
        self.verticalLayout = QVBoxLayout(self.pnl_view)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frm_imgview = QFrame(self.pnl_view)
        self.frm_imgview.setObjectName(u"frm_imgview")
        self.frm_imgview.setFrameShape(QFrame.NoFrame)
        self.frm_imgview.setLineWidth(0)

        self.verticalLayout.addWidget(self.frm_imgview)

        self.btn_compare = QPushButton(self.pnl_view)
        self.btn_compare.setObjectName(u"btn_compare")

        self.verticalLayout.addWidget(self.btn_compare)

        self.wgt_stacked.addWidget(self.pnl_view)

        self.gridLayout.addWidget(self.wgt_stacked, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.wgt_central)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 810, 19))
        self.mnu_file = QMenu(self.menubar)
        self.mnu_file.setObjectName(u"mnu_file")
        self.mnu_edit = QMenu(self.menubar)
        self.mnu_edit.setObjectName(u"mnu_edit")
        self.mnu_help = QMenu(self.menubar)
        self.mnu_help.setObjectName(u"mnu_help")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.mnu_file.menuAction())
        self.menubar.addAction(self.mnu_edit.menuAction())
        self.menubar.addAction(self.mnu_help.menuAction())
        self.mnu_file.addAction(self.act_open)
        self.mnu_file.addAction(self.act_save)
        self.mnu_file.addAction(self.act_exit)
        self.mnu_edit.addAction(self.act_pref)
        self.mnu_help.addAction(self.act_support)
        self.mnu_help.addAction(self.act_about)

        self.retranslateUi(MainWindow)
        self.act_exit.triggered.connect(MainWindow.close)

        self.wgt_stacked.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.act_exit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.act_exit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.act_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.act_save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.act_pref.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
#if QT_CONFIG(shortcut)
        self.act_pref.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+,", None))
#endif // QT_CONFIG(shortcut)
        self.act_support.setText(QCoreApplication.translate("MainWindow", u"Support", None))
#if QT_CONFIG(shortcut)
        self.act_support.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.act_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(shortcut)
        self.act_about.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+F1", None))
#endif // QT_CONFIG(shortcut)
        self.act_open.setText(QCoreApplication.translate("MainWindow", u"Open Image", None))
#if QT_CONFIG(shortcut)
        self.act_open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_open_image.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Click inside to open the Filebrowser</span></p><p align=\"center\"><span style=\" font-size:10pt;\">or drop an Image anywhere</span></p></body></html>", None))
        self.btn_compare.setText(QCoreApplication.translate("MainWindow", u"Compare", None))
        self.mnu_file.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.mnu_edit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.mnu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

