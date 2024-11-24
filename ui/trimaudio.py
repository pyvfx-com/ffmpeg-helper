from PyQt5.QtCore import (QCoreApplication,QMetaObject, QSize, Qt)
from PyQt5.QtGui import (QFont, QIcon)
from PyQt5.QtWidgets import (QFrame, QGridLayout, QHBoxLayout,QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QToolButton, QVBoxLayout)



class Ui_audio_ofset(object):
    def setupUi(self, audio_ofset):
        if not audio_ofset.objectName():
            audio_ofset.setObjectName(u"audio_ofset")
        audio_ofset.resize(510, 208)
        audio_ofset.setMinimumSize(QSize(510, 208))
        audio_ofset.setMaximumSize(QSize(510, 208))
        audio_ofset.setStyleSheet(u"QWidget {\n"
"	background-color: #2a2a2a;\n"
"}")
        self.gridLayout = QGridLayout(audio_ofset)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.audio_spectrum_frame = QFrame(audio_ofset)
        self.audio_spectrum_frame.setObjectName(u"audio_spectrum_frame")
        self.audio_spectrum_frame.setStyleSheet(u"QFrame {\n"
"    border-radius: 4px;\n"
"	background-color:#3b3b3b;\n"
"}")
        self.audio_spectrum_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.audio_spectrum_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.audio_spectrum_frame)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.audio_spectrum_view = QFrame(self.audio_spectrum_frame)
        self.audio_spectrum_view.setObjectName(u"audio_spectrum_view")
        self.audio_spectrum_view.setStyleSheet(u"QFrame {\n"
"	border : 1px solid #4C6C3F;\n"
"    border-radius: 8px;\n"
"	background-color:#323232;\n"
"}")
        self.audio_spectrum_view.setFrameShape(QFrame.Shape.StyledPanel)
        self.audio_spectrum_view.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.audio_spectrum_view)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.Track_root_path_horizontalLayout = QHBoxLayout()
        self.Track_root_path_horizontalLayout.setObjectName(u"Track_root_path_horizontalLayout")
        self.label_root_path = QLabel(self.audio_spectrum_view)
        self.label_root_path.setObjectName(u"label_root_path")
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_root_path.setFont(font)
        self.label_root_path.setStyleSheet(u" QLabel {\n"
"	color: rgb(150, 150, 150);\n"
"	border : none;\n"
"    border-radius: none;\n"
"	background-color:none;\n"
"}")

        self.Track_root_path_horizontalLayout.addWidget(self.label_root_path)

        self.lineEdit_path = QLineEdit(self.audio_spectrum_view)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setMinimumSize(QSize(282, 25))
        self.lineEdit_path.setMaximumSize(QSize(282, 25))
        font1 = QFont()
        font1.setPointSize(9)
        self.lineEdit_path.setFont(font1)
        self.lineEdit_path.setStyleSheet(u"QLineEdit {\n"
"    color: #548f54;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    padding: 0 8px;\n"
"    background: #212121;\n"
"    selection-background-color: #212121;\n"
"}")

        self.Track_root_path_horizontalLayout.addWidget(self.lineEdit_path)

        self.toolButton_select_track = QToolButton(self.audio_spectrum_view)
        self.toolButton_select_track.setObjectName(u"toolButton_select_track")
        self.toolButton_select_track.setStyleSheet(u"QToolButton { /* all types of tool button */\n"
"	color:#4A702B;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #151616, stop: 1 #1C1D1C);\n"
"    min-width: 25px;\n"
"	min-height: 23px;\n"
"\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"    padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1C1D1C, stop: 1 #151616);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	color: #151616;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4A702B, stop: 1 #215740);	\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
"    border: 1px solid #1C1D1C;\n"
"    border-t"
                        "op-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    /* 16px width + 4px for border = 20px allocated above */\n"
"    width: 16px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
"    top: 1px; left: 1px; /* shift it a bit */\n"
"}")

        self.Track_root_path_horizontalLayout.addWidget(self.toolButton_select_track)

        self.pushButton_track_pathReset = QPushButton(self.audio_spectrum_view)
        self.pushButton_track_pathReset.setObjectName(u"pushButton_track_pathReset")
        self.pushButton_track_pathReset.setMinimumSize(QSize(62, 27))
        self.pushButton_track_pathReset.setMaximumSize(QSize(60, 25))
        self.pushButton_track_pathReset.setStyleSheet(u"QPushButton {\n"
"	color:#4A702B;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #151616, stop: 1 #1C1D1C);\n"
"    min-width: 60px;\n"
"	min-height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #151616;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4A702B, stop: 1 #215740);	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #4A702B;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1C1D1C, stop: 1 #151616);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")

        self.Track_root_path_horizontalLayout.addWidget(self.pushButton_track_pathReset)


        self.verticalLayout_3.addLayout(self.Track_root_path_horizontalLayout)

        self.Track_horizontalLayout = QHBoxLayout()
        self.Track_horizontalLayout.setObjectName(u"Track_horizontalLayout")
        self.label_TrackName = QLabel(self.audio_spectrum_view)
        self.label_TrackName.setObjectName(u"label_TrackName")
        self.label_TrackName.setFont(font)
        self.label_TrackName.setStyleSheet(u" QLabel {\n"
"	color: rgb(150, 150, 150);\n"
"	border : none;\n"
"    border-radius: none;\n"
"	background-color:none;\n"
"}")

        self.Track_horizontalLayout.addWidget(self.label_TrackName)

        self.lineEdit_trackName = QLineEdit(self.audio_spectrum_view)
        self.lineEdit_trackName.setObjectName(u"lineEdit_trackName")
        self.lineEdit_trackName.setMinimumSize(QSize(317, 25))
        self.lineEdit_trackName.setMaximumSize(QSize(317, 25))
        self.lineEdit_trackName.setStyleSheet(u"QLineEdit {\n"
"    color: #548f54;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    padding: 0 8px;\n"
"    background: #212121;\n"
"    selection-background-color: #212121;\n"
"}")

        self.Track_horizontalLayout.addWidget(self.lineEdit_trackName)

        self.pushButton_trackNameReset = QPushButton(self.audio_spectrum_view)
        self.pushButton_trackNameReset.setObjectName(u"pushButton_trackNameReset")
        self.pushButton_trackNameReset.setMinimumSize(QSize(62, 27))
        self.pushButton_trackNameReset.setMaximumSize(QSize(60, 25))
        self.pushButton_trackNameReset.setStyleSheet(u"QPushButton {\n"
"	color:#4A702B;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #151616, stop: 1 #1C1D1C);\n"
"    min-width: 60px;\n"
"	min-height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #151616;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4A702B, stop: 1 #215740);	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #4A702B;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1C1D1C, stop: 1 #151616);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")

        self.Track_horizontalLayout.addWidget(self.pushButton_trackNameReset)


        self.verticalLayout_3.addLayout(self.Track_horizontalLayout)

        self.offset_horizontalLayout = QHBoxLayout()
        self.offset_horizontalLayout.setObjectName(u"offset_horizontalLayout")
        self.label_offset = QLabel(self.audio_spectrum_view)
        self.label_offset.setObjectName(u"label_offset")
        self.label_offset.setFont(font)
        self.label_offset.setStyleSheet(u" QLabel {\n"
"	color: rgb(150, 150, 150);\n"
"	border : none;\n"
"    border-radius: none;\n"
"	background-color:none;\n"
"}")

        self.offset_horizontalLayout.addWidget(self.label_offset)

        self.pushButton_prevFrame = QPushButton(self.audio_spectrum_view)
        self.pushButton_prevFrame.setObjectName(u"pushButton_prevFrame")
        self.pushButton_prevFrame.setMinimumSize(QSize(27, 25))
        self.pushButton_prevFrame.setMaximumSize(QSize(25, 25))
        font2 = QFont()
        font2.setBold(True)
        self.pushButton_prevFrame.setFont(font2)
        self.pushButton_prevFrame.setStyleSheet(u"QPushButton {\n"
"	color:#4A702B;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #151616, stop: 1 #1C1D1C);\n"
"    min-width: 25px;\n"
"    min-height: 23px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #151616;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4A702B, stop: 1 #215740);	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #4A702B;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1C1D1C, stop: 1 #151616);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/prev.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_prevFrame.setIcon(icon)

        self.offset_horizontalLayout.addWidget(self.pushButton_prevFrame)

        self.lineEdit_offset_frame = QLineEdit(self.audio_spectrum_view)
        self.lineEdit_offset_frame.setObjectName(u"lineEdit_offset_frame")
        self.lineEdit_offset_frame.setMinimumSize(QSize(124, 25))
        self.lineEdit_offset_frame.setMaximumSize(QSize(124, 25))
        self.lineEdit_offset_frame.setStyleSheet(u"QLineEdit {\n"
"    color: #548f54;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    padding: 0 8px;\n"
"    background: #212121;\n"
"    selection-background-color: #212121;\n"
"}")
        self.lineEdit_offset_frame.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.offset_horizontalLayout.addWidget(self.lineEdit_offset_frame)

        self.lineEdit_tail_offset_frame = QLineEdit(self.audio_spectrum_view)
        self.lineEdit_tail_offset_frame.setObjectName(u"lineEdit_tail_offset_frame")
        self.lineEdit_tail_offset_frame.setMinimumSize(QSize(124, 25))
        self.lineEdit_tail_offset_frame.setMaximumSize(QSize(124, 25))
        self.lineEdit_tail_offset_frame.setStyleSheet(u"QLineEdit {\n"
"    color: #548f54;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    padding: 0 8px;\n"
"    background: #212121;\n"
"    selection-background-color: #212121;\n"
"}")
        self.lineEdit_tail_offset_frame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_tail_offset_frame.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)

        self.offset_horizontalLayout.addWidget(self.lineEdit_tail_offset_frame)

        self.PushButton_nextFrame = QPushButton(self.audio_spectrum_view)
        self.PushButton_nextFrame.setObjectName(u"PushButton_nextFrame")
        self.PushButton_nextFrame.setMinimumSize(QSize(27, 25))
        self.PushButton_nextFrame.setMaximumSize(QSize(25, 25))
        self.PushButton_nextFrame.setFont(font2)
        self.PushButton_nextFrame.setStyleSheet(u"QPushButton {\n"
"	color:#4A702B;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #151616, stop: 1 #1C1D1C);\n"
"    min-width: 25px;\n"
"    min-height: 23px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #151616;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4A702B, stop: 1 #215740);	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #4A702B;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1C1D1C, stop: 1 #151616);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PushButton_nextFrame.setIcon(icon1)

        self.offset_horizontalLayout.addWidget(self.PushButton_nextFrame)

        self.pushButton_frameReset = QPushButton(self.audio_spectrum_view)
        self.pushButton_frameReset.setObjectName(u"pushButton_frameReset")
        self.pushButton_frameReset.setMinimumSize(QSize(62, 27))
        self.pushButton_frameReset.setMaximumSize(QSize(60, 25))
        self.pushButton_frameReset.setStyleSheet(u"QPushButton {\n"
"	color:#4A702B;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #151616, stop: 1 #1C1D1C);\n"
"    min-width: 60px;\n"
"	min-height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #151616;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4A702B, stop: 1 #215740);	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #4A702B;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1C1D1C, stop: 1 #151616);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")

        self.offset_horizontalLayout.addWidget(self.pushButton_frameReset)


        self.verticalLayout_3.addLayout(self.offset_horizontalLayout)

        self.audio_spectrum_horizontalLayout = QHBoxLayout()
        self.audio_spectrum_horizontalLayout.setObjectName(u"audio_spectrum_horizontalLayout")
        self.frame_Controls = QFrame(self.audio_spectrum_view)
        self.frame_Controls.setObjectName(u"frame_Controls")
        self.frame_Controls.setMinimumSize(QSize(332, 80))
        self.frame_Controls.setMaximumSize(QSize(332, 80))
        self.frame_Controls.setStyleSheet(u"QFrame {\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"	background-color:none;\n"
"}")
        self.frame_Controls.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Controls.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_Controls)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.playSlider = QSlider(self.frame_Controls)
        self.playSlider.setObjectName(u"playSlider")
        self.playSlider.setStyleSheet(u"QSlider {\n"
"    background-color: rgb(0, 85, 0, 0);\n"
"}\n"
"")
        self.playSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_4.addWidget(self.playSlider)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_play_time = QLabel(self.frame_Controls)
        self.label_play_time.setObjectName(u"label_play_time")
        self.label_play_time.setStyleSheet(u" QLabel {\n"
"	color: rgb(150, 150, 150);\n"
"	border : none;\n"
"    border-radius: none;\n"
"	background-color:none;\n"
"}")
        self.label_play_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_play_time)

        self.line = QFrame(self.frame_Controls)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.label_play_remain = QLabel(self.frame_Controls)
        self.label_play_remain.setObjectName(u"label_play_remain")
        self.label_play_remain.setStyleSheet(u" QLabel {\n"
"	color: rgb(150, 150, 150);\n"
"	border : none;\n"
"    border-radius: none;\n"
"	background-color:none;\n"
"}")
        self.label_play_remain.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_play_remain)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 17, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 0, 3, 3)
        self.pushButton_back_seeek = QPushButton(self.frame_Controls)
        self.pushButton_back_seeek.setObjectName(u"pushButton_back_seeek")
        self.pushButton_back_seeek.setMinimumSize(QSize(27, 25))
        self.pushButton_back_seeek.setMaximumSize(QSize(25, 25))
        self.pushButton_back_seeek.setStyleSheet(u"QPushButton {\n"
"	color:#4A702B;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #151616, stop: 1 #1C1D1C);\n"
"    min-width: 25px;\n"
"    min-height: 23px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #151616;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4A702B, stop: 1 #215740);	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #4A702B;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1C1D1C, stop: 1 #151616);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/backword.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_back_seeek.setIcon(icon2)

        self.horizontalLayout.addWidget(self.pushButton_back_seeek)

        self.pushButton_play = QPushButton(self.frame_Controls)
        self.pushButton_play.setObjectName(u"pushButton_play")
        self.pushButton_play.setMinimumSize(QSize(27, 25))
        self.pushButton_play.setMaximumSize(QSize(25, 25))
        self.pushButton_play.setStyleSheet(u"QPushButton {\n"
"	color:#4A702B;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #151616, stop: 1 #1C1D1C);\n"
"    min-width: 25px;\n"
"    min-height: 23px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #151616;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4A702B, stop: 1 #215740);	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #4A702B;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1C1D1C, stop: 1 #151616);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_play.setIcon(icon3)

        self.horizontalLayout.addWidget(self.pushButton_play)

        self.pushButton_seek = QPushButton(self.frame_Controls)
        self.pushButton_seek.setObjectName(u"pushButton_seek")
        self.pushButton_seek.setMinimumSize(QSize(27, 25))
        self.pushButton_seek.setMaximumSize(QSize(25, 25))
        self.pushButton_seek.setStyleSheet(u"QPushButton {\n"
"	color:#4A702B;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #151616, stop: 1 #1C1D1C);\n"
"    min-width: 25px;\n"
"    min-height: 23px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #151616;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4A702B, stop: 1 #215740);	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #4A702B;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1C1D1C, stop: 1 #151616);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/forward.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_seek.setIcon(icon4)

        self.horizontalLayout.addWidget(self.pushButton_seek)

        self.pushButton_repeat = QPushButton(self.frame_Controls)
        self.pushButton_repeat.setObjectName(u"pushButton_repeat")
        self.pushButton_repeat.setMinimumSize(QSize(27, 25))
        self.pushButton_repeat.setMaximumSize(QSize(25, 25))
        self.pushButton_repeat.setStyleSheet(u"QPushButton {\n"
"	color:#4A702B;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #151616, stop: 1 #1C1D1C);\n"
"    min-width: 25px;\n"
"    min-height: 23px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #151616;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4A702B, stop: 1 #215740);	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #4A702B;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1C1D1C, stop: 1 #151616);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/replay.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_repeat.setIcon(icon5)

        self.horizontalLayout.addWidget(self.pushButton_repeat)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 4, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.audio_spectrum_horizontalLayout.addWidget(self.frame_Controls)

        self.pushButton = QPushButton(self.audio_spectrum_view)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 80))
        self.pushButton.setMaximumSize(QSize(150, 80))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color:#4A702B;\n"
"    border: 1px solid #215740;\n"
"    border-radius: 4px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #151616, stop: 1 #1C1D1C);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #151616;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #4A702B, stop: 1 #215740);	\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #4A702B;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #1C1D1C, stop: 1 #151616);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")

        self.audio_spectrum_horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.audio_spectrum_horizontalLayout)


        self.verticalLayout.addWidget(self.audio_spectrum_view)


        self.gridLayout.addWidget(self.audio_spectrum_frame, 1, 0, 1, 1)


        self.retranslateUi(audio_ofset)

        QMetaObject.connectSlotsByName(audio_ofset)
    # setupUi

    def retranslateUi(self, audio_ofset):
        audio_ofset.setWindowTitle(QCoreApplication.translate("audio_ofset", u"Audio Offset Exporter", None))
        self.label_root_path.setText(QCoreApplication.translate("audio_ofset", u"Track Root Path", None))
        self.toolButton_select_track.setText(QCoreApplication.translate("audio_ofset", u"...", None))
        self.pushButton_track_pathReset.setText(QCoreApplication.translate("audio_ofset", u"Reset", None))
        self.label_TrackName.setText(QCoreApplication.translate("audio_ofset", u"Track Name", None))
        self.pushButton_trackNameReset.setText(QCoreApplication.translate("audio_ofset", u"Reset", None))
        self.label_offset.setText(QCoreApplication.translate("audio_ofset", u"Offset", None))
        self.lineEdit_offset_frame.setPlaceholderText(QCoreApplication.translate("audio_ofset", u"offset start frame", None))
        self.lineEdit_tail_offset_frame.setPlaceholderText(QCoreApplication.translate("audio_ofset", u"offset tail frame", None))
        self.pushButton_frameReset.setText(QCoreApplication.translate("audio_ofset", u"Reset", None))
        self.pushButton.setText(QCoreApplication.translate("audio_ofset", u"Publish", None))
    # retranslateUi
