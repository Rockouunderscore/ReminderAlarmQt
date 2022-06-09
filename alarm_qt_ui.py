# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alarm_qt_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_timer_settings = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_timer_settings.setGeometry(QtCore.QRect(20, 20, 310, 240))
        self.groupBox_timer_settings.setObjectName("groupBox_timer_settings")
        self.label_input_seconds = QtWidgets.QLabel(self.groupBox_timer_settings)
        self.label_input_seconds.setGeometry(QtCore.QRect(210, 50, 70, 30))
        self.label_input_seconds.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_seconds.setIndent(0)
        self.label_input_seconds.setObjectName("label_input_seconds")
        self.label_input_minutes = QtWidgets.QLabel(self.groupBox_timer_settings)
        self.label_input_minutes.setGeometry(QtCore.QRect(120, 50, 70, 30))
        self.label_input_minutes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_minutes.setIndent(0)
        self.label_input_minutes.setObjectName("label_input_minutes")
        self.label_input_hours = QtWidgets.QLabel(self.groupBox_timer_settings)
        self.label_input_hours.setGeometry(QtCore.QRect(30, 50, 70, 30))
        self.label_input_hours.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_hours.setIndent(0)
        self.label_input_hours.setObjectName("label_input_hours")
        self.spinBox_input_hours = QtWidgets.QSpinBox(self.groupBox_timer_settings)
        self.spinBox_input_hours.setGeometry(QtCore.QRect(30, 80, 70, 30))
        self.spinBox_input_hours.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_input_hours.setObjectName("spinBox_input_hours")
        self.spinBox_input_minutes = QtWidgets.QSpinBox(self.groupBox_timer_settings)
        self.spinBox_input_minutes.setGeometry(QtCore.QRect(120, 80, 70, 30))
        self.spinBox_input_minutes.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_input_minutes.setObjectName("spinBox_input_minutes")
        self.spinBox_input_seconds = QtWidgets.QSpinBox(self.groupBox_timer_settings)
        self.spinBox_input_seconds.setGeometry(QtCore.QRect(210, 80, 70, 30))
        self.spinBox_input_seconds.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_input_seconds.setObjectName("spinBox_input_seconds")
        self.frame_time_remaining = QtWidgets.QFrame(self.groupBox_timer_settings)
        self.frame_time_remaining.setGeometry(QtCore.QRect(50, 140, 210, 60))
        self.frame_time_remaining.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_time_remaining.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_time_remaining.setObjectName("frame_time_remaining")
        self.label_time_remaining = QtWidgets.QLabel(self.frame_time_remaining)
        self.label_time_remaining.setGeometry(QtCore.QRect(10, 10, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_time_remaining.setFont(font)
        self.label_time_remaining.setScaledContents(False)
        self.label_time_remaining.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_remaining.setObjectName("label_time_remaining")
        self.groupBox_timer_actions = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_timer_actions.setGeometry(QtCore.QRect(350, 20, 230, 370))
        self.groupBox_timer_actions.setObjectName("groupBox_timer_actions")
        self.pushButton_start_timer = QtWidgets.QPushButton(self.groupBox_timer_actions)
        self.pushButton_start_timer.setGeometry(QtCore.QRect(40, 90, 150, 40))
        self.pushButton_start_timer.setObjectName("pushButton_start_timer")
        self.pushButton_stop_timer = QtWidgets.QPushButton(self.groupBox_timer_actions)
        self.pushButton_stop_timer.setGeometry(QtCore.QRect(40, 150, 150, 40))
        self.pushButton_stop_timer.setObjectName("pushButton_stop_timer")
        self.pushButton_stop_alarm = QtWidgets.QPushButton(self.groupBox_timer_actions)
        self.pushButton_stop_alarm.setGeometry(QtCore.QRect(40, 210, 150, 40))
        self.pushButton_stop_alarm.setObjectName("pushButton_stop_alarm")
        self.pushButton_repeat = QtWidgets.QPushButton(self.groupBox_timer_actions)
        self.pushButton_repeat.setGeometry(QtCore.QRect(40, 290, 150, 40))
        self.pushButton_repeat.setObjectName("pushButton_repeat")
        self.progressBar_progress_timer = QtWidgets.QProgressBar(self.groupBox_timer_actions)
        self.progressBar_progress_timer.setGeometry(QtCore.QRect(40, 40, 150, 23))
        self.progressBar_progress_timer.setProperty("value", 24)
        self.progressBar_progress_timer.setObjectName("progressBar_progress_timer")
        self.groupBox_longer_time_periods = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_longer_time_periods.setEnabled(False)
        self.groupBox_longer_time_periods.setGeometry(QtCore.QRect(20, 300, 310, 250))
        self.groupBox_longer_time_periods.setTabletTracking(False)
        self.groupBox_longer_time_periods.setAcceptDrops(False)
        self.groupBox_longer_time_periods.setObjectName("groupBox_longer_time_periods")
        self.label_input_days = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.label_input_days.setGeometry(QtCore.QRect(50, 30, 100, 20))
        self.label_input_days.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_days.setIndent(0)
        self.label_input_days.setObjectName("label_input_days")
        self.spinBox_input_days = QtWidgets.QSpinBox(self.groupBox_longer_time_periods)
        self.spinBox_input_days.setGeometry(QtCore.QRect(50, 50, 100, 30))
        self.spinBox_input_days.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_input_days.setObjectName("spinBox_input_days")
        self.spinBox_input_months = QtWidgets.QSpinBox(self.groupBox_longer_time_periods)
        self.spinBox_input_months.setGeometry(QtCore.QRect(50, 100, 100, 30))
        self.spinBox_input_months.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_input_months.setObjectName("spinBox_input_months")
        self.label_input_months = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.label_input_months.setGeometry(QtCore.QRect(50, 80, 100, 20))
        self.label_input_months.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_months.setIndent(0)
        self.label_input_months.setObjectName("label_input_months")
        self.spinBox_input_years = QtWidgets.QSpinBox(self.groupBox_longer_time_periods)
        self.spinBox_input_years.setGeometry(QtCore.QRect(160, 100, 100, 30))
        self.spinBox_input_years.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_input_years.setObjectName("spinBox_input_years")
        self.label_input_weeks = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.label_input_weeks.setGeometry(QtCore.QRect(160, 30, 100, 20))
        self.label_input_weeks.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_weeks.setIndent(0)
        self.label_input_weeks.setObjectName("label_input_weeks")
        self.spinBox_input_weeks = QtWidgets.QSpinBox(self.groupBox_longer_time_periods)
        self.spinBox_input_weeks.setGeometry(QtCore.QRect(160, 50, 100, 30))
        self.spinBox_input_weeks.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_input_weeks.setObjectName("spinBox_input_weeks")
        self.label_input_years = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.label_input_years.setGeometry(QtCore.QRect(160, 80, 100, 20))
        self.label_input_years.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_years.setIndent(0)
        self.label_input_years.setObjectName("label_input_years")
        self.label_remaining_weeks = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.label_remaining_weeks.setGeometry(QtCore.QRect(160, 150, 100, 30))
        self.label_remaining_weeks.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_remaining_weeks.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_remaining_weeks.setTextFormat(QtCore.Qt.AutoText)
        self.label_remaining_weeks.setScaledContents(False)
        self.label_remaining_weeks.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_remaining_weeks.setIndent(12)
        self.label_remaining_weeks.setOpenExternalLinks(False)
        self.label_remaining_weeks.setObjectName("label_remaining_weeks")
        self.label_remaining_years = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.label_remaining_years.setGeometry(QtCore.QRect(160, 190, 100, 30))
        self.label_remaining_years.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_remaining_years.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_remaining_years.setTextFormat(QtCore.Qt.AutoText)
        self.label_remaining_years.setScaledContents(False)
        self.label_remaining_years.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_remaining_years.setIndent(12)
        self.label_remaining_years.setOpenExternalLinks(False)
        self.label_remaining_years.setObjectName("label_remaining_years")
        self.label_remaining_months = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.label_remaining_months.setGeometry(QtCore.QRect(50, 190, 100, 30))
        self.label_remaining_months.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_remaining_months.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_remaining_months.setTextFormat(QtCore.Qt.AutoText)
        self.label_remaining_months.setScaledContents(False)
        self.label_remaining_months.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_remaining_months.setIndent(12)
        self.label_remaining_months.setOpenExternalLinks(False)
        self.label_remaining_months.setObjectName("label_remaining_months")
        self.label_remaining_days = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.label_remaining_days.setGeometry(QtCore.QRect(50, 150, 100, 30))
        self.label_remaining_days.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_remaining_days.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_remaining_days.setTextFormat(QtCore.Qt.AutoText)
        self.label_remaining_days.setScaledContents(False)
        self.label_remaining_days.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_remaining_days.setIndent(12)
        self.label_remaining_days.setOpenExternalLinks(False)
        self.label_remaining_days.setObjectName("label_remaining_days")
        self.groupBox_alarm_settings = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_alarm_settings.setEnabled(False)
        self.groupBox_alarm_settings.setGeometry(QtCore.QRect(350, 430, 230, 120))
        self.groupBox_alarm_settings.setObjectName("groupBox_alarm_settings")
        self.label_alarm_notices = QtWidgets.QLabel(self.groupBox_alarm_settings)
        self.label_alarm_notices.setGeometry(QtCore.QRect(20, 70, 100, 30))
        self.label_alarm_notices.setAlignment(QtCore.Qt.AlignCenter)
        self.label_alarm_notices.setIndent(0)
        self.label_alarm_notices.setObjectName("label_alarm_notices")
        self.spinBox_input_alarm_notices = QtWidgets.QSpinBox(self.groupBox_alarm_settings)
        self.spinBox_input_alarm_notices.setGeometry(QtCore.QRect(120, 70, 90, 31))
        self.spinBox_input_alarm_notices.setObjectName("spinBox_input_alarm_notices")
        self.checkBox_longer_time_periods = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_longer_time_periods.setGeometry(QtCore.QRect(70, 270, 210, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.checkBox_longer_time_periods.setFont(font)
        self.checkBox_longer_time_periods.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.checkBox_longer_time_periods.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_longer_time_periods.setObjectName("checkBox_longer_time_periods")
        self.checkBox_auto_repeat = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_auto_repeat.setGeometry(QtCore.QRect(410, 400, 110, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.checkBox_auto_repeat.setFont(font)
        self.checkBox_auto_repeat.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.checkBox_auto_repeat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_auto_repeat.setObjectName("checkBox_auto_repeat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 29))
        self.menubar.setObjectName("menubar")
        self.appmenu_menu = QtWidgets.QMenu(self.menubar)
        self.appmenu_menu.setObjectName("appmenu_menu")
        self.appmenu_about = QtWidgets.QMenu(self.menubar)
        self.appmenu_about.setObjectName("appmenu_about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.appmenu_menu_quit = QtWidgets.QAction(MainWindow)
        self.appmenu_menu_quit.setObjectName("appmenu_menu_quit")
        self.appmenu_about_creator = QtWidgets.QAction(MainWindow)
        self.appmenu_about_creator.setObjectName("appmenu_about_creator")
        self.menu_about_app = QtWidgets.QAction(MainWindow)
        self.menu_about_app.setObjectName("menu_about_app")
        self.appmenu_menu.addAction(self.appmenu_menu_quit)
        self.appmenu_about.addAction(self.appmenu_about_creator)
        self.appmenu_about.addSeparator()
        self.appmenu_about.addAction(self.menu_about_app)
        self.menubar.addAction(self.appmenu_menu.menuAction())
        self.menubar.addAction(self.appmenu_about.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_timer_settings.setTitle(_translate("MainWindow", "Timer settings"))
        self.label_input_seconds.setText(_translate("MainWindow", "Seconds"))
        self.label_input_minutes.setText(_translate("MainWindow", "Minutes"))
        self.label_input_hours.setText(_translate("MainWindow", "Hours"))
        self.label_time_remaining.setText(_translate("MainWindow", "<html><head/><body><p>00:00:00</p></body></html>"))
        self.groupBox_timer_actions.setTitle(_translate("MainWindow", "Timer Actions"))
        self.pushButton_start_timer.setText(_translate("MainWindow", "Start Timer"))
        self.pushButton_stop_timer.setText(_translate("MainWindow", "Stop Timer"))
        self.pushButton_stop_alarm.setText(_translate("MainWindow", "Stop Alarm"))
        self.pushButton_repeat.setText(_translate("MainWindow", "Repeat"))
        self.groupBox_longer_time_periods.setTitle(_translate("MainWindow", "Longer Periods of Time"))
        self.label_input_days.setText(_translate("MainWindow", "Days"))
        self.label_input_months.setText(_translate("MainWindow", "Months"))
        self.label_input_weeks.setText(_translate("MainWindow", "Weeks"))
        self.label_input_years.setText(_translate("MainWindow", "Years"))
        self.label_remaining_weeks.setText(_translate("MainWindow", "0 Weeks"))
        self.label_remaining_years.setText(_translate("MainWindow", "0 Years"))
        self.label_remaining_months.setText(_translate("MainWindow", "0 Months"))
        self.label_remaining_days.setText(_translate("MainWindow", "0 Days"))
        self.groupBox_alarm_settings.setTitle(_translate("MainWindow", "Alarm Settings"))
        self.label_alarm_notices.setText(_translate("MainWindow", "Alarm notices"))
        self.checkBox_longer_time_periods.setText(_translate("MainWindow", "Enable longer periods of time"))
        self.checkBox_auto_repeat.setToolTip(_translate("MainWindow", "<html><head/><body><p>Will run the alert textEdit_focus_resetter specified amount of times.</p><p>Restarts the timer without clicking \'Repeat\'.</p></body></html>"))
        self.checkBox_auto_repeat.setText(_translate("MainWindow", "Auto Repeat"))
        self.appmenu_menu.setTitle(_translate("MainWindow", "Menu"))
        self.appmenu_about.setTitle(_translate("MainWindow", "About"))
        self.appmenu_menu_quit.setText(_translate("MainWindow", "Quit"))
        self.appmenu_about_creator.setText(_translate("MainWindow", "Creator"))
        self.menu_about_app.setText(_translate("MainWindow", "App"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
