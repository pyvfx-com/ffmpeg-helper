import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaContent
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl, QTime

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
        self.pushButton_play.setEnabled(False)
        self.pushButton_repeat.setEnabled(False)
        self.pushButton_back_seeek.setEnabled(False)
        self.pushButton_seek.setEnabled(False)


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

        self.lineEdit_path.setText(file_name)
        self.lineEdit_trackName.setText(file_name.split("/")[-1].split(".")[0])
        return file_name

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
        self.lineEdit_tail_offset_frame.clear()
        self.lineEdit_offset_frame.clear()

    def track_reset(self):
        self.lineEdit_trackName.clear()
        self.ofseet_reset()

    def trackPath_reset(self):
        self.pushButton_back_seeek.setEnabled(False)
        self.pushButton_play.setEnabled(False)
        self.pushButton_seek.setEnabled(False)
        self.pushButton_repeat.setEnabled(False)
        self.lineEdit_path.clear()
        self.track_reset()


# For widgets
if __name__ == '__main__':
    app = QApplication([])
    widgets = audioTrimmer()
    widgets.show()
    sys.exit(app.exec_())
