# sudo apt purge gstreamer1.0-vaapi (linux) ???????? MAY NOT NEED
# may need LAV filters (win)

import os

from PySide6 import QtGui
from PySide6.QtCore import QUrl, Qt
from PySide6.QtMultimedia import QMediaPlayer, QVideoSink
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QWidget

class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 500)
        self.setWindowTitle('Event Manager')

        '''
        This mdp (self.mdp.mediaStatusChanged) signal is emitted to check if status has cjhanged from 
        LoadingMedia->BufferingMedia to BufferedMedia and  go to clicked position. 
        Otherwise, on newly loaded media, it will not jump immedeately due to buffering in progress.      
        '''
        self.mdp = QMediaPlayer(self)           # player for video
        self.mdp_i = QMediaPlayer(self)         # player for screengrabs

        #  see above
        self.mdp.mediaStatusChanged.connect(lambda: self.loadstatus(self.mdp.mediaStatus()))
        self.mdp_i.mediaStatusChanged.connect(lambda: self.loadstatus(self.mdp_i.mediaStatus()))

        # create videowidget and set player output to it
        self.vd = QVideoWidget(self)
        self.mdp.setVideoOutput(self.vd)

        # create video sink for frame extraction and connect to player_i
        self.video_sink = QVideoSink()
        self.video_sink.videoFrameChanged.connect(self.getframe)
        self.mdp_i.setVideoSink(self.video_sink)

        self.evtno = 0
        self.timestamp = 0


    def wheelEvent(self, e):
        # moving 0.5s bwd-fwd from current position
        if e.angleDelta().y() > 0:
            self.pos += 500
        else:
            self.pos -= 500
        self.gototime(self.pos, self.evtno, self.timestamp)


    def keyPressEvent(self, e):
        # save frame as image if Spacebar pressed
        if e.key() == Qt.Key_Space:
            # print(self.frame)
            image = self.frame.toImage()
            image.save(os.path.join(self.savefolder, f'evt_{self.evtno + 1}_{self.timestamp}.jpg'))


    def getframe(self, frame):
        # method to get frame from videoSink
        self.frame = frame


    def loadmedia(self, media, pos, savefolder):
        #  loading media to player and player_i and got to pos=0 (see loadstatus)
        self.savefolder = savefolder
        self.pos = pos

        self.mdp.setSource(QUrl.fromLocalFile(media))
        self.mdp.play()
        self.mdp.pause()

        self.mdp_i.setSource(QUrl.fromLocalFile(media))
        self.mdp_i.play()
        self.mdp_i.pause()


    def gototime(self, pos, evtno, timestamp):
        # set position to player and player_i of the clicked event
        self.evtno = evtno
        self.timestamp = timestamp
        self.pos = pos

        self.mdp.setPosition(self.pos)
        self.mdp_i.setPosition(self.pos)


    def resizeEvent(self, e: QtGui.QResizeEvent):
        # on resize
        self.vd.setGeometry(0, 0, self.size().width(), self.size().height())


    def loadstatus(self, stat):
        # print(stat)
        '''
        jumps to selected event once media is BufferedMedia (newly loaded)
        '''
        if stat == QMediaPlayer.BufferedMedia:
           # print(f'ready {self.pos}')
           self.gototime(self.pos, self.evtno, self.timestamp)


