#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-05 11:14:46
# @Author  : Lewis Tian (chtian@hust.edu.cn)
# @Link    : https://lewistian.github.io/
# @Version : Python3.6

from ui_mwin import Ui_MWin
from PyQt5 import QtCore
from PyQt5.QtCore import QUrl, QThread, pyqtSignal
from  PyQt5.QtGui import QIcon, QPixmap, QDesktopServices, QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QProgressBar, QMenu, QAction
import re
import sys
import requests
import time
import json
import os
import threading
from contextlib import closing


class AmazonBookRecommendation(QMainWindow, Ui_MWin):
    def __init__(self, parent=None):
        super(AmazonBookRecommendation, self).__init__(parent)
        self.setupUi(self)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AmazonBookRecommendation()
    w.show()
    sys.exit(app.exec_())
