import sys

from PySide6.QtCore import QFile, QTranslator, QLocale, QLibraryInfo
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

from ui.MainWindow import Ui_MainWindow
import res


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.open_file_dialog = QFileDialog(self)
        self.open_file_dialog.setFileMode(QFileDialog.ExistingFile)
        self.open_file_dialog.setNameFilter("Images (*.png *.jpg)")
        self.open_file_dialog.setWindowTitle("Open Image")

        self.lbl_open_image.click.connect(self.open_file_dialog.open)
        self.lbl_open_image.wrongdrop.connect(self.show_drop_decline)
        self.lbl_initialText = self.lbl_open_image.text()
        self.lbl_rejectText = self.lbl_open_image.property("dropRejectText")

        self.open_file_dialog.fileSelected.connect(self.load_image)
        self.lbl_open_image.drop.connect(self.load_image)

    def load_image(self, fileUrl):
        print(fileUrl)

    # change label text, to indicate that the file is wrong
    def show_drop_decline(self, event):
        if event:
            self.lbl_open_image.setText(self.lbl_rejectText)
        else:
            self.lbl_open_image.setText(self.lbl_initialText)

    # reset the label text, if it was changed by the drop event
    def leaveEvent(self, event):
        if self.lbl_open_image.text() != self.lbl_initialText:
            self.show_drop_decline(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # this isn't required, but otherwise PyCharm will remove it when optimizing imports
    res.qInitResources()

    # styles
    rc = QFile(':/styles/dracula')
    rc.open(QFile.ReadOnly)
    content = rc.readAll().data()
    app.setStyleSheet(str(content, "utf-8"))

    # i18n
    translator = QTranslator(app)
    app.installTranslator(translator)

    # install the default language
    path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    if translator.load(QLocale.system(), "qtbase", "_", path):
        app.installTranslator(translator)
    # install languages from resources
    translator = QTranslator(app)
    if translator.load(QLocale.system(), "", "", ":/translations"):
        app.installTranslator(translator)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
