import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaContent
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtCore import QUrl, QTime, QRegExp

from datetime import datetime
from ui.trimaudio import Ui_audio_ofset
from icon import resources



date = datetime.now()
month = date.strftime("%B")
year = date.strftime("%Y")
username = os.getlogin()


class audioTrimmer(Ui_audio_ofset, QWidget):
    def __init__(self):
        super(audioTrimmer, self).__init__()
        self.setupUi(self)

        rx  = QRegExp("[0-9]{30}")
        validator = QRegExpValidator(rx)
        self.lineEdit_offset_frame.setValidator(validator)

        self.pushButton_play.setEnabled(False)
        self.pushButton_repeat.setEnabled(False)
        self.pushButton_back_seeek.setEnabled(False)
        self.pushButton_seek.setEnabled(False)
        self.PushButton_nextFrame.setEnabled(False)
        self.pushButton_prevFrame.setEnabled(False)



        self.toolButton_select_track.clicked.connect(self.get_folder)
        self.pushButton_play.clicked.connect(self.play_music)

        # Repeat status
        self.repeat_enabled = False

        self.player = QMediaPlayer()
        self.audio = QAudioOutput()

        # Connect media player signals
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)
        self.playSlider.sliderMoved.connect(self.playSliderChanged)

        # Connect the media status changed signal
        self.player.mediaStatusChanged.connect(self.handle_media_status)

        self.player.positionChanged.connect(self.time_calculate)
        self.player.positionChanged.connect(self.update_current_time)

        self.pushButton_back_seeek.clicked.connect(self.backward)
        self.pushButton_seek.clicked.connect(self.forward)

        self.pushButton_repeat.clicked.connect(self.toggle_repeat)

        # Reset buttons conneect
        self.pushButton_track_pathReset.clicked.connect(self.trackPath_reset)
        self.pushButton_trackNameReset.clicked.connect(self.track_reset)
        self.pushButton_frameReset.clicked.connect(self.ofseet_reset)

        # setting the aofset value from here.
        self.PushButton_nextFrame.clicked.connect(self.inc_frameNumber)
        self.pushButton_prevFrame.clicked.connect(self.dec_frameNumber)


    def inc_frameNumber(self):
        current_value = self.lineEdit_offset_frame.text()
        if current_value == "" or current_value == "0":
            self.counter = 1
        else:
            self.counter = int(current_value) + 1

        self.lineEdit_offset_frame.setText(str(self.counter))

    def dec_frameNumber(self):
        current_value = self.lineEdit_offset_frame.text()
        if current_value == "" or current_value == "0":
            self.counter = 0
        else:
            self.counter = max(0, int(current_value) - 1)

        self.lineEdit_offset_frame.setText(str(self.counter))

    def get_folder(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, 'Audio file', r"", "*.mp3 *.wav")

        if file_name != "":
            media = QMediaContent(QUrl.fromLocalFile(file_name))
            self.player.setMedia(media)
            self.pushButton_play.setEnabled(True)
            self.pushButton_repeat.setEnabled(True)
            self.pushButton_back_seeek.setEnabled(True)
            self.pushButton_seek.setEnabled(True)
            self.PushButton_nextFrame.setEnabled(True)
            self.pushButton_prevFrame.setEnabled(True)

        self.lineEdit_path.setText(file_name)
        self.lineEdit_trackName.setText(file_name.split("/")[-1].split(".")[0])
        return file_name

    def ofset_value(self):
        pass

    def play_music(self):
        icon_play = QIcon(":/icons/play.png")
        icon_pause = QIcon(":/icons/pause.png")

        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.pushButton_play.setIcon(icon_play)
        else:
            self.player.play()
            self.pushButton_play.setIcon(icon_pause)

    def time_calculate(self, position):
        second = int((position / 1000) % 60)
        minutes = int((position / 60000) % 60)
        hour = int((position / 3600000) % 24)

        # Create QTime object with the integer values
        time = QTime(hour, minutes, second)
        self.label_play_time.setText(time.toString())

    def update_current_time(self):
        update_position_ms = self.player.position()
        current_position_ms = self.player.duration() - update_position_ms

        # Calculate the seconds, minutes, and hours from the position
        second = int((current_position_ms / 1000) % 60)
        minutes = int((current_position_ms / 60000) % 60)
        hour = int((current_position_ms / 3600000) % 24)
        time = QTime(hour, minutes, second)

        # Set the formatted time in the label
        self.label_play_remain.setText(time.toString("hh:mm:ss"))

    def position_changed(self, position):
        if self.playSlider.maximum() != self.player.duration():
            self.playSlider.setMaximum(self.player.duration())

        self.playSlider.setValue(position)

    def backward(self):
        # Get current position in milliseconds
        current_position_ms = self.player.position()
        new_position = current_position_ms - 1000
        # Make sure the new position doesn't go below 0
        if new_position < 0:
            new_position = 0

        # Set the new position in the player
        self.player.setPosition(new_position)

    def forward(self):
        # Get current position in milliseconds
        current_position_ms = self.player.position()
        new_position = current_position_ms + 1000
        if new_position > self.player.duration():
            new_position = self.player.duration()

        # Set the new position in the player
        self.player.setPosition(new_position)

    def toggle_repeat(self):
        # Toggle the repeat mode
        icon_repeat_on = QIcon(":/icons/replay_act.png")
        icon_repeat_off = QIcon(":/icons/replay.png")
        self.repeat_enabled = not self.repeat_enabled

        if self.repeat_enabled:
            self.pushButton_repeat.setIcon(icon_repeat_on)
        else:
            self.pushButton_repeat.setIcon(icon_repeat_off)

    def handle_media_status(self, status):
        # Check if the media has ended (i.e., finished playing)
        if status == QMediaPlayer.EndOfMedia:
            if self.repeat_enabled:
                self.player.setPosition(0)
                self.player.play()
            else:
                # If repeat is not enabled, stop the player
                self.player.stop()

    def duration_changed(self, duration):
        self.playSlider.setRange(0, duration)

    def playSliderChanged(self, position):
        self.player.setPosition(position)

    def ofseet_reset(self):
        self.lineEdit_offset_frame.clear()

    def track_reset(self):
        self.lineEdit_trackName.clear()
        self.ofseet_reset()

    def trackPath_reset(self):
        icon_play = QIcon(":/icons/play.png")
        self.pushButton_back_seeek.setEnabled(False)
        self.pushButton_play.setEnabled(False)
        self.pushButton_seek.setEnabled(False)
        self.pushButton_repeat.setEnabled(False)
        self.lineEdit_path.clear()

        # Reset the QMediaPlayer
        if self.player is not None:
            self.player.stop()
            self.pushButton_play.setIcon(icon_play)
            self.label_play_remain.setText("0:00:0")
            self.player = QMediaPlayer()

        self.track_reset()


# For widgets
if __name__ == '__main__':
    app = QApplication([])
    widgets = audioTrimmer()
    widgets.show()
    sys.exit(app.exec_())
