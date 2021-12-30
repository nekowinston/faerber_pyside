from os import path
from PySide6.QtCore import QStandardPaths, Qt, Signal
from PySide6.QtWidgets import QLabel


class QClickDropLabel(QLabel):
    click = Signal(bool)
    drop = Signal(str)
    wrongdrop = Signal(bool)

    def __init__(self, parent=None):
        super(QClickDropLabel, self).__init__(parent)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.click.emit(True)

    def dragEnterEvent(self, e):
        mime = e.mimeData()
        file = mime.urls()[0].toLocalFile()
        if (
            mime.hasUrls()
            and len(mime.urls()) == 1
            and (file.endswith(".png") or file.endswith(".jpg"))
        ) or (mime.hasImage()):
            e.acceptProposedAction()
        else:
            self.wrongdrop.emit(True)
            e.ignore()

    def dropEvent(self, e):
        mime = e.mimeData()

        if mime.hasImage():
            image = mime.imageData()
            file_name = path.join(
                (QStandardPaths.writableLocation(QStandardPaths.CacheLocation)),
                "dropped.png",
            )
            image.save(file_name, "PNG")
            print(file_name)
            self.drop.emit(file_name)
        elif mime.hasUrls():
            for url in mime.urls():
                file_name = url.toLocalFile()
                self.drop.emit(file_name)
