from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QResizeEvent, QPixmap
from PySide6.QtWidgets import QLabel


class QImageLabel(QLabel):
    def __init__(self, parent=None):
        super(QImageLabel, self).__init__(parent)

        # store original pixmap, to preserve scaling quality
        self.orig_pixmap = QPixmap()

    def resizeEvent(self, event: QResizeEvent) -> None:
        # is the new scale > the image size? if so, cap at orignal size
        if self.orig_pixmap.width() < event.size().width():
            self.setPixmap(self.orig_pixmap, self.orig_pixmap.size())

        # otherwise, scale down to 0, 0
        else:
            self.setPixmap(self.orig_pixmap, event.size())

    def setPixmap(self, pixmap: QPixmap, size: QSize = QSize()) -> None:
        # default to self.frameSize()
        if size.isEmpty():
            size = self.frameSize()

        # store the passed pixmap as the original
        self.orig_pixmap = pixmap
        # scale it
        pixmap_scaled = pixmap.scaled(size, Qt.KeepAspectRatio)
        # and use the inherited function to set the actual pixmap
        super(QImageLabel, self).setPixmap(pixmap_scaled)
