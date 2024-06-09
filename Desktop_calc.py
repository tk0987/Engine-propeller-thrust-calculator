# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pendulum.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
"""
one mistake was solved - all 'bout uncertainty() function.
mistake was that: degrees were feeding this function instead of radians. 
at 11 radians uncertainty was horrible.
problem solved


"""




from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QLineEdit, QWidget,QDialog)
import sys
import numpy as np
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 353)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Form.setAutoFillBackground(False)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 381, 331))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.LineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.LineEdit_2.setObjectName(u"LineEdit_2")

        self.gridLayout.addWidget(self.LineEdit_2, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.LineEdit = QLineEdit(self.gridLayoutWidget)
        self.LineEdit.setObjectName(u"LineEdit")

        self.gridLayout.addWidget(self.LineEdit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.LineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.LineEdit_3.setObjectName(u"LineEdit_3")

        self.gridLayout.addWidget(self.LineEdit_3, 2, 1, 1, 1)

        self.LineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.LineEdit_4.setObjectName(u"LineEdit_4")

        self.gridLayout.addWidget(self.LineEdit_4, 3, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.calculate_force_and_uncertainty)
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"ThurstPendulum_Calculator", None))
        # self.LineEdit_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "hr { height: 1px; border-width: 0; }\n"
# "li.unchecked::marker { content: \"\\2610\"; }\n"
# "li.checked::marker { content: \"\\2612\"; }\n"
# "</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.label_2.setText("Scale division [g]")
#         self.LineEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "hr { height: 1px; border-width: 0; }\n"
# "li.unchecked::marker { content: \"\\2610\"; }\n"
# "li.checked::marker { content: \"\\2612\"; }\n"
# "</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.label_4.setText("Scale division [deg]")
#         self.LineEdit_3.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "hr { height: 1px; border-width: 0; }\n"
# "li.unchecked::marker { content: \"\\2610\"; }\n"
# "li.checked::marker { content: \"\\2612\"; }\n"
# "</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
#         self.LineEdit_4.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "hr { height: 1px; border-width: 0; }\n"
# "li.unchecked::marker { content: \"\\2610\"; }\n"
# "li.checked::marker { content: \"\\2612\"; }\n"
# "</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
# "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.label.setText("Mass [g]")
        self.label_3.setText("Angle\nof displacement \n[deg]")
        self.pushButton.setText( "Calculate thrust [N]")
        self.label_5.setText("-------")
    # retranslateUi
    def calculate_force_and_uncertainty(self):
        def uncertainty(u_deg,deg,u_mass,mass):
            return np.sqrt((u_deg*mass/1000.0/np.cos(deg)**2)**2+(np.tan(deg)*u_mass/1000.0)**2)
        g=9.81
        deg=float(self.LineEdit_3.text())
        mass_g=float(self.LineEdit.text())
        u_deg=float(self.LineEdit_4.text())/180.0*np.pi
        u_mass=float(self.LineEdit_2.text())
        rad=deg/180*np.pi
        thrust=np.tan(rad)*mass_g*g/1000.0
        u_thrust=uncertainty(u_deg,rad,u_mass,mass_g)
        self.label_5.setText(f"Thrust: {thrust:.4f} \u00B1 {u_thrust:.4f} [N]")
if __name__=="__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
