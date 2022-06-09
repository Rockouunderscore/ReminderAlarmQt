import sys
from time import sleep

from PyQt5 import QtCore, QtGui, QtTest
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow

from Clock_Data import ClockQt
from alarm_qt_window_params import *


# noinspection DuplicatedCode
class AlarmMainWindow(QMainWindow):
    c: ClockQt

    # %%

    textEdit_focus_resetter: QtWidgets.QTextEdit

    centralwidget: QtWidgets.QWidget

    #

    groupBox_timer_settings: QtWidgets.QGroupBox

    label_input_seconds: QtWidgets.QLabel
    label_input_minutes: QtWidgets.QLabel
    label_input_hours: QtWidgets.QLabel

    spinBox_input_seconds: QtWidgets.QSpinBox
    spinBox_input_minutes: QtWidgets.QSpinBox
    spinBox_input_hours: QtWidgets.QSpinBox

    frame_time_remaining: QtWidgets.QFrame
    label_time_remaining: QtWidgets.QLabel

    #

    groupBox_timer_actions: QtWidgets.QGroupBox
    progressBar_progress_timer: QtWidgets.QProgressBar
    pushButton_start_timer: QtWidgets.QPushButton
    pushButton_pause_timer: QtWidgets.QPushButton
    pushButton_stop_alarm: QtWidgets.QPushButton
    pushButton_stop: QtWidgets.QPushButton

    #

    groupBox_longer_time_periods: QtWidgets.QGroupBox

    label_input_days: QtWidgets.QLabel
    spinBox_input_days: QtWidgets.QSpinBox
    label_input_months: QtWidgets.QLabel
    spinBox_input_months: QtWidgets.QSpinBox
    label_input_weeks: QtWidgets.QLabel
    spinBox_input_weeks: QtWidgets.QSpinBox
    label_input_years: QtWidgets.QLabel
    spinBox_input_years: QtWidgets.QSpinBox

    label_remaining_days: QtWidgets.QLabel
    label_remaining_weeks: QtWidgets.QLabel
    label_remaining_months: QtWidgets.QLabel
    label_remaining_years: QtWidgets.QLabel

    #

    groupBox_alarm_settings: QtWidgets.QGroupBox
    label_alarm_notices: QtWidgets.QLabel
    spinBox_input_alarm_notices: QtWidgets.QSpinBox

    #

    checkBox_longer_time_periods: QtWidgets.QCheckBox

    pushButton_reset_timers_values: QtWidgets.QPushButton

    checkBox_auto_repeat: QtWidgets.QCheckBox

    #

    menubar: QtWidgets.QMenuBar

    appmenu_menu: QtWidgets.QMenu

    appmenu_menu_quit: QtWidgets.QAction

    appmenu_about: QtWidgets.QMenu

    appmenu_about_creator: QtWidgets.QAction

    appmenu_about_app: QtWidgets.QAction

    #

    statusbar: QtWidgets.QStatusBar

    # %%

    def __init__(self):
        super(AlarmMainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.setFixedSize(window_width, window_height)

        self.setWindowTitle(app_name)

        self.setWindowIcon(app_icon)

        self.setup_ui()

        self.setup_events()

        self.c = ClockQt()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.c.reset_clock()

    def create_ui_widgets(self):
        self.centralwidget = QtWidgets.QWidget(self)

        #

        #

        self.groupBox_timer_settings = QtWidgets.QGroupBox(self.centralwidget)
        self.label_input_seconds = QtWidgets.QLabel(self.groupBox_timer_settings)
        self.spinBox_input_seconds = QtWidgets.QSpinBox(self.groupBox_timer_settings)
        self.label_input_minutes = QtWidgets.QLabel(self.groupBox_timer_settings)
        self.spinBox_input_minutes = QtWidgets.QSpinBox(self.groupBox_timer_settings)
        self.label_input_hours = QtWidgets.QLabel(self.groupBox_timer_settings)
        self.spinBox_input_hours = QtWidgets.QSpinBox(self.groupBox_timer_settings)
        self.frame_time_remaining = QtWidgets.QFrame(self.groupBox_timer_settings)
        self.label_time_remaining = QtWidgets.QLabel(self.frame_time_remaining)

        #

        self.groupBox_timer_actions = QtWidgets.QGroupBox(self.centralwidget)
        self.progressBar_progress_timer = QtWidgets.QProgressBar(self.groupBox_timer_actions)
        self.pushButton_start_timer = QtWidgets.QPushButton(self.groupBox_timer_actions)
        self.pushButton_pause_timer = QtWidgets.QPushButton(self.groupBox_timer_actions)
        self.pushButton_stop_alarm = QtWidgets.QPushButton(self.groupBox_timer_actions)
        self.pushButton_stop = QtWidgets.QPushButton(self.groupBox_timer_actions)

        #

        self.groupBox_longer_time_periods = QtWidgets.QGroupBox(self.centralwidget)
        self.label_input_days = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.spinBox_input_days = QtWidgets.QSpinBox(self.groupBox_longer_time_periods)
        self.label_input_months = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.spinBox_input_months = QtWidgets.QSpinBox(self.groupBox_longer_time_periods)
        self.label_input_weeks = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.spinBox_input_weeks = QtWidgets.QSpinBox(self.groupBox_longer_time_periods)
        self.label_input_years = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.spinBox_input_years = QtWidgets.QSpinBox(self.groupBox_longer_time_periods)
        self.label_remaining_days = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.label_remaining_weeks = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.label_remaining_months = QtWidgets.QLabel(self.groupBox_longer_time_periods)
        self.label_remaining_years = QtWidgets.QLabel(self.groupBox_longer_time_periods)

        #

        self.groupBox_alarm_settings = QtWidgets.QGroupBox(self.centralwidget)
        self.label_alarm_notices = QtWidgets.QLabel(self.groupBox_alarm_settings)
        self.spinBox_input_alarm_notices = QtWidgets.QSpinBox(self.groupBox_alarm_settings)

        #

        self.checkBox_longer_time_periods = QtWidgets.QCheckBox(self.centralwidget)

        self.pushButton_reset_timers_values = QtWidgets.QPushButton(self.centralwidget)

        #

        self.checkBox_auto_repeat = QtWidgets.QCheckBox(self.centralwidget)

        #

        self.menubar = QtWidgets.QMenuBar(self)

        self.appmenu_menu = QtWidgets.QMenu(self.menubar)
        self.appmenu_menu_quit = QtWidgets.QAction(self)

        self.appmenu_about = QtWidgets.QMenu(self.menubar)
        self.appmenu_about_creator = QtWidgets.QAction(self)
        self.appmenu_about_app = QtWidgets.QAction(self)

        self.statusbar = QtWidgets.QStatusBar(self)

    def set_geometry(self):
        self.setGeometry(window_xpos, window_ypos, window_width, window_height)

        #

        #

        self.groupBox_timer_settings.setGeometry(QtCore.QRect(20, 20, 310, 240))

        self.label_input_seconds.setGeometry(QtCore.QRect(210, 50, 70, 30))
        self.spinBox_input_seconds.setGeometry(QtCore.QRect(210, 80, 70, 30))
        self.label_input_minutes.setGeometry(QtCore.QRect(120, 50, 70, 30))

        self.spinBox_input_minutes.setGeometry(QtCore.QRect(120, 80, 70, 30))
        self.label_input_hours.setGeometry(QtCore.QRect(30, 50, 70, 30))
        self.spinBox_input_hours.setGeometry(QtCore.QRect(30, 80, 70, 30))

        self.frame_time_remaining.setGeometry(QtCore.QRect(50, 140, 210, 60))
        self.label_time_remaining.setGeometry(QtCore.QRect(10, 10, 190, 40))

        #

        self.checkBox_longer_time_periods.setGeometry(QtCore.QRect(25, 270, 210, 20))
        self.pushButton_reset_timers_values.setGeometry(QtCore.QRect(235, 265, 90, 30))

        #

        self.groupBox_longer_time_periods.setGeometry(QtCore.QRect(20, 300, 310, 250))
        self.label_input_days.setGeometry(QtCore.QRect(50, 30, 100, 20))
        self.spinBox_input_days.setGeometry(QtCore.QRect(50, 50, 100, 30))
        self.label_input_months.setGeometry(QtCore.QRect(50, 80, 100, 20))
        self.spinBox_input_months.setGeometry(QtCore.QRect(50, 100, 100, 30))
        self.label_input_weeks.setGeometry(QtCore.QRect(160, 30, 100, 20))
        self.spinBox_input_weeks.setGeometry(QtCore.QRect(160, 50, 100, 30))
        self.label_input_years.setGeometry(QtCore.QRect(160, 80, 100, 20))
        self.spinBox_input_years.setGeometry(QtCore.QRect(160, 100, 100, 30))
        self.label_remaining_days.setGeometry(QtCore.QRect(50, 150, 100, 30))
        self.label_remaining_weeks.setGeometry(QtCore.QRect(160, 150, 100, 30))
        self.label_remaining_months.setGeometry(QtCore.QRect(50, 190, 100, 30))
        self.label_remaining_years.setGeometry(QtCore.QRect(160, 190, 100, 30))

        #

        self.checkBox_auto_repeat.setGeometry(QtCore.QRect(410, 400, 110, 20))

        #

        self.groupBox_timer_actions.setGeometry(QtCore.QRect(350, 20, 230, 370))
        self.progressBar_progress_timer.setGeometry(QtCore.QRect(40, 40, 150, 25))
        self.pushButton_start_timer.setGeometry(QtCore.QRect(40, 90, 150, 40))
        self.pushButton_pause_timer.setGeometry(QtCore.QRect(40, 150, 150, 40))
        self.pushButton_stop_alarm.setGeometry(QtCore.QRect(40, 210, 150, 40))
        self.pushButton_stop.setGeometry(QtCore.QRect(40, 290, 150, 40))

        #

        self.groupBox_alarm_settings.setGeometry(QtCore.QRect(350, 430, 230, 120))
        self.label_alarm_notices.setGeometry(QtCore.QRect(20, 70, 100, 30))
        self.spinBox_input_alarm_notices.setGeometry(QtCore.QRect(120, 70, 90, 30))

        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 30))

    def set_object_name(self):
        self.setObjectName("MainWindow")

        self.centralwidget.setObjectName("centralwidget")

        self.groupBox_timer_settings.setObjectName("groupBox_timer_settings")
        self.label_input_seconds.setObjectName("label_input_seconds")
        self.spinBox_input_seconds.setObjectName("spinBox_input_seconds")
        self.label_input_minutes.setObjectName("label_input_minutes")
        self.spinBox_input_minutes.setObjectName("spinBox_input_minutes")
        self.label_input_hours.setObjectName("label_input_hours")
        self.spinBox_input_hours.setObjectName("spinBox_input_hours")
        self.frame_time_remaining.setObjectName("frame_time_remaining")
        self.label_time_remaining.setObjectName("label_time_remaining")
        self.groupBox_timer_actions.setObjectName("groupBox_timer_actions")
        self.progressBar_progress_timer.setObjectName("progressBar_progress_timer")
        self.pushButton_start_timer.setObjectName("pushButton_start_timer")
        self.pushButton_pause_timer.setObjectName("pushButton_stop_timer")
        self.pushButton_stop_alarm.setObjectName("pushButton_stop_alarm")
        self.pushButton_stop.setObjectName("pushButton_repeat")
        self.groupBox_longer_time_periods.setObjectName("groupBox_longer_time_periods")
        self.label_input_days.setObjectName("label_input_days")
        self.spinBox_input_days.setObjectName("spinBox_input_days")
        self.label_input_months.setObjectName("label_input_months")
        self.spinBox_input_months.setObjectName("spinBox_input_months")
        self.label_input_weeks.setObjectName("label_input_weeks")
        self.spinBox_input_weeks.setObjectName("spinBox_input_weeks")
        self.label_input_years.setObjectName("label_input_years")
        self.spinBox_input_years.setObjectName("spinBox_input_years")
        self.label_remaining_days.setObjectName("label_remaining_days")
        self.label_remaining_weeks.setObjectName("label_remaining_weeks")
        self.label_remaining_months.setObjectName("label_remaining_months")
        self.label_remaining_years.setObjectName("label_remaining_years")
        self.groupBox_alarm_settings.setObjectName("groupBox_alarm_settings")
        self.label_alarm_notices.setObjectName("label_alarm_notices")
        self.spinBox_input_alarm_notices.setObjectName("spinBox_input_alarm_notices")
        self.checkBox_longer_time_periods.setObjectName("checkBox_longer_time_periods")
        self.checkBox_auto_repeat.setObjectName("checkBox_auto_repeat")
        self.menubar.setObjectName("menubar")
        self.appmenu_menu.setObjectName("appmenu_menu")
        self.appmenu_menu_quit.setObjectName("appmenu_menu_quit")
        self.appmenu_about.setObjectName("appmenu_about")
        self.appmenu_about_creator.setObjectName("appmenu_about_creator")
        self.appmenu_about_app.setObjectName("menu_about_app")
        self.statusbar.setObjectName("statusbar")

    def set_font(self):
        label_time_remaining_font = QtGui.QFont()
        label_time_remaining_font.setPointSize(14)
        self.label_time_remaining.setFont(label_time_remaining_font)

        check_box_longer_time_periods_font = QtGui.QFont()
        check_box_longer_time_periods_font.setBold(False)
        check_box_longer_time_periods_font.setItalic(False)
        check_box_longer_time_periods_font.setUnderline(False)
        check_box_longer_time_periods_font.setWeight(50)
        check_box_longer_time_periods_font.setStrikeOut(False)
        self.checkBox_longer_time_periods.setFont(check_box_longer_time_periods_font)

        check_box_auto_repeat_font = QtGui.QFont()
        check_box_auto_repeat_font.setBold(False)
        check_box_auto_repeat_font.setItalic(False)
        check_box_auto_repeat_font.setUnderline(False)
        check_box_auto_repeat_font.setWeight(50)
        check_box_auto_repeat_font.setStrikeOut(False)
        self.checkBox_auto_repeat.setFont(check_box_auto_repeat_font)

    def set_input_method_hints(self):
        self.spinBox_input_seconds.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_input_minutes.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_input_hours.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_input_days.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_input_months.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_input_weeks.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_input_years.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)

    def set_alignment(self):
        self.label_input_seconds.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_minutes.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_hours.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_remaining.setAlignment(QtCore.Qt.AlignCenter)

        self.label_input_days.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_months.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_weeks.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input_years.setAlignment(QtCore.Qt.AlignCenter)

        self.label_remaining_days.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_remaining_weeks.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_remaining_months.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_remaining_years.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        self.label_alarm_notices.setAlignment(QtCore.Qt.AlignCenter)

    def set_indent(self):
        self.label_remaining_days.setIndent(20)
        self.label_remaining_weeks.setIndent(20)
        self.label_remaining_months.setIndent(20)
        self.label_remaining_years.setIndent(20)

    def set_frame_shape(self):
        self.frame_time_remaining.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.label_remaining_days.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_remaining_weeks.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_remaining_months.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_remaining_years.setFrameShape(QtWidgets.QFrame.StyledPanel)

    def set_frame_shadow(self):
        self.frame_time_remaining.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label_remaining_days.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_remaining_weeks.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_remaining_months.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_remaining_years.setFrameShadow(QtWidgets.QFrame.Raised)

    def set_scaled_contents(self):
        self.label_time_remaining.setScaledContents(False)

        self.label_remaining_days.setScaledContents(False)
        self.label_remaining_weeks.setScaledContents(False)
        self.label_remaining_months.setScaledContents(False)
        self.label_remaining_years.setScaledContents(False)

    def set_text_format(self):
        self.label_remaining_days.setTextFormat(QtCore.Qt.AutoText)
        self.label_remaining_weeks.setTextFormat(QtCore.Qt.AutoText)
        self.label_remaining_months.setTextFormat(QtCore.Qt.AutoText)
        self.label_remaining_years.setTextFormat(QtCore.Qt.AutoText)

    def set_others(self):
        self.setCentralWidget(self.centralwidget)
        self.setMenuBar(self.menubar)

        self.progressBar_progress_timer.setProperty("value", 0)
        self.progressBar_progress_timer.setTextVisible(False)

        self.groupBox_longer_time_periods.setEnabled(False)
        self.groupBox_alarm_settings.setEnabled(False)

        self.checkBox_longer_time_periods.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_auto_repeat.setLayoutDirection(QtCore.Qt.LeftToRight)

        #

        self.appmenu_menu.addAction(self.appmenu_menu_quit)

        self.appmenu_about.addSeparator()

        self.appmenu_about.addAction(self.appmenu_about_app)

        self.appmenu_about.addAction(self.appmenu_about_creator)

        self.menubar.addAction(self.appmenu_menu.menuAction())
        self.menubar.addAction(self.appmenu_about.menuAction())

        self.setStatusBar(self.statusbar)

        self.set_text()
        QtCore.QMetaObject.connectSlotsByName(self)

    def setup_ui(self):

        self.create_ui_widgets()

        self.set_geometry()
        # self.set_object_name()
        self.set_font()
        # self.set_input_method_hints()
        self.set_alignment()
        self.set_indent()
        self.set_frame_shape()
        self.set_frame_shadow()
        self.set_others()
        self.set_text()

    def set_text(self):

        # Set Window name

        self.setWindowTitle(app_name)

        # Timer Settings

        self.groupBox_timer_settings.setTitle("Timer settings")
        self.label_input_seconds.setText("Seconds")
        self.label_input_minutes.setText("Minutes")
        self.label_input_hours.setText("Hours")
        self.label_time_remaining.setText("<html><head/><body><p>00:00:00</p></body></html>")

        # Longer Periods of time

        self.checkBox_longer_time_periods.setText("Enable longer periods of time")
        self.groupBox_longer_time_periods.setTitle("Longer Periods of Time")

        self.pushButton_reset_timers_values.setText("Reset Timers")

        self.label_input_days.setText("Days")
        self.label_input_months.setText("Months")
        self.label_input_weeks.setText("Weeks")
        self.label_input_years.setText("Years")

        self.label_remaining_weeks.setText("0 Weeks")
        self.label_remaining_years.setText("0 Years")
        self.label_remaining_months.setText("0 Months")
        self.label_remaining_days.setText("0 Days")

        # Timer Actions

        self.groupBox_timer_actions.setTitle("Timer Actions")
        self.pushButton_start_timer.setText("Start Timer")
        self.pushButton_pause_timer.setText("Pause Timer")
        self.pushButton_stop_alarm.setText("Stop Alarm")
        self.pushButton_stop.setText("Reset Clock")

        # Auto Repeat / Alarm Settings

        self.checkBox_auto_repeat.setToolTip(
            "<html><head/><body>"
            "<p>Will run the alert textEdit_focus_resetter specified amount of times.</p>"
            "<p>Restarts the timer without clicking \'Repeat\'.</p>"
            "</body></html>"
        )
        self.checkBox_auto_repeat.setText("Auto Repeat")

        self.groupBox_alarm_settings.setTitle("Alarm Settings")
        self.label_alarm_notices.setText("Alarm notices")

        self.appmenu_menu.setTitle("Menu")
        self.appmenu_menu_quit.setText("Quit")

        self.appmenu_about.setTitle("About")
        self.appmenu_about_creator.setText("Creator")
        self.appmenu_about_app.setText("App")

    def setup_events(self):
        self.setup_spin_boxes_events()
        self.setup_check_boxes_events()
        self.setup_push_button_events()

    #

    def setup_spin_boxes_events(self):
        self.pushButton_start_timer.setDisabled(True)
        self.pushButton_pause_timer.setDisabled(True)
        self.pushButton_stop_alarm.setDisabled(True)
        self.pushButton_stop.setDisabled(True)

        self.spinBox_input_seconds.setMaximum(60)
        self.spinBox_input_minutes.setMaximum(60)
        self.spinBox_input_hours.setMaximum(24)
        self.spinBox_input_days.setMaximum(7)
        self.spinBox_input_weeks.setMaximum(4)
        self.spinBox_input_months.setMaximum(12)
        self.spinBox_input_years.setMaximum(999)

        self.spinBox_input_alarm_notices.setMaximum(999)

        #

        self.spinBox_input_seconds.setMinimum(-1)
        self.spinBox_input_minutes.setMinimum(-1)
        self.spinBox_input_hours.setMinimum(-1)
        self.spinBox_input_days.setMinimum(-1)
        self.spinBox_input_weeks.setMinimum(-1)
        self.spinBox_input_months.setMinimum(-1)
        self.spinBox_input_years.setMinimum(-1)

        self.spinBox_input_alarm_notices.setMinimum(1)

        #

        self.spinBox_input_seconds.valueChanged.connect(self.spin_box_input_timer_update)
        self.spinBox_input_minutes.valueChanged.connect(self.spin_box_input_timer_update)
        self.spinBox_input_hours.valueChanged.connect(self.spin_box_input_timer_update)
        self.spinBox_input_days.valueChanged.connect(self.spin_box_input_timer_update)
        self.spinBox_input_weeks.valueChanged.connect(self.spin_box_input_timer_update)
        self.spinBox_input_months.valueChanged.connect(self.spin_box_input_timer_update)
        self.spinBox_input_years.valueChanged.connect(self.spin_box_input_timer_update)

        # self.spinBox_input_alarm_notices.valueChanged.connect(self.spin_box_input_alarm_notices_update)

    valid_times: bool = False

    def spin_box_input_timer_update(self):

        if self.spinBox_input_seconds.value() == self.spinBox_input_seconds.maximum() and \
                not self.spinBox_input_minutes.value() == self.spinBox_input_minutes.maximum():
            self.spinBox_input_seconds.setValue(0)
            self.spinBox_input_minutes.setValue(self.spinBox_input_minutes.value() + 1)

        if self.spinBox_input_minutes.value() == self.spinBox_input_minutes.maximum() and \
                not self.spinBox_input_hours.value() == self.spinBox_input_hours.maximum():
            self.spinBox_input_minutes.setValue(0)
            self.spinBox_input_hours.setValue(self.spinBox_input_hours.value() + 1)

        if self.spinBox_input_hours.value() == self.spinBox_input_hours.maximum() and \
                not self.spinBox_input_days.value() == self.spinBox_input_days.maximum():
            self.spinBox_input_hours.setValue(0)
            self.spinBox_input_days.setValue(self.spinBox_input_days.value() + 1)

        if self.spinBox_input_days.value() == self.spinBox_input_days.maximum() and \
                not self.spinBox_input_weeks.value() == self.spinBox_input_weeks.maximum():
            self.spinBox_input_days.setValue(0)
            self.spinBox_input_weeks.setValue(self.spinBox_input_weeks.value() + 1)

        if self.spinBox_input_weeks.value() == self.spinBox_input_weeks.maximum() and \
                not self.spinBox_input_months.value() == self.spinBox_input_months.maximum():
            self.spinBox_input_weeks.setValue(0)
            self.spinBox_input_months.setValue(self.spinBox_input_months.value() + 1)

        if self.spinBox_input_months.value() == self.spinBox_input_months.maximum() and \
                not self.spinBox_input_years.value() == self.spinBox_input_years.maximum():
            self.spinBox_input_months.setValue(0)
            self.spinBox_input_years.setValue(self.spinBox_input_years.value() + 1)

        #

        if self.spinBox_input_seconds.value() < 0:
            self.spinBox_input_seconds.setValue(self.spinBox_input_seconds.maximum() - 1)
            if self.spinBox_input_minutes.value() > 0:
                self.spinBox_input_minutes.setValue(self.spinBox_input_minutes.value() - 1)
            else:
                self.spinBox_input_minutes.setValue(0)

        if self.spinBox_input_minutes.value() < 0:
            self.spinBox_input_minutes.setValue(self.spinBox_input_minutes.maximum() - 1)
            if self.spinBox_input_hours.value() > 0:
                self.spinBox_input_hours.setValue(self.spinBox_input_hours.value() - 1)
            else:
                self.spinBox_input_hours.setValue(0)

        if self.spinBox_input_hours.value() < 0:
            self.spinBox_input_hours.setValue(self.spinBox_input_hours.maximum() - 1)
            if self.spinBox_input_days.value() > 0:
                self.spinBox_input_days.setValue(self.spinBox_input_days.value() - 1)
            else:
                self.spinBox_input_days.setValue(0)

        if self.spinBox_input_days.value() < 0:
            self.spinBox_input_days.setValue(self.spinBox_input_days.maximum() - 1)
            if self.spinBox_input_weeks.value() > 0:
                self.spinBox_input_weeks.setValue(self.spinBox_input_weeks.value() - 1)
            else:
                self.spinBox_input_weeks.setValue(0)

        if self.spinBox_input_weeks.value() < 0:
            self.spinBox_input_weeks.setValue(self.spinBox_input_weeks.maximum() - 1)
            if self.spinBox_input_months.value() > 0:
                self.spinBox_input_months.setValue(self.spinBox_input_months.value() - 1)
            else:
                self.spinBox_input_months.setValue(0)

        if self.spinBox_input_months.value() < 0:
            self.spinBox_input_months.setValue(self.spinBox_input_months.maximum() - 1)
            if self.spinBox_input_years.value() > 0:
                self.spinBox_input_years.setValue(self.spinBox_input_years.value() - 1)
            else:
                self.spinBox_input_years.setValue(0)

        if self.spinBox_input_years.value() < 0:
            self.spinBox_input_years.setValue(1)

        if self.spinBox_input_days.value() > 0 or \
                self.spinBox_input_weeks.value() > 0 or \
                self.spinBox_input_months.value() > 0 or \
                self.spinBox_input_years.value() > 0 or \
                self.checkBox_longer_time_periods.isChecked():
            self.checkBox_longer_time_periods.setChecked(True)

        self.pushButton_start_timer.setEnabled(sum([
            self.spinBox_input_seconds.value(),
            self.spinBox_input_minutes.value(),
            self.spinBox_input_hours.value(),
            self.spinBox_input_days.value(),
            self.spinBox_input_weeks.value(),
            self.spinBox_input_months.value(),
            self.spinBox_input_years.value()
        ]) > 0)

    #

    def setup_check_boxes_events(self):
        self.checkBox_longer_time_periods.stateChanged.connect(self.check_box_longer_time_periods_update)
        self.checkBox_auto_repeat.stateChanged.connect(self.check_box_auto_repeat_update)

    def check_box_longer_time_periods_update(self):
        self.groupBox_longer_time_periods.setEnabled(self.checkBox_longer_time_periods.isChecked())

        if not self.checkBox_longer_time_periods.isChecked():
            self.spinBox_input_days.setValue(0)
            self.spinBox_input_weeks.setValue(0)
            self.spinBox_input_months.setValue(0)
            self.spinBox_input_years.setValue(0)

    def check_box_auto_repeat_update(self):
        self.groupBox_alarm_settings.setEnabled(self.checkBox_auto_repeat.isChecked())

    #

    def setup_push_button_events(self):
        self.pushButton_reset_timers_values.clicked.connect(self.push_button_reset_timers_values_trigger)
        self.pushButton_start_timer.clicked.connect(self.push_button_start_timer_trigger)
        self.pushButton_pause_timer.clicked.connect(self.push_button_pause_timer_trigger)
        self.pushButton_stop_alarm.clicked.connect(self.push_button_stop_alarm_trigger)
        self.pushButton_stop.clicked.connect(self.push_button_reset_clock)

    def push_button_reset_timers_values_trigger(self):
        self.spinBox_input_seconds.setValue(0)
        self.spinBox_input_minutes.setValue(0)
        self.spinBox_input_hours.setValue(0)

        self.spinBox_input_days.setValue(0)
        self.spinBox_input_weeks.setValue(0)
        self.spinBox_input_months.setValue(0)
        self.spinBox_input_years.setValue(0)

    def push_button_start_timer_trigger(self):

        if self.c.time == 0:
            time: list[int] = []

            time.append(self.spinBox_input_seconds.value())
            time.append(self.spinBox_input_minutes.value())
            time.append(self.spinBox_input_hours.value())
            time.append(self.spinBox_input_days.value())
            time.append(self.spinBox_input_weeks.value())
            time.append(self.spinBox_input_months.value())
            time.append(self.spinBox_input_years.value())

            if sum(time) <= 0:
                return

            self.disable_inputs(True)

            self.c.set_time(time)

            self.c.set_window_widgets(window=self)

            self.c.start_clock()
        else:
            self.c.repeat_clock()

    def push_button_pause_timer_trigger(self):
        self.c.pause_timer()

    def push_button_stop_alarm_trigger(self):
        self.c.stop_alarm()

    def push_button_reset_clock(self):
        self.c.stop_reset_clock()
        self.disable_inputs(False)

    #

    def disable_inputs(self, disabled: bool = True):

        self.spinBox_input_seconds.setReadOnly(disabled)
        self.spinBox_input_minutes.setReadOnly(disabled)
        self.spinBox_input_hours.setReadOnly(disabled)
        self.spinBox_input_days.setReadOnly(disabled)
        self.spinBox_input_weeks.setReadOnly(disabled)
        self.spinBox_input_months.setReadOnly(disabled)
        self.spinBox_input_years.setReadOnly(disabled)

        self.spinBox_input_alarm_notices.setReadOnly(disabled)

        self.pushButton_reset_timers_values.setDisabled(disabled)

        self.checkBox_longer_time_periods.setDisabled(disabled)

        self.checkBox_auto_repeat.setDisabled(disabled)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    AlarmMainWindow = AlarmMainWindow()

    AlarmMainWindow.show()

    sys.exit(app.exec_())
