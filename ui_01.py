import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFileDialog

from NEPSE_DATASET_EXTRAXTOR_LOGIC_2_copy import column_names
from NEPSE_DATASET_EXTRAXTOR_LOGIC_2_copy import Nepse_Dataset_Extractor_Final_Class
import time


value = 0


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 265)
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame_upper = QtWidgets.QFrame(self.centralwidget)
        self.frame_upper.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_upper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_upper.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_upper.setObjectName("frame_upper")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_upper)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.frame_upper_left = QtWidgets.QFrame(self.frame_upper)
        self.frame_upper_left.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_upper_left.setStyleSheet("background-color: rgb(24, 24, 24);\n"
                                            "border-radius:5px;")
        self.frame_upper_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_upper_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_upper_left.setObjectName("frame_upper_left")
        self.label = QtWidgets.QLabel(self.frame_upper_left)

        self.label.setGeometry(QtCore.QRect(20, 0, 101, 31))
        self.label.setObjectName("label")

        self.line = QtWidgets.QFrame(self.frame_upper_left)
        self.line.setGeometry(QtCore.QRect(0, 40, 151, 3))
        self.line.setMinimumSize(QtCore.QSize(100, 0))
        self.line.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.label_2 = QtWidgets.QLabel(self.frame_upper_left)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 101, 21))
        self.label_2.setObjectName("label_2")

        self.line_2 = QtWidgets.QFrame(self.frame_upper_left)
        self.line_2.setGeometry(QtCore.QRect(0, 80, 151, 3))
        self.line_2.setMinimumSize(QtCore.QSize(100, 0))
        self.line_2.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.label_3 = QtWidgets.QLabel(self.frame_upper_left)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 101, 21))
        self.label_3.setObjectName("label_3")

        self.line_3 = QtWidgets.QFrame(self.frame_upper_left)
        self.line_3.setGeometry(QtCore.QRect(0, 120, 151, 3))
        self.line_3.setMinimumSize(QtCore.QSize(100, 0))
        self.line_3.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.pushButton_extract = QtWidgets.QPushButton(self.frame_upper_left)
        self.pushButton_extract.setGeometry(QtCore.QRect(30, 140, 91, 31))

        font = QtGui.QFont()
        font.setPointSize(10)

        self.pushButton_extract.setFont(font)
        self.pushButton_extract.setStyleSheet("background-color: rgb(235, 167, 20);\n"
                                              "\n"
                                              "QPushButton:: hover\n"
                                              "{\n"
                                              "background-color: rgb(254, 180, 21);\n"
                                              "    color: rgb(191, 191, 191);\n"
                                              "\n"
                                              "}")
        self.pushButton_extract.setObjectName("pushButton_extract")

        self.horizontalLayout.addWidget(self.frame_upper_left)
        self.frame_upper_right = QtWidgets.QFrame(self.frame_upper)
        self.frame_upper_right.setStyleSheet("background-color: rgb(24, 24, 24);\n"
                                             "border-radius:5px;")
        self.frame_upper_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_upper_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_upper_right.setObjectName("frame_upper_right")

        self.comboBox_1 = QtWidgets.QComboBox(self.frame_upper_right)
        self.comboBox_1.setGeometry(QtCore.QRect(10, 10, 451, 25))
        self.comboBox_1.setStyleSheet("background-color: rgb(49, 49, 49);\n"
                                      "color: rgb(186, 186, 186);\n"
                                      "border-radius:10px;")
        self.comboBox_1.setObjectName("comboBox_1")
        # column_names = []
        for i in column_names:
            self.comboBox_1.addItem(f'{i}')

        self.line_4 = QtWidgets.QFrame(self.frame_upper_right)
        self.line_4.setGeometry(QtCore.QRect(0, 40, 480, 3))
        self.line_4.setMinimumSize(QtCore.QSize(100, 0))
        self.line_4.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.line_5 = QtWidgets.QFrame(self.frame_upper_right)
        self.line_5.setGeometry(QtCore.QRect(0, 80, 480, 3))
        self.line_5.setMinimumSize(QtCore.QSize(100, 0))
        self.line_5.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.line_6 = QtWidgets.QFrame(self.frame_upper_right)
        self.line_6.setGeometry(QtCore.QRect(0, 120, 480, 3))
        self.line_6.setMinimumSize(QtCore.QSize(100, 0))
        self.line_6.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.lineEdit_main_path = QtWidgets.QLineEdit(self.frame_upper_right)
        self.lineEdit_main_path.setGeometry(QtCore.QRect(20, 50, 401, 20))
        self.lineEdit_main_path.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                              "color: rgb(252, 252, 252);")
        self.lineEdit_main_path.setObjectName("lineEdit_main_path")

        self.pushButton_main_path = QtWidgets.QPushButton(self.frame_upper_right)
        self.pushButton_main_path.setGeometry(QtCore.QRect(430, 50, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_main_path.setFont(font)
        self.pushButton_main_path.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.pushButton_main_path.setStyleSheet("background-color: rgb(235, 167, 20);\n"
                                                "\n"
                                                "QPushButton:: hover\n"
                                                "{\n"
                                                "background-color: rgb(254, 180, 21);\n"
                                                "    color: rgb(191, 191, 191);\n"
                                                "\n"
                                                "}")
        self.pushButton_main_path.setText("")
        self.pushButton_main_path.setObjectName("pushButton_main_path")
        self.pushButton_main_path.setIcon(
            QIcon(r'D:\Coding-Projects\pandas_full_tut\128px-Windows_Settings_app_icon.png'))

        self.lineEdit_save_to = QtWidgets.QLineEdit(self.frame_upper_right)
        self.lineEdit_save_to.setGeometry(QtCore.QRect(20, 90, 401, 20))
        self.lineEdit_save_to.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                            "color: rgb(252, 252, 252);")
        self.lineEdit_save_to.setObjectName("lineEdit_save_to")

        self.pushButton_save_to = QtWidgets.QPushButton(self.frame_upper_right)
        self.pushButton_save_to.setGeometry(QtCore.QRect(430, 90, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_save_to.setFont(font)
        self.pushButton_save_to.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.pushButton_save_to.setStyleSheet("background-color: rgb(235, 167, 20);\n"
                                              "\n"
                                              "QPushButton:: hover\n"
                                              "{\n"
                                              "background-color: rgb(254, 180, 21);\n"
                                              "    color: rgb(191, 191, 191);\n"
                                              "\n"
                                              "}")
        self.pushButton_save_to.setText("")
        self.pushButton_save_to.setObjectName("pushButton_save_to")
        self.pushButton_save_to.setIcon(
            QIcon(r'D:\Coding-Projects\pandas_full_tut\128px-Windows_Settings_app_icon.png'))

        self.frame_info = QtWidgets.QFrame(self.frame_upper_right)
        self.frame_info.setGeometry(QtCore.QRect(90, 150, 301, 31))
        self.frame_info.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.frame_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info.setObjectName("frame_info")

        self.label_4 = QtWidgets.QLabel(self.frame_info)
        self.label_4.setGeometry(QtCore.QRect(80, 10, 161, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("BEGIN EXTRACTION")
        self.horizontalLayout.addWidget(self.frame_upper_right)
        self.verticalLayout.addWidget(self.frame_upper)

        self.frame_bottom = QtWidgets.QFrame(self.centralwidget)
        self.frame_bottom.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_bottom.setStyleSheet("background-color: rgb(24, 24, 24);\n"
                                        "border-radius:10px;")
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_bottom)
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.progressBar_1 = QtWidgets.QProgressBar(self.frame_bottom)
        self.progressBar_1.setMinimumSize(QtCore.QSize(0, 25))
        # self.progressBar_1.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.progressBar_1.setStyleSheet("border-radius:5px;")
        self.progressBar_1.setProperty("value", 0)
        self.progressBar_1.setObjectName("progressBar_1")

        # Bindings
        self.pushButton_main_path.clicked.connect(self.main_path_extract)
        self.pushButton_save_to.clicked.connect(self.to_save_path)
        self.pushButton_extract.clicked.connect(self.thread_activator)

        self.verticalLayout_2.addWidget(self.progressBar_1)
        self.verticalLayout.addWidget(self.frame_bottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#fdfdfd;\">Symbol</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#fdfdfd;\">Main Path</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Save To</span></p></body></html>"))
        self.pushButton_extract.setText(_translate("MainWindow", "Extract"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">START EXTRACTION</span></p></body></html>"))

    def main_path_extract(self):
        self.label_4.setText('BEGIN EXTRACTION')
        self.file_path = str(QFileDialog.getExistingDirectory(None, "Select Any Folder"))
        print(self.file_path)
        self.lineEdit_main_path.setText(self.file_path)

    def to_save_path(self):
        self.to_save = QFileDialog.getSaveFileName()[0]
        # print(self.to_save)
        # self.to_save = self.to_save[0]
        print(type(self.to_save), self.to_save)
        self.lineEdit_save_to.setText(self.to_save)
        self.progressBar_1.setProperty("value", 0)

    def final_extraction(self):
        self.label_4.setText('BEGIN EXTRACTION')
        start_time = time.time()
        obj = Nepse_Dataset_Extractor_Final_Class(company_symbol=self.comboBox_1.currentText(),
                                                  main_path=self.file_path, save_to=self.to_save)
        # obj.column_names_extractore()
        obj.datalist_creator()
        from Nepse_Dataset_Extracter_Final_LOGIC_1_copy import number_of_rows_extracted
        obj.dataset_converter()
        self.label_4.setText('EXTRACTION COMPLETED')
        end_time = time.time()
        del obj
        print('Total_time =>', end_time - start_time)

        # print(self.to_save)
        # print(self.comboBox_1.currentText())

    def increment_progress_bar(self):
        global value
        self.progressBar_1.setProperty("value", 0)
        value = 0
        for i in range(101):
            value += 0.5
            self.progressBar_1.setValue(value)
            time.sleep(0.05)

    def thread_activator(self):
        try:
            th1 = threading.Thread(target=self.final_extraction, daemon=True)
            th2 = threading.Thread(target=self.increment_progress_bar, daemon=True)
            th1.start()
            th2.start()
        except Exception as e:
            print('Exception is  => ',e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
