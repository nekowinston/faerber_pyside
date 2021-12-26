import sys

from PySide6.QtCore import (
    QFile,
    QTranslator,
    QLocale,
    QLibraryInfo,
    QUrl,
    QDir,
)
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap, QDesktopServices
from ImageGoNord.GoNord import GoNord
from PIL import ImageQt

from ui.MainWindow import Ui_MainWindow
import res


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ImageGoNord stuff
        self.go_nord = GoNord()
        self.orig_image = QPixmap()
        self.ign_image = QPixmap()

        # reset to default 0 index, regardless of Designer output
        self.wgt_stacked.setCurrentIndex(0)

        # connect actions
        self.open_file_dialog = QFileDialog(self)
        self.open_file_dialog.setFileMode(QFileDialog.ExistingFile)
        self.open_file_dialog.setDirectory(QDir.homePath())
        # TODO: add translate function
        self.open_file_dialog.setNameFilter("Images (*.png *.jpg)")
        self.open_file_dialog.setWindowTitle("Open Image")
        self.open_file_dialog.fileSelected.connect(self.load_image)

        self.save_file_dialog = QFileDialog(self)
        self.save_file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        self.save_file_dialog.setFileMode(QFileDialog.AnyFile)
        self.save_file_dialog.setDirectory(QDir.homePath())
        self.save_file_dialog.setDefaultSuffix("png")
        # TODO: add translate function
        self.save_file_dialog.setNameFilter("Image (*.png)")
        self.save_file_dialog.setWindowTitle("Save Image")
        self.save_file_dialog.fileSelected.connect(self.save_image)
        self.save_file_dialog.filterSelected.connect(print)

        self.lbl_open_image.click.connect(self.open_file_dialog.open)
        self.lbl_open_image.wrongdrop.connect(self.show_drop_decline)
        self.lbl_initialText = self.lbl_open_image.text()
        self.lbl_rejectText = self.lbl_open_image.property("dropRejectText")

        self.lbl_open_image.drop.connect(self.load_image)

        self.btn_compare.pressed.connect(self.action_compare_pressed)
        self.btn_compare.released.connect(self.action_compare_released)

        self.act_open.triggered.connect(self.open_file_dialog.open)
        self.act_save.triggered.connect(self.save_file_dialog.open)
        self.act_support.triggered.connect(self.action_support)

    def load_image(self, fileUrl):
        self.btn_compare.setDisabled(True)
        self.act_save.setDisabled(True)

        self.wgt_stacked.setCurrentIndex(1)
        self.orig_image = QPixmap(fileUrl)
        self.lbl_view.setPixmap(self.orig_image)
        self.lbl_view.setMask(self.orig_image.mask())

        gn_file = self.go_nord.open_image(fileUrl)
        gn_img = self.go_nord.convert_image(gn_file)
        gn_img = ImageQt.ImageQt(gn_img)

        self.ign_image = QPixmap().fromImage(gn_img)
        self.lbl_view.setPixmap(self.ign_image)

        self.btn_compare.setEnabled(True)
        self.act_save.setEnabled(True)

    def save_image(self, fileUrl):
        print("saving to: {}".format(fileUrl))
        self.ign_image.save(fileUrl, "PNG")

    def open_url(self, url):
        QDesktopServices.openUrl(QUrl(url, QUrl.StrictMode))

    def action_compare_pressed(self):
        self.lbl_view.setPixmap(self.orig_image)

    def action_compare_released(self):
        self.lbl_view.setPixmap(self.ign_image)

    def action_support(self):
        self.open_url("https://github.com/nekowinston/IGNQt")

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
    rc = QFile(":/styles/dracula")
    rc.open(QFile.ReadOnly)
    content = rc.readAll().data()
    app.setStyleSheet(str(content, "utf-8"))

    # i18n
    translator = QTranslator(app)
    app.installTranslator(translator)

    # install the default language
    path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    if translator.load(QLocale.system().language(), "qtbase", "_", path):
        app.installTranslator(translator)
    # install languages from resources
    translator = QTranslator(app)
    if translator.load(QLocale.system().language(), "", "", ":/translations"):
        app.installTranslator(translator)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
