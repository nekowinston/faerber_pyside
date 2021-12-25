from PySide6.QtCore import QFile


def load_stylesheet(self, res=":/styles/dracula"):
    rc = QFile(res)
    rc.open(QFile.ReadOnly)
    content = rc.readAll().data()
    self.setStyleSheet(str(content, "utf-8"))
