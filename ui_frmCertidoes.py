# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmCertidoesiBtMZg.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(343, 223)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.cbTodas = QCheckBox(self.centralwidget)
        self.cbTodas.setObjectName(u"cbTodas")
        self.cbTodas.setGeometry(QRect(41, 43, 53, 20))
        self.cbTodas.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbTodas.setChecked(True)
        self.txtCNPJ = QLineEdit(self.centralwidget)
        self.txtCNPJ.setObjectName(u"txtCNPJ")
        self.txtCNPJ.setGeometry(QRect(146, 42, 151, 22))
        font = QFont()
        font.setKerning(True)
        self.txtCNPJ.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(106, 44, 30, 16))
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 78, 281, 22))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cbCND = QCheckBox(self.layoutWidget)
        self.cbCND.setObjectName(u"cbCND")
        self.cbCND.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbCND.setCheckable(True)
        self.cbCND.setChecked(True)

        self.horizontalLayout.addWidget(self.cbCND)

        self.cbCRF = QCheckBox(self.layoutWidget)
        self.cbCRF.setObjectName(u"cbCRF")
        self.cbCRF.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbCRF.setChecked(True)

        self.horizontalLayout.addWidget(self.cbCRF)

        self.cbCADIN = QCheckBox(self.layoutWidget)
        self.cbCADIN.setObjectName(u"cbCADIN")
        self.cbCADIN.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbCADIN.setChecked(True)

        self.horizontalLayout.addWidget(self.cbCADIN)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(40, 108, 281, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cbE_Sancoes = QCheckBox(self.layoutWidget1)
        self.cbE_Sancoes.setObjectName(u"cbE_Sancoes")
        self.cbE_Sancoes.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbE_Sancoes.setChecked(True)

        self.horizontalLayout_2.addWidget(self.cbE_Sancoes)

        self.cbApenados = QCheckBox(self.layoutWidget1)
        self.cbApenados.setObjectName(u"cbApenados")
        self.cbApenados.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbApenados.setChecked(True)

        self.horizontalLayout_2.addWidget(self.cbApenados)

        self.cbCEIS = QCheckBox(self.layoutWidget1)
        self.cbCEIS.setObjectName(u"cbCEIS")
        self.cbCEIS.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbCEIS.setChecked(True)

        self.horizontalLayout_2.addWidget(self.cbCEIS)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(78, 154, 191, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btConsultar = QPushButton(self.layoutWidget2)
        self.btConsultar.setObjectName(u"btConsultar")
        self.btConsultar.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_3.addWidget(self.btConsultar)

        self.btCancelar = QPushButton(self.layoutWidget2)
        self.btCancelar.setObjectName(u"btCancelar")
        self.btCancelar.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_3.addWidget(self.btCancelar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btCancelar.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Consultar Certid\u00f5es - USP", None))
        self.cbTodas.setText(QCoreApplication.translate("MainWindow", u"Todas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CNPJ:", None))
        self.cbCND.setText(QCoreApplication.translate("MainWindow", u"CND", None))
        self.cbCRF.setText(QCoreApplication.translate("MainWindow", u"CRF", None))
        self.cbCADIN.setText(QCoreApplication.translate("MainWindow", u"CADIN", None))
        self.cbE_Sancoes.setText(QCoreApplication.translate("MainWindow", u"E-San\u00e7\u00f5es", None))
        self.cbApenados.setText(QCoreApplication.translate("MainWindow", u"Apenados", None))
        self.cbCEIS.setText(QCoreApplication.translate("MainWindow", u"CEIS", None))
        self.btConsultar.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.btCancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

