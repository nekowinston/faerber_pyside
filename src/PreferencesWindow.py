from PySide6.QtWidgets import QWidget
from ui.Preferences import Ui_Preferences


# TODO: make this actually useful
class PreferencesWindow(QWidget, Ui_Preferences):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
