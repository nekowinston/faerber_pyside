from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QResizeEvent, QPixmap
from PySide6.QtWidgets import QLabel


class QImageLabel(QLabel):
    def __init__(self, parent=None):
        super(QImageLabel, self).__init__(parent)

        # store original pixmap, to preserve scaling quality
        self.orig_pixmap = QPixmap()

    def __capped_size(self, size):
        # is the new scale > the image size? return the orignal size
        if self.orig_pixmap.width() < size.width():
            return self.orig_pixmap.size()
        # otherwise, scale down to size
        else:
            return size

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.setPixmap(self.orig_pixmap, self.__capped_size(event.size()))

    def setPixmap(self, pixmap: QPixmap, size: QSize = QSize()) -> None:
        # default to self.frameSize()
        if size.isEmpty():
            size = self.frameSize()
            pass

        # store the passed pixmap as the original
        self.orig_pixmap = pixmap
        # scale it
        pixmap_scaled = pixmap.scaled(self.__capped_size(size), Qt.KeepAspectRatio)
        # and use the inherited function to set the actual pixmap
        super(QImageLabel, self).setPixmap(pixmap_scaled)
