# Form implementation generated from reading ui file 'view/history.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HistoryDialog(object):
    def setupUi(self, HistoryDialog):
        HistoryDialog.setObjectName("HistoryDialog")
        HistoryDialog.resize(590, 399)
        HistoryDialog.setWindowOpacity(4.0)
        self.query_btn = QtWidgets.QPushButton(parent=HistoryDialog)
        self.query_btn.setGeometry(QtCore.QRect(10, 70, 51, 31))
        self.query_btn.setObjectName("query_btn")
        self.choose_order_box = QtWidgets.QComboBox(parent=HistoryDialog)
        self.choose_order_box.setGeometry(QtCore.QRect(70, 20, 111, 31))
        self.choose_order_box.setObjectName("choose_order_box")
        self.choose_order_box.addItem("")
        self.choose_order_box.addItem("")
        self.choose_order_box.addItem("")
        self.label = QtWidgets.QLabel(parent=HistoryDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 31))
        self.label.setObjectName("label")
        self.query_result_table = QtWidgets.QTableWidget(parent=HistoryDialog)
        self.query_result_table.setGeometry(QtCore.QRect(190, 10, 391, 381))
        self.query_result_table.setObjectName("query_result_table")
        self.query_result_table.setColumnCount(4)
        self.query_result_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.query_result_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.query_result_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.query_result_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.query_result_table.setHorizontalHeaderItem(3, item)
        self.result_group = QtWidgets.QGroupBox(parent=HistoryDialog)
        self.result_group.setGeometry(QtCore.QRect(10, 110, 171, 201))
        self.result_group.setObjectName("result_group")
        self.label_7 = QtWidgets.QLabel(parent=self.result_group)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 131, 31))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(parent=self.result_group)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 131, 31))
        self.label_9.setObjectName("label_9")
        self.dice_label = QtWidgets.QLabel(parent=self.result_group)
        self.dice_label.setGeometry(QtCore.QRect(10, 70, 141, 41))
        self.dice_label.setText("")
        self.dice_label.setWordWrap(True)
        self.dice_label.setObjectName("dice_label")
        self.class_label = QtWidgets.QLabel(parent=self.result_group)
        self.class_label.setGeometry(QtCore.QRect(10, 150, 141, 21))
        self.class_label.setText("")
        self.class_label.setObjectName("class_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=HistoryDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 70, 111, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.asc_order = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        self.asc_order.setChecked(True)
        self.asc_order.setObjectName("asc_order")
        self.horizontalLayout.addWidget(self.asc_order)
        self.desc_order = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        self.desc_order.setChecked(False)
        self.desc_order.setObjectName("desc_order")
        self.horizontalLayout.addWidget(self.desc_order)
        self.cancel_chosen_btn = QtWidgets.QPushButton(parent=HistoryDialog)
        self.cancel_chosen_btn.setEnabled(True)
        self.cancel_chosen_btn.setGeometry(QtCore.QRect(20, 320, 151, 31))
        self.cancel_chosen_btn.setObjectName("cancel_chosen_btn")
        self.restore_chosen_btn = QtWidgets.QPushButton(parent=HistoryDialog)
        self.restore_chosen_btn.setGeometry(QtCore.QRect(20, 360, 151, 31))
        self.restore_chosen_btn.setObjectName("restore_chosen_btn")

        self.retranslateUi(HistoryDialog)
        QtCore.QMetaObject.connectSlotsByName(HistoryDialog)

    def retranslateUi(self, HistoryDialog):
        _translate = QtCore.QCoreApplication.translate
        HistoryDialog.setWindowTitle(_translate("HistoryDialog", "查看历史"))
        self.query_btn.setText(_translate("HistoryDialog", "查询"))
        self.choose_order_box.setItemText(0, _translate("HistoryDialog", "编号"))
        self.choose_order_box.setItemText(1, _translate("HistoryDialog", "日期"))
        self.choose_order_box.setItemText(2, _translate("HistoryDialog", "名字"))
        self.label.setText(_translate("HistoryDialog", "查询方式"))
        item = self.query_result_table.horizontalHeaderItem(0)
        item.setText(_translate("HistoryDialog", "编号"))
        item = self.query_result_table.horizontalHeaderItem(1)
        item.setText(_translate("HistoryDialog", "名称"))
        item = self.query_result_table.horizontalHeaderItem(2)
        item.setText(_translate("HistoryDialog", "标签"))
        item = self.query_result_table.horizontalHeaderItem(3)
        item.setText(_translate("HistoryDialog", "日期"))
        self.result_group.setTitle(_translate("HistoryDialog", "结果"))
        self.label_7.setText(_translate("HistoryDialog", "分类置信度："))
        self.label_9.setText(_translate("HistoryDialog", "类别："))
        self.asc_order.setText(_translate("HistoryDialog", "正序"))
        self.desc_order.setText(_translate("HistoryDialog", "倒序"))
        self.cancel_chosen_btn.setText(_translate("HistoryDialog", "取消选择"))
        self.restore_chosen_btn.setText(_translate("HistoryDialog", "将选中信息复原"))
