import os
from typing import Union

from ImageGoNord.GoNord import GoNord
from PIL import ImageQt
from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtGui import QPixmap


class QIGNSignals(QObject):
    finished = Signal(QPixmap)


class QIGNWorker(QThread):
    def __init__(self, parent, file: Union[str, os.PathLike]):
        QThread.__init__(self, parent)
        self.signals = QIGNSignals()
        self.signals.finished.connect(parent.set_image)
        self.file = file
        self.go_nord = GoNord()

    def run(self) -> None:
        gn_file = self.go_nord.open_image(self.file)
        gn_img = self.go_nord.convert_image(gn_file)
        gn_img = ImageQt.ImageQt(gn_img)

        self.signals.finished.emit(QPixmap().fromImage(gn_img))
