import sys

from PySide6.QtCore import QDir, QEvent, QUrl, Slot
from PySide6.QtGui import QCloseEvent, QDesktopServices, QPixmap
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

import res
from App import App
from PreferencesWindow import PreferencesWindow
from qt.QIGNWorker import QIGNWorker
from qt.QWaitingSpinner import QWaitingSpinner
from ui.MainWindow import Ui_MainWindow
from utils.FaerberProtocolHandler import FaerberProtocolHandler
from utils.qt import open_url


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.logger = QApplication.instance().logger

        # set up scheme handler
        self.protocolHandler = FaerberProtocolHandler(self)
        QDesktopServices.setUrlHandler("faerber", self.protocolHandler, "handle")

        # other windows
        self.wdw_prefs = None

        # ImageGoNord stuff
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

        # accept drops on the initial window, and the imageview
        self.lbl_open_image.drop.connect(self.load_image)
        self.lbl_view.drop.connect(self.load_image)

        self.btn_compare.pressed.connect(self.action_compare_pressed)
        self.btn_compare.released.connect(self.action_compare_released)

        self.act_open.triggered.connect(self.open_file_dialog.open)
        self.act_save.triggered.connect(self.save_file_dialog.open)
        self.act_pref.triggered.connect(self.action_open_preferences)
        self.act_about.triggered.connect(app.aboutQt)
        self.act_support.triggered.connect(
            lambda: open_url("https://github.com/farbenfroh/faerber")
        )

        self.spinner = QWaitingSpinner(self)
        self.spinner.setInnerRadius(40)
        self.spinner.setLineLength(20)
        self.spinner.setLineWidth(8)
        self.spinner.setRoundness(0)
        self.wgt_stacked.layout().addWidget(self.spinner)

    def load_image(self, file_url: str) -> None:
        self.btn_compare.setDisabled(True)
        self.act_save.setDisabled(True)

        self.wgt_stacked.setCurrentIndex(1)
        self.orig_image = QPixmap(file_url)
        self.lbl_view.setPixmap(self.orig_image)
        self.lbl_view.setMask(self.orig_image.mask())

        worker = QIGNWorker(self, file_url)
        worker.start()
        self.spinner.start()
        self.spinner.raise_()

    @Slot(QPixmap)
    def set_image(self, pixmap: QPixmap) -> None:
        self.spinner.stop()
        self.ign_image = pixmap
        self.lbl_view.setPixmap(self.ign_image)

        self.btn_compare.setEnabled(True)
        self.act_save.setEnabled(True)

    def save_image(self, file_url: str) -> None:
        print("saving to: {}".format(file_url))
        self.ign_image.save(file_url, "PNG")

    def action_compare_pressed(self) -> None:
        self.lbl_view.setPixmap(self.orig_image)

    def action_compare_released(self) -> None:
        self.lbl_view.setPixmap(self.ign_image)

    def action_open_preferences(self) -> None:
        self.wdw_prefs = PreferencesWindow()
        self.wdw_prefs.show()

    # change label text, to indicate that the file is wrong
    def show_drop_decline(self, show: bool) -> None:
        if show:
            self.lbl_open_image.setText(self.lbl_rejectText)
        else:
            self.lbl_open_image.setText(self.lbl_initialText)

    # reset the label text, if it was changed by the drop event
    def leaveEvent(self, event: QEvent) -> None:
        if self.lbl_open_image.text() != self.lbl_initialText:
            self.show_drop_decline(False)

    # also close preferences window if main window is closed
    def closeEvent(self, event: QCloseEvent) -> None:
        if self.wdw_prefs:
            self.wdw_prefs.close()
        QMainWindow.closeEvent(self, event)

    @staticmethod
    def handle_open_file_request(url: QUrl) -> bool:
        return open_url(url)


if __name__ == "__main__":
    app = App(sys.argv)

    # this isn't required, but otherwise PyCharm will remove it when optimizing imports
    res.qInitResources()

    window = MainWindow()
    window.show()

    # handle startup URLs
    for arg in sys.argv:
        if arg.startswith("faerber://"):
            window.handle_open_file_request(QUrl(arg))

    app.openFileRequest.connect(window.handle_open_file_request)

    sys.exit(app.exec())
