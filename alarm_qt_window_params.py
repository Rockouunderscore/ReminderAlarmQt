from PyQt5 import QtCore
from PyQt5.QtGui import QIcon

window_width = 600
window_height = 600

window_xpos = 1920 + 2560 - round(2560/2) - round(window_width/2)
window_ypos = 1440 - round(1440/2) - round(window_height/2)
# window_xpos = 1920+2560
# window_ypos = 180

app_name = "Alarm Reminder"
app_icon = QIcon("icon.svg")

