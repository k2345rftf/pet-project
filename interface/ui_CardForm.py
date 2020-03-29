# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Гена/AppData/Local/Temp/CardFormZYZcaA.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CardForm(object):
    def setupUi(self, CardForm):
        CardForm.setObjectName("CardForm")
        CardForm.setWindowModality(QtCore.Qt.WindowModal)
        CardForm.resize(331, 481)
        CardForm.setMinimumSize(QtCore.QSize(331, 481))
        CardForm.setMaximumSize(QtCore.QSize(331, 481))
        self.verticalLayoutWidget = QtWidgets.QWidget(CardForm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 331, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.addLine = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addLine.setObjectName("addLine")
        self.verticalLayout.addWidget(self.addLine)
        self.delLine = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delLine.setObjectName("delLine")
        self.verticalLayout.addWidget(self.delLine)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget_2.setRowCount(10)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget_2)

        self.retranslateUi(CardForm)
        QtCore.QMetaObject.connectSlotsByName(CardForm)

    def retranslateUi(self, CardForm):
        _translate = QtCore.QCoreApplication.translate
        CardForm.setWindowTitle(_translate("CardForm", "Карточка садовода"))
        self.label.setText(_translate("CardForm", "Дата документа"))
        self.label_2.setText(_translate("CardForm", "Номер документа"))
        self.label_3.setText(_translate("CardForm", "ФИО"))
        self.addLine.setText(_translate("CardForm", "Добавить поле"))
        self.delLine.setText(_translate("CardForm", "Удалить поле"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("CardForm", "Услуга"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("CardForm", "Приход"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("CardForm", "Расход"))
