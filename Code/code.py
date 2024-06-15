from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import interface
import os

class Player(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super(Player, self).__init__()
        self.setupUi(self)
        self.Play.clicked.connect(self.play)
        self.Pause.clicked.connect(self.stop)
        self.listMusic.itemDoubleClicked.connect(self.play)
        self.Load.clicked.connect(self.load)

        self.dir = ""

        self.setFixedSize(self.size())
        self.setWindowIcon(QtGui.QIcon("../Icon.ico"))

    def play(self):
        item = self.listMusic.currentItem()

        if item:
            file_name = os.path.join(self.dir, item.text())
            file_name = file_name.replace('/',"\\")
            print(file_name)

            content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file_name))

            self.mediaPlayer = QtMultimedia.QMediaPlayer()
            self.mediaPlayer.setMedia(content)
            self.mediaPlayer.play()
            print(1)
        else:
            self.listMusic.setCurrentRow(0)
            self.play()
            print(2)

    def stop(self):
        self.mediaPlayer.stop()
        print(3)

    def load(self):
        self.listMusic.clear()

        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")

        if dir:
            for file_name in os.listdir(dir):
                if file_name.endswith(".mp3"):
                    self.listMusic.addItem(os.path.join(file_name))

            self.dir = dir
        print(4)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    player = Player()
    player.show()
    app.exec()