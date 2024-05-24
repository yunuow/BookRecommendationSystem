# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
import csv
import json


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


id_path = r'id_mapping.json'
id_mapping = read_json(id_path)
id_mapping_reverse = {v: k for k, v in id_mapping.items()}
user_path = r'user_id_mapping.json'
user_mapping = read_json(user_path)

# 构建推荐查询字典
output_path = r'output.txt'
output_dict = {}
with open(output_path, 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split()  # 按空格分隔每一行
        if parts:
            # 第一列作为字典的键
            key = parts[0]
            value = []
            for item in parts[1:]:
                value.append(id_mapping_reverse[item])
            output_dict[key] = value

books_data = {}

books_title2row = read_json(r'books_title2row.json')
books_id2title = read_json(r'books_id2title.json')
books_title2id = {v: k for k, v in books_id2title.items()}
with open(r'archive/books_data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for i, row in enumerate(reader):
        books_data[books_title2id[row[0]]] = row

class Ui_MWin(object):
    def setupUi(self, MWin):
        MWin.setObjectName("MWin")
        MWin.resize(1281, 1008)
        MWin.setMinimumSize(QtCore.QSize(1281, 1008))
        MWin.setMaximumSize(QtCore.QSize(1581, 1314))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        MWin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MWin.setWindowIcon(icon)
        self.load_stylesheet(r'style.qss')
        self.centralWidget = QtWidgets.QWidget(MWin)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(30, 30))
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setObjectName("tabWidget")

        # 第一个标签页
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab1)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout1Main = QtWidgets.QVBoxLayout()
        self.layout1Main.setSpacing(10)
        self.layout1Main.setObjectName("layout1Main")
        self.layout1T1 = QtWidgets.QHBoxLayout()
        self.layout1T1.setSpacing(6)
        self.layout1T1.setObjectName("layout1T1")
        font = QtGui.QFont()
        font.setPointSize(10)

        self.table_widget = QTableWidget(self.tab1)
        self.table_widget.setObjectName("tableWidget")
        self.layout1Main.addLayout(self.layout1T1)
        self.layout1Main.addWidget(self.table_widget)
        self.horizontalLayout.addLayout(self.layout1Main)
        self.display_csv(r'archive/books_data.csv', self.table_widget)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icon1"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab1, icon1, "")

        # 第二个标签页
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.horizontalLayout2 = QtWidgets.QHBoxLayout(self.tab2)
        self.horizontalLayout2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout2.setSpacing(6)
        self.horizontalLayout2.setObjectName("horizontalLayout")
        self.layout2Main = QtWidgets.QVBoxLayout()
        self.layout2Main.setSpacing(10)
        self.layout2Main.setObjectName("layout2Main")
        self.layout2T1 = QtWidgets.QHBoxLayout()
        self.layout2T1.setSpacing(6)
        self.layout2T1.setObjectName("layout2T1")
        font = QtGui.QFont()
        font.setPointSize(10)

        self.table_widget2 = QTableWidget(self.tab2)
        self.table_widget2.setObjectName("tableWidget")
        self.layout2Main.addLayout(self.layout2T1)
        self.layout2Main.addWidget(self.table_widget2)
        self.horizontalLayout2.addLayout(self.layout2Main)
        self.display_csv(r'archive/Books_rating.csv', self.table_widget2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icon2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab2, icon2, "")

        # 第三个标签页
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.horizontalLayout3 = QtWidgets.QHBoxLayout(self.tab3)
        self.horizontalLayout3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout3.setSpacing(6)
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        self.layout3Main = QtWidgets.QVBoxLayout()
        self.layout3Main.setSpacing(10)
        self.layout3Main.setObjectName("layout3Main")
        # 创建一个水平布局用于放置 lineEdit_input 和 search 按钮
        self.layout3T1 = QtWidgets.QHBoxLayout()
        self.layout3T1.setSpacing(6)
        self.layout3T1.setObjectName("layout3T1")
        # 创建 QLabel 并添加到水平布局中
        self.label_username = QtWidgets.QLabel(self.tab3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_username.setFont(font)
        self.label_username.setText("用户名")
        self.label_username.setObjectName("label_username")
        self.layout3T1.addWidget(self.label_username)
        # 创建 lineEdit_input 并添加到水平布局中
        self.lineEdit_input = QtWidgets.QLineEdit(self.tab3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_input.setFont(font)
        self.lineEdit_input.setInputMask("")
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.lineEdit_input.setFixedHeight(50)

        self.layout3T1.addWidget(self.lineEdit_input)
        # 创建 search 按钮并添加到水平布局中
        self.search = QtWidgets.QPushButton(self.tab3)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(15)
        self.search.setFont(font)
        self.search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icon3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon3)
        self.search.setObjectName("search")
        self.layout3T1.addWidget(self.search)
        # 将水平布局添加到 layout3Main 的顶部
        self.layout3Main.addLayout(self.layout3T1)
        # 继续添加其他控件或布局到 layout3Main 中
        self.tableWidget3 = QtWidgets.QTableWidget(self.tab3)
        self.tableWidget3.setObjectName("tableWidget")

        self.layout3Main.addWidget(self.tableWidget3)
        # 将 layout3Main 添加到水平布局中
        self.horizontalLayout3.addLayout(self.layout3Main)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icon3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab3, icon3, "")

        # 第四个标签页
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab4)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_about1 = QtWidgets.QLabel(self.tab4)
        self.label_about1.setFont(font)
        self.label_about1.setAlignment(QtCore.Qt.AlignLeft)  # 设置左对齐
        self.label_about1.setObjectName("label_about1")
        self.label_about1.setText("Label About 1")
        self.label_about1.setFixedHeight(30)
        self.verticalLayout_4.addWidget(self.label_about1)

        self.label_about2 = QtWidgets.QLabel(self.tab4)
        self.label_about2.setFont(font)
        self.label_about2.setAlignment(QtCore.Qt.AlignLeft)  # 设置左对齐
        self.label_about2.setObjectName("label_about2")
        self.label_about2.setText("Label About 2")
        self.label_about2.setFixedHeight(30)
        self.verticalLayout_4.addWidget(self.label_about2)

        self.label_about3 = QtWidgets.QLabel(self.tab4)
        self.label_about3.setFont(font)
        self.label_about3.setAlignment(QtCore.Qt.AlignLeft)  # 设置左对齐
        self.label_about3.setObjectName("label_about3")
        self.label_about3.setText("Label About 3")
        self.label_about3.setFixedHeight(30)
        self.verticalLayout_4.addWidget(self.label_about3)

        self.label_about4 = QtWidgets.QLabel(self.tab4)
        self.label_about4.setFont(font)
        self.label_about4.setAlignment(QtCore.Qt.AlignLeft)  # 设置左对齐
        self.label_about4.setObjectName("label_about4")
        self.label_about4.setText("Label About 4")
        self.label_about4.setFixedHeight(30)
        self.verticalLayout_4.addWidget(self.label_about4)

        self.label_about5 = QtWidgets.QLabel(self.tab4)
        self.label_about5.setFont(font)
        self.label_about5.setAlignment(QtCore.Qt.AlignLeft)  # 设置左对齐
        self.label_about5.setObjectName("label_about5")
        self.label_about5.setText("Label About 5")
        self.label_about5.setFixedHeight(30)
        self.verticalLayout_4.addWidget(self.label_about5)

        self.label_about6 = QtWidgets.QLabel(self.tab4)
        self.label_about6.setFont(font)
        self.label_about6.setAlignment(QtCore.Qt.AlignLeft)  # 设置左对齐
        self.label_about6.setObjectName("label_about6")
        self.label_about6.setText("Label About 6")
        self.label_about6.setFixedHeight(30)
        self.verticalLayout_4.addWidget(self.label_about6)

        spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacer)

        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icon4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab4, icon5, "")


        self.verticalLayout.addWidget(self.tabWidget)
        MWin.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MWin)
        self.statusBar.setObjectName("statusBar")
        MWin.setStatusBar(self.statusBar)

        self.retranslateUi(MWin)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MWin)

        self.lineEdit_input.setFocus()

        # 连接按钮点击事件
        self.search.clicked.connect(self.on_search_click)

    def retranslateUi(self, MWin):
        _translate = QtCore.QCoreApplication.translate
        MWin.setWindowTitle(_translate("MWin", "亚马逊图书推荐"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MWin", "书籍信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MWin", "书籍评分"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MWin", "用户推荐"))
        self.search.setText(_translate("MWin", "推荐"))
        self.label_about1.setText(_translate("MWin", "感谢使用亚马逊推荐系统ο(=•ω＜=)ρ⌒☆"))
        self.label_about2.setText(_translate("MWin", "项目制作人：于松涛、王凯、丁文星、张恒顺"))
        self.label_about3.setText(_translate("MWin", "数据集来源："))
        self.label_about4.setText(_translate("MWin", "gitbub项目地址："))
        self.label_about5.setText(_translate("MWin", "项目使用模型为："))
        self.label_about6.setText(_translate("MWin", "ps:数据展示部分只显示前400条数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), _translate("MWin", "关于项目"))

    def display_csv(self, file_name, table_widget):
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data = []
            # 只读取两百行
            for i, row in enumerate(reader):
                if i >= 400:
                    break
                data.append(row)

            if data:
                # 设置表格的行列数
                table_widget.setRowCount(len(data))
                headers = data[0]
                table_widget.setColumnCount(len(headers))
                table_widget.setHorizontalHeaderLabels(headers)

                # 填充表格
                for row_idx, row_data in enumerate(data[1:]):
                    for col_idx, col_data in enumerate(row_data):
                        item = QTableWidgetItem(col_data)
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        table_widget.setItem(row_idx, col_idx, item)
                        table_widget.setColumnWidth(row_idx, 400)

    def on_search_click(self):
        # 获取 lineEdit_input 的内容
        username = self.lineEdit_input.text()
        print(f"用户名: {username}")
        recommend_result = output_dict[user_mapping[str(username)]]
        print(recommend_result)
        if len(recommend_result) != 0:
            self.tableWidget3.setRowCount(len(recommend_result))
            self.tableWidget3.setColumnCount(2)
            self.tableWidget3.setHorizontalHeaderLabels(["推荐书籍编号", ""])
            self.tableWidget3.setColumnWidth(1, 120)
            header = self.tableWidget3.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            for row in range(len(recommend_result)):
                book_id = str(recommend_result[row])
                item = QtWidgets.QTableWidgetItem(books_id2title[book_id])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget3.setItem(row, 0, item)
                button = QtWidgets.QPushButton("查看")
                button.setFixedWidth(100)
                button.clicked.connect(lambda ch, r=row: self.on_button_click(book_id))
                # 创建一个 QWidget 作为容器，并将其设置为水平布局
                container = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout()
                layout.addWidget(button)
                layout.setContentsMargins(0, 0, 0, 0)  # 移除布局的边距
                layout.setAlignment(QtCore.Qt.AlignCenter)  # 设置布局中的控件居中对齐
                container.setLayout(layout)
                self.tableWidget3.setCellWidget(row, 1, container)

    def on_button_click(self, book_id):
        # 获取该行的数据
        self.child_window = ChildWindow()
        self.child_window.add_info(book_id)
        self.child_window.setWindowTitle("《" + books_id2title[book_id] + "》信息")
        self.child_window.show()

    def load_stylesheet(self, file_path):
        with open(file_path, "r") as file:
            self.setStyleSheet(file.read())


class ChildWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(881, 608)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        # self.load_stylesheet(r'style.qss')

    def load_stylesheet(self, file_path):
        with open(file_path, "r") as file:
            self.setStyleSheet(file.read())

    def add_info(self, book_id):
        book_info = books_data[book_id]
        print(book_info)
        layoutChild = QtWidgets.QTableWidget()
        layoutChild.setColumnCount(1)
        layoutChild.setRowCount(11)
        layoutChild.setVerticalHeaderLabels(["id", "Title", "description", "authors", "images", "previewLink",
                                             "publisher", "publishedDate", "infoLink", "categories", "ratingsCount"])
        layoutChild.setHorizontalHeaderLabels(["信息"])
        header = layoutChild.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        item = QTableWidgetItem(book_id)

        layoutChild.setItem(0, 0, item)
        item = QTableWidgetItem(book_info[0])

        layoutChild.setItem(1, 0, item)
        item = QTableWidgetItem(book_info[1])

        layoutChild.setItem(2, 0, item)
        item = QTableWidgetItem(book_info[2])

        layoutChild.setItem(3, 0, item)
        item = QTableWidgetItem(book_info[3])

        layoutChild.setItem(4, 0, item)
        item = QTableWidgetItem(book_info[4])

        layoutChild.setItem(5, 0, item)
        item = QTableWidgetItem(book_info[5])

        layoutChild.setItem(6, 0, item)
        item = QTableWidgetItem(book_info[6])

        layoutChild.setItem(7, 0, item)
        item = QTableWidgetItem(book_info[7])

        layoutChild.setItem(8, 0, item)
        item = QTableWidgetItem(book_info[8])

        layoutChild.setItem(9, 0, item)
        item = QTableWidgetItem(book_info[9])

        layoutChild.setItem(10, 0, item)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(layoutChild)
        self.setLayout(layout)
        self.load_stylesheet(r'style.qss')
