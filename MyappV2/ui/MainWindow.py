# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1193, 874)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Arial\";\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.horizontalLayout_17.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setStyleSheet("#lineEdit_username{\n"
"border-radius: 4px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.horizontalLayout_17.addWidget(self.lineEdit_username)
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setStyleSheet("#lineEdit_password{\n"
"border-radius: 4px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_17.addWidget(self.lineEdit_password)
        self.pushButton_run = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_run.setStyleSheet("#pushButton_run {\n"
"  border: none;\n"
"border-radius: 4px;\n"
"  color: white;\n"
"  padding: 2px 16px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"  -webkit-transition-duration: 0.4s; /* Safari */\n"
"  transition-duration: 0.4s;\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"#pushButton_run {\n"
"  background-color: white; \n"
"  color: #4CAF50; \n"
"  border: 2px solid #4CAF50;\n"
"}\n"
"\n"
"#pushButton_run:hover {\n"
"  background-color: #4CAF50;\n"
"  color: white;\n"
"}\n"
"\n"
"#pushButton_run:disabled {\n"
"  background-color: grey;\n"
"  color: white;\n"
"    border: 2px solid grey;\n"
"}\n"
"")
        self.pushButton_run.setDefault(False)
        self.pushButton_run.setFlat(False)
        self.pushButton_run.setObjectName("pushButton_run")
        self.horizontalLayout_17.addWidget(self.pushButton_run)
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setAutoFillBackground(False)
        self.pushButton_stop.setStyleSheet("#pushButton_stop {\n"
"  border: none;\n"
"border-radius: 4px;\n"
"  color: white;\n"
"  padding: 2px 16px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"  transition-duration: 0.4s;\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"#pushButton_stop {\n"
"  background-color: white; \n"
"  color: red; \n"
"  border: 2px solid red;\n"
"}\n"
"\n"
"#pushButton_stop:hover {\n"
"  background-color: red;\n"
"  color: white;\n"
"}\n"
"\n"
"#pushButton_stop:disabled {\n"
"  background-color: grey;\n"
"  color: white;\n"
"    border: 2px solid grey;\n"
"}\n"
"")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout_17.addWidget(self.pushButton_stop)
        self.button_testing = QtWidgets.QPushButton(self.centralwidget)
        self.button_testing.setStyleSheet("text: balik")
        self.button_testing.setCheckable(False)
        self.button_testing.setObjectName("button_testing")
        self.horizontalLayout_17.addWidget(self.button_testing)
        self.verticalLayout_11.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_home = QtWidgets.QWidget()
        self.tab_home.setObjectName("tab_home")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_home)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_home)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1092, 756))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_4.setStyleSheet("background-color: rgb(209, 236, 241);\n"
"")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.spinBox_follow = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_follow.setStyleSheet("")
        self.spinBox_follow.setReadOnly(True)
        self.spinBox_follow.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_follow.setMinimum(1)
        self.spinBox_follow.setMaximum(2000)
        self.spinBox_follow.setProperty("value", 50)
        self.spinBox_follow.setObjectName("spinBox_follow")
        self.verticalLayout.addWidget(self.spinBox_follow)
        self.spinBox_unfollow = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_unfollow.setReadOnly(True)
        self.spinBox_unfollow.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_unfollow.setMinimum(1)
        self.spinBox_unfollow.setMaximum(2000)
        self.spinBox_unfollow.setProperty("value", 30)
        self.spinBox_unfollow.setObjectName("spinBox_unfollow")
        self.verticalLayout.addWidget(self.spinBox_unfollow)
        self.spinBox_like = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_like.setReadOnly(True)
        self.spinBox_like.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_like.setMinimum(1)
        self.spinBox_like.setMaximum(2000)
        self.spinBox_like.setProperty("value", 50)
        self.spinBox_like.setObjectName("spinBox_like")
        self.verticalLayout.addWidget(self.spinBox_like)
        self.spinBox_comment = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_comment.setReadOnly(True)
        self.spinBox_comment.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_comment.setMinimum(1)
        self.spinBox_comment.setMaximum(2000)
        self.spinBox_comment.setProperty("value", 7)
        self.spinBox_comment.setObjectName("spinBox_comment")
        self.verticalLayout.addWidget(self.spinBox_comment)
        self.spinBox_getfollowers = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_getfollowers.setReadOnly(True)
        self.spinBox_getfollowers.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_getfollowers.setMinimum(1)
        self.spinBox_getfollowers.setMaximum(1000000)
        self.spinBox_getfollowers.setProperty("value", 100)
        self.spinBox_getfollowers.setObjectName("spinBox_getfollowers")
        self.verticalLayout.addWidget(self.spinBox_getfollowers)
        self.spinBox_getfollowing = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_getfollowing.setReadOnly(True)
        self.spinBox_getfollowing.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_getfollowing.setMinimum(1)
        self.spinBox_getfollowing.setMaximum(1000000)
        self.spinBox_getfollowing.setProperty("value", 100)
        self.spinBox_getfollowing.setObjectName("spinBox_getfollowing")
        self.verticalLayout.addWidget(self.spinBox_getfollowing)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.radioButton_slow = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_slow.setChecked(True)
        self.radioButton_slow.setObjectName("radioButton_slow")
        self.verticalLayout_6.addWidget(self.radioButton_slow)
        self.radioButton_standard = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_standard.setObjectName("radioButton_standard")
        self.verticalLayout_6.addWidget(self.radioButton_standard)
        self.radioButton_fast = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_fast.setObjectName("radioButton_fast")
        self.verticalLayout_6.addWidget(self.radioButton_fast)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_16.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setStyleSheet("background-color: rgb(209, 236, 241);")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_private = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_private.setObjectName("checkBox_private")
        self.verticalLayout_3.addWidget(self.checkBox_private)
        self.checkBox_no_profilePic = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_no_profilePic.setObjectName("checkBox_no_profilePic")
        self.verticalLayout_3.addWidget(self.checkBox_no_profilePic)
        self.checkBox_business = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_business.setObjectName("checkBox_business")
        self.verticalLayout_3.addWidget(self.checkBox_business)
        self.checkBox_verified = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_verified.setObjectName("checkBox_verified")
        self.verticalLayout_3.addWidget(self.checkBox_verified)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.horizontalLayout_16.addWidget(self.groupBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.groupBox_follow = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_follow.setStyleSheet("#groupBox_follow:checked{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.groupBox_follow.setCheckable(True)
        self.groupBox_follow.setChecked(False)
        self.groupBox_follow.setObjectName("groupBox_follow")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_follow)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_follow)
        self.label_2.setStyleSheet("#label_2:enabled{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_follow = QtWidgets.QComboBox(self.groupBox_follow)
        self.comboBox_follow.setObjectName("comboBox_follow")
        self.comboBox_follow.addItem("")
        self.comboBox_follow.addItem("")
        self.comboBox_follow.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_follow)
        self.label_follow = QtWidgets.QLabel(self.groupBox_follow)
        self.label_follow.setStyleSheet("#label_follow:enabled{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.label_follow.setObjectName("label_follow")
        self.horizontalLayout_2.addWidget(self.label_follow)
        self.lineEdit_follow = QtWidgets.QLineEdit(self.groupBox_follow)
        self.lineEdit_follow.setStyleSheet("#lineEdit_follow{\n"
"border-radius: 4px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_follow.setObjectName("lineEdit_follow")
        self.horizontalLayout_2.addWidget(self.lineEdit_follow)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_10.addWidget(self.groupBox_follow)
        self.groupBox_unfollow = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_unfollow.setStyleSheet("#groupBox_unfollow:checked{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.groupBox_unfollow.setCheckable(True)
        self.groupBox_unfollow.setChecked(False)
        self.groupBox_unfollow.setObjectName("groupBox_unfollow")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_unfollow)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_nonfollowers = QtWidgets.QRadioButton(self.groupBox_unfollow)
        self.radioButton_nonfollowers.setStyleSheet("#radioButton_nonfollowers{\n"
"border-radius: 4px;\n"
"\n"
"}")
        self.radioButton_nonfollowers.setChecked(True)
        self.radioButton_nonfollowers.setObjectName("radioButton_nonfollowers")
        self.horizontalLayout_3.addWidget(self.radioButton_nonfollowers)
        self.radioButton_unfollowAll = QtWidgets.QRadioButton(self.groupBox_unfollow)
        self.radioButton_unfollowAll.setStyleSheet("#radioButton_unfollowAll{\n"
"border-radius: 4px;\n"
"}")
        self.radioButton_unfollowAll.setObjectName("radioButton_unfollowAll")
        self.horizontalLayout_3.addWidget(self.radioButton_unfollowAll)
        self.radioButton_restoreFollowing = QtWidgets.QRadioButton(self.groupBox_unfollow)
        self.radioButton_restoreFollowing.setStyleSheet("#radioButton_restoreFollowing{\n"
"border-radius: 4px;\n"
"}")
        self.radioButton_restoreFollowing.setObjectName("radioButton_restoreFollowing")
        self.horizontalLayout_3.addWidget(self.radioButton_restoreFollowing)
        self.verticalLayout_10.addWidget(self.groupBox_unfollow)
        self.groupBox_like = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_like.setStyleSheet("#groupBox_like:checked{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.groupBox_like.setCheckable(True)
        self.groupBox_like.setChecked(False)
        self.groupBox_like.setObjectName("groupBox_like")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_like)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox_like)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet("#label_10:enabled{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.comboBox_like = QtWidgets.QComboBox(self.groupBox_like)
        self.comboBox_like.setObjectName("comboBox_like")
        self.comboBox_like.addItem("")
        self.comboBox_like.addItem("")
        self.comboBox_like.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_like)
        self.label_like = QtWidgets.QLabel(self.groupBox_like)
        self.label_like.setStyleSheet("#label_like:enabled{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.label_like.setObjectName("label_like")
        self.horizontalLayout_8.addWidget(self.label_like)
        self.lineEdit_like = QtWidgets.QLineEdit(self.groupBox_like)
        self.lineEdit_like.setStyleSheet("#lineEdit_like{\n"
"border-radius: 4px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_like.setObjectName("lineEdit_like")
        self.horizontalLayout_8.addWidget(self.lineEdit_like)
        self.label_11 = QtWidgets.QLabel(self.groupBox_like)
        self.label_11.setStyleSheet("#label_11:enabled{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.spinBox_nlikes = QtWidgets.QSpinBox(self.groupBox_like)
        self.spinBox_nlikes.setMaximum(100)
        self.spinBox_nlikes.setProperty("value", 3)
        self.spinBox_nlikes.setObjectName("spinBox_nlikes")
        self.horizontalLayout_8.addWidget(self.spinBox_nlikes)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.verticalLayout_10.addWidget(self.groupBox_like)
        self.groupBox_comment = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_comment.setStyleSheet("#groupBox_comment:checked{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.groupBox_comment.setCheckable(True)
        self.groupBox_comment.setChecked(False)
        self.groupBox_comment.setObjectName("groupBox_comment")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_comment)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.groupBox_comment)
        self.label_12.setStyleSheet("#label_12:enabled{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.comboBox_comment = QtWidgets.QComboBox(self.groupBox_comment)
        self.comboBox_comment.setObjectName("comboBox_comment")
        self.comboBox_comment.addItem("")
        self.comboBox_comment.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_comment)
        self.label_comment = QtWidgets.QLabel(self.groupBox_comment)
        self.label_comment.setStyleSheet("#label_comment:enabled{\n"
"background-color: rgb(204, 229, 255);\n"
"}\n"
"")
        self.label_comment.setObjectName("label_comment")
        self.horizontalLayout_9.addWidget(self.label_comment)
        self.lineEdit_comment = QtWidgets.QLineEdit(self.groupBox_comment)
        self.lineEdit_comment.setStyleSheet("#lineEdit_comment{\n"
"border-radius: 4px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        self.horizontalLayout_9.addWidget(self.lineEdit_comment)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.groupBox_comment)
        self.label_14.setStyleSheet("#label_14:enabled{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        self.lineEdit_commentText = QtWidgets.QLineEdit(self.groupBox_comment)
        self.lineEdit_commentText.setStyleSheet("#lineEdit_commentText{\n"
"border-radius: 4px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_commentText.setObjectName("lineEdit_commentText")
        self.horizontalLayout_10.addWidget(self.lineEdit_commentText)
        self.pushButton_addComment = QtWidgets.QPushButton(self.groupBox_comment)
        self.pushButton_addComment.setStyleSheet("#pushButton_addComment {\n"
"  border: none;\n"
"border-radius: 4px;\n"
"  color: white;\n"
"  padding: 2px 16px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"  transition-duration: 0.4s;\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"#pushButton_addComment {\n"
"  background-color: white; \n"
"  color: #4CAF50; \n"
"  border: 2px solid #4CAF50;\n"
"}\n"
"\n"
"#pushButton_addComment:hover {\n"
"  background-color: #4CAF50;\n"
"  color: white;\n"
"}\n"
"\n"
"#pushButton_addComment:disabled {\n"
"  color: grey;\n"
"    border: 2px solid grey;\n"
"}\n"
"")
        self.pushButton_addComment.setObjectName("pushButton_addComment")
        self.horizontalLayout_10.addWidget(self.pushButton_addComment)
        self.pushButton_delComment = QtWidgets.QPushButton(self.groupBox_comment)
        self.pushButton_delComment.setStyleSheet("#pushButton_delComment {\n"
"  border: none;\n"
"border-radius: 4px;\n"
"  color: white;\n"
"  padding: 2px 16px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"  transition-duration: 0.4s;\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"#pushButton_delComment {\n"
"  background-color: white; \n"
"  color: red; \n"
"  border: 2px solid red;\n"
"}\n"
"\n"
"#pushButton_delComment:hover {\n"
"  background-color: red;\n"
"  color: white;\n"
"}\n"
"\n"
"#pushButton_delComment:disabled {\n"
"  color: grey;\n"
"    border: 2px solid grey;\n"
"}\n"
"")
        self.pushButton_delComment.setObjectName("pushButton_delComment")
        self.horizontalLayout_10.addWidget(self.pushButton_delComment)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.listWidget = QtWidgets.QListWidget(self.groupBox_comment)
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_12.addLayout(self.verticalLayout_2)
        self.verticalLayout_10.addWidget(self.groupBox_comment)
        self.groupBox_combo = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_combo.setStyleSheet("#groupBox_combo:checked{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.groupBox_combo.setCheckable(True)
        self.groupBox_combo.setChecked(False)
        self.groupBox_combo.setObjectName("groupBox_combo")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox_combo)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_13 = QtWidgets.QLabel(self.groupBox_combo)
        self.label_13.setStyleSheet("#label_13:enabled{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_14.addWidget(self.label_13)
        self.spinBox_nlikes_combo = QtWidgets.QSpinBox(self.groupBox_combo)
        self.spinBox_nlikes_combo.setMaximum(100)
        self.spinBox_nlikes_combo.setProperty("value", 1)
        self.spinBox_nlikes_combo.setObjectName("spinBox_nlikes_combo")
        self.horizontalLayout_14.addWidget(self.spinBox_nlikes_combo)
        self.label_15 = QtWidgets.QLabel(self.groupBox_combo)
        self.label_15.setStyleSheet("#label_15:enabled{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15)
        self.comboBox_combo = QtWidgets.QComboBox(self.groupBox_combo)
        self.comboBox_combo.setObjectName("comboBox_combo")
        self.comboBox_combo.addItem("")
        self.comboBox_combo.addItem("")
        self.comboBox_combo.addItem("")
        self.horizontalLayout_14.addWidget(self.comboBox_combo)
        self.label_like_2 = QtWidgets.QLabel(self.groupBox_combo)
        self.label_like_2.setStyleSheet("#label_like_2:enabled{\n"
"background-color: rgb(204, 229, 255);\n"
"}")
        self.label_like_2.setObjectName("label_like_2")
        self.horizontalLayout_14.addWidget(self.label_like_2)
        self.lineEdit_combo = QtWidgets.QLineEdit(self.groupBox_combo)
        self.lineEdit_combo.setStyleSheet("#lineEdit_combo{\n"
"border-radius: 4px;\n"
"border: 1px solid grey;\n"
"}")
        self.lineEdit_combo.setObjectName("lineEdit_combo")
        self.horizontalLayout_14.addWidget(self.lineEdit_combo)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self.verticalLayout_10.addWidget(self.groupBox_combo)
        self.verticalLayout_15.addLayout(self.verticalLayout_10)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_14.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab_home, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_6.addWidget(self.textEdit)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_dashboard = QtWidgets.QWidget()
        self.tab_dashboard.setObjectName("tab_dashboard")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab_dashboard)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_16 = QtWidgets.QLabel(self.tab_dashboard)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_7.addWidget(self.label_16)
        self.lineEdit_followers = QtWidgets.QLineEdit(self.tab_dashboard)
        self.lineEdit_followers.setStyleSheet("border: 2px solid blue;\n"
"border-radius: 4px;")
        self.lineEdit_followers.setText("")
        self.lineEdit_followers.setReadOnly(True)
        self.lineEdit_followers.setObjectName("lineEdit_followers")
        self.verticalLayout_7.addWidget(self.lineEdit_followers)
        self.horizontalLayout_15.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_17 = QtWidgets.QLabel(self.tab_dashboard)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_8.addWidget(self.label_17)
        self.lineEdit_following = QtWidgets.QLineEdit(self.tab_dashboard)
        self.lineEdit_following.setStyleSheet("border: 2px solid blue;\n"
"border-radius: 4px;")
        self.lineEdit_following.setText("")
        self.lineEdit_following.setReadOnly(True)
        self.lineEdit_following.setObjectName("lineEdit_following")
        self.verticalLayout_8.addWidget(self.lineEdit_following)
        self.horizontalLayout_15.addLayout(self.verticalLayout_8)
        self.verticalLayout_12.addLayout(self.horizontalLayout_15)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_dashboard)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_12.addWidget(self.groupBox_2)
        self.progressBar = QtWidgets.QProgressBar(self.tab_dashboard)
        self.progressBar.setProperty("value", 99)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_12.addWidget(self.progressBar)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_update_status = QtWidgets.QPushButton(self.tab_dashboard)
        self.pushButton_update_status.setStyleSheet("#pushButton_update_status {\n"
"  border: none;\n"
"border-radius: 4px;\n"
"  color: white;\n"
"  padding: 2px 16px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"  transition-duration: 0.4s;\n"
"  cursor: pointer;\n"
"}\n"
"\n"
"#pushButton_update_status {\n"
"  background-color: white; \n"
"  color: blue; \n"
"  border: 2px solid blue;\n"
"}\n"
"\n"
"#pushButton_update_status:hover {\n"
"  background-color: blue;\n"
"  color: white;\n"
"}\n"
"\n"
"")
        self.pushButton_update_status.setObjectName("pushButton_update_status")
        self.horizontalLayout_11.addWidget(self.pushButton_update_status)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.tabWidget.addTab(self.tab_dashboard, "")
        self.horizontalLayout_18.addWidget(self.tabWidget)
        self.verticalLayout_11.addLayout(self.horizontalLayout_18)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1193, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.groupBox_combo.clicked['bool'].connect(self.groupBox_unfollow.setChecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Vetogram"))
        self.lineEdit_username.setPlaceholderText(_translate("MainWindow", "username"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "password"))
        self.pushButton_run.setText(_translate("MainWindow", "Start"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.button_testing.setText(_translate("MainWindow", "testing"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Limit Setting Per Day"))
        self.label_4.setText(_translate("MainWindow", "How many account do you want to follow"))
        self.label_6.setText(_translate("MainWindow", "How many account do you want to unfollow"))
        self.label_5.setText(_translate("MainWindow", "How many media do you want to like"))
        self.label_7.setText(_translate("MainWindow", "How many media do you want to comment"))
        self.label_8.setText(_translate("MainWindow", "How many competitor Followers do you want to get "))
        self.label_9.setText(_translate("MainWindow", "How many competitor Following do you want to get"))
        self.radioButton_slow.setText(_translate("MainWindow", "Slow"))
        self.radioButton_standard.setText(_translate("MainWindow", "Standard"))
        self.radioButton_fast.setText(_translate("MainWindow", "Fast"))
        self.groupBox.setTitle(_translate("MainWindow", "Filter Account"))
        self.label_3.setText(_translate("MainWindow", "Tick the box to not follow the account"))
        self.checkBox_private.setText(_translate("MainWindow", "Private Account"))
        self.checkBox_no_profilePic.setText(_translate("MainWindow", "Account Without Profile Picture"))
        self.checkBox_business.setText(_translate("MainWindow", "Business Account"))
        self.checkBox_verified.setText(_translate("MainWindow", "Verified Account"))
        self.groupBox_follow.setTitle(_translate("MainWindow", "Follow Task"))
        self.label_2.setText(_translate("MainWindow", "Follow"))
        self.comboBox_follow.setItemText(0, _translate("MainWindow", "followers"))
        self.comboBox_follow.setItemText(1, _translate("MainWindow", "following"))
        self.comboBox_follow.setItemText(2, _translate("MainWindow", "hashtags"))
        self.label_follow.setText(_translate("MainWindow", "of username"))
        self.lineEdit_follow.setPlaceholderText(_translate("MainWindow", "username1,username2,username3"))
        self.groupBox_unfollow.setTitle(_translate("MainWindow", "Unfollow task"))
        self.radioButton_nonfollowers.setText(_translate("MainWindow", "Unfollow Non Followers"))
        self.radioButton_unfollowAll.setText(_translate("MainWindow", "Unfollow All"))
        self.radioButton_restoreFollowing.setText(_translate("MainWindow", "Restore Following"))
        self.groupBox_like.setTitle(_translate("MainWindow", "Like Task"))
        self.label_10.setText(_translate("MainWindow", "Like media from"))
        self.comboBox_like.setItemText(0, _translate("MainWindow", "followers"))
        self.comboBox_like.setItemText(1, _translate("MainWindow", "following"))
        self.comboBox_like.setItemText(2, _translate("MainWindow", "hashtags"))
        self.label_like.setText(_translate("MainWindow", "of username"))
        self.lineEdit_like.setPlaceholderText(_translate("MainWindow", "username1,username2,username3"))
        self.label_11.setText(_translate("MainWindow", "Amount media="))
        self.groupBox_comment.setTitle(_translate("MainWindow", "Comment Task"))
        self.label_12.setText(_translate("MainWindow", "Comment media from"))
        self.comboBox_comment.setItemText(0, _translate("MainWindow", "my timeline"))
        self.comboBox_comment.setItemText(1, _translate("MainWindow", "hashtags"))
        self.label_comment.setText(_translate("MainWindow", "of username"))
        self.lineEdit_comment.setPlaceholderText(_translate("MainWindow", "my username"))
        self.label_14.setText(_translate("MainWindow", "Add Comments"))
        self.lineEdit_commentText.setPlaceholderText(_translate("MainWindow", "insert your comment"))
        self.pushButton_addComment.setText(_translate("MainWindow", "add"))
        self.pushButton_delComment.setText(_translate("MainWindow", "delete"))
        self.listWidget.setSortingEnabled(True)
        self.groupBox_combo.setTitle(_translate("MainWindow", "Combo Task (follow, like, unfollow)"))
        self.label_13.setText(_translate("MainWindow", "follow and like"))
        self.label_15.setText(_translate("MainWindow", "media of"))
        self.comboBox_combo.setItemText(0, _translate("MainWindow", "followers"))
        self.comboBox_combo.setItemText(1, _translate("MainWindow", "following"))
        self.comboBox_combo.setItemText(2, _translate("MainWindow", "likers"))
        self.label_like_2.setText(_translate("MainWindow", "of username"))
        self.lineEdit_combo.setPlaceholderText(_translate("MainWindow", "only one username"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), _translate("MainWindow", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Log"))
        self.label_16.setText(_translate("MainWindow", "Followers"))
        self.label_17.setText(_translate("MainWindow", "Following"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Follower Growth"))
        self.pushButton_update_status.setText(_translate("MainWindow", "Update Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dashboard), _translate("MainWindow", "Dashboard"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

