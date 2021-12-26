from PySide6.QtCore import QFile, QJsonDocument
from PySide6.QtWidgets import QMainWindow

from ui.Preferences import Ui_Preferences


# TODO: make this actually useful
class PreferencesWindow(QMainWindow, Ui_Preferences):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # load default color schemes
        rc = QFile(":/data/colorschemes.json")
        rc.open(QFile.ReadOnly)
        self.colorschemes = QJsonDocument.fromJson(rc.readAll().data())
        self.cbb_colorscheme.addItems(self.colorschemes.object().keys())
