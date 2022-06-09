import multiprocessing

from PyQt5 import QtWidgets, QtCore, QtTest
from PyQt5.QtCore import QMetaObject, Q_ARG, Qt


# noinspection DuplicatedCode
# from alarm_qt import AlarmMainWindow
from PyQt5.QtMultimedia import QSound


class ClockQt:

    remaining_time: int
    time: int

    timer_started: bool
    timer_paused: bool

    alarm_running: bool
    alarm_force_stop: bool

    force_stop: bool
    auto_repeat: int

    #

    alarm_sound_player: QSound

    display_timer: QtWidgets.QLabel
    display_days: QtWidgets.QLabel
    display_weeks: QtWidgets.QLabel
    display_months: QtWidgets.QLabel
    display_years: QtWidgets.QLabel
    display_progressbar: QtWidgets.QProgressBar

    button_start_repeat: QtWidgets.QPushButton
    button_pause_resume: QtWidgets.QPushButton
    button_stop_alarm: QtWidgets.QPushButton
    button_reset_clock: QtWidgets.QPushButton

    def __init__(self):
        self.alarm_sound_player = QSound("./alarm.wav")
        self.reset_clock()

    def set_time(self, times: list[int]):

        _time = 0

        _time += times[0] * 1
        _time += times[1] * 60
        _time += times[2] * 3600
        _time += times[3] * 86400
        _time += times[4] * 604800
        _time += times[5] * 2629800
        _time += times[6] * 31557600

        self.time = _time
        self.remaining_time = _time

    def reset_clock(self, full=True):
        if full:
            self.time = 0
            self.remaining_time = 0
            self.auto_repeat = 0
            self.force_stop = True
            self.timer_started = False
        else:
            self.timer_started = True
            self.force_stop = False
        self.timer_paused = False
        self.alarm_running = False
        self.alarm_force_stop = False

    def set_window_widgets(self, window):

        self.display_timer = window.label_time_remaining
        self.display_days = window.label_remaining_days
        self.display_weeks = window.label_remaining_weeks
        self.display_months = window.label_remaining_months
        self.display_years = window.label_remaining_years
        self.display_progressbar = window.progressBar_progress_timer

        self.button_start_repeat = window.pushButton_start_timer
        self.button_pause_resume = window.pushButton_pause_timer
        self.button_stop_alarm = window.pushButton_stop_alarm
        self.button_reset_clock = window.pushButton_stop

        self.auto_repeat = window.spinBox_input_alarm_notices.value() if window.checkBox_auto_repeat.isChecked() else 0

    def update_window(self):
        self.update_displays()
        self.update_buttons()

    def update_displays(self):

        intervals = [
            ('Years', 31557600),
            # 60 * 60 * 24 * 7 * 4.34821428571 * 12
            # 60 * 60 * 24 * 365.25

            ('Months', 2629800),
            # 60 * 60 * 24 * 7 * 4.34821428571 = 2629800
            # 60 * 60 * 24 * 30.4375

            ('Weeks', 604800),
            # 60 * 60 * 24 * 7

            ('Days', 86400),
            # 60 * 60 * 24

            ('Hours', 3600),
            # 60 * 60

            ('Minutes', 60),
            # 60

            ('Seconds', 1),
            # 1
        ]

        time: dict[str, str] = {}

        time_to_format = self.remaining_time

        for name, count in intervals:

            name = name.lower()

            value = time_to_format // count

            if value:
                time_to_format -= value * count

            if count <= 3600:
                time[name] = f"0{value}"
                if value > 10:
                    time[name] = f"{value}"
            if count > 3600:
                time[name] = f"{value} {name}"
                if value == 1:
                    time[name] = f"{value} {name[:-1]}"

        self.display_timer.setText(f"{time['hours']}:"
                                   f"{time['minutes']}:"
                                   f"{time['seconds']}")

        self.display_days.setText(f"{time['days']}")
        self.display_weeks.setText(f"{time['weeks']}")
        self.display_months.setText(f"{time['months']}")
        self.display_years.setText(f"{time['years']}")

        self.display_progressbar.setValue(
            round(abs((self.remaining_time / self.time) * 100 - 100)) if self.time != 0 else 0
        )

    def update_buttons(self):
        self.button_start_repeat.setDisabled(
            self.timer_started
        )
        self.button_start_repeat.setText(
            "Repeat Timer" if self.time != 0 else "Start Timer"
        )
        self.button_pause_resume.setEnabled(
            self.timer_started
        )
        self.button_pause_resume.setText(
            "Resume Timer" if self.timer_paused else "Pause Timer"
        )
        self.button_stop_alarm.setEnabled(
            self.alarm_running and not self.alarm_force_stop
        )
        self.button_reset_clock.setEnabled(
            self.time != 0
        )

    def start_clock(self):

        self.reset_clock(False)

        self.timer_loop()

    def repeat_clock(self):
        self.remaining_time = self.time

        self.start_clock()

    def timer_loop(self):

        while not self.force_stop:

            self.update_window()

            while self.remaining_time > 0:

                self.update_window()

                QtTest.QTest.qWait(1000)
                if self.force_stop:
                    break

                if self.timer_paused:
                    QtTest.QTest.qWait(50)
                    if self.force_stop:
                        break
                    continue
                self.remaining_time = self.remaining_time - 1

            #

            if not self.remaining_time > 0:

                self.timer_started = False
                self.alarm_running = True

                self.update_window()

                if self.auto_repeat > 0:
                    for i in range(self.auto_repeat):
                        if self.alarm_running and not self.alarm_force_stop:
                            self.__trigger_alert()
                            if self.force_stop:
                                break
                    self.remaining_time = self.time
                    continue

                while self.alarm_running and not self.alarm_force_stop:
                    self.__trigger_alert()
                    if self.force_stop:
                        break
            return

    def __trigger_alert(self):
        self.alarm_sound_player.play()
        QtTest.QTest.qWait(1000)

    def pause_timer(self):
        self.timer_paused = not self.timer_paused
        self.update_buttons()

    def stop_alarm(self):
        self.alarm_force_stop = True
        self.update_window()

    def stop_reset_clock(self):
        self.reset_clock()
        self.update_window()















