import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsWidget, QFileDialog

from ui.MainWindow import Ui_MainWindow


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
        self.initialText = self.lbl_open_image.text()

        self.open_file_dialog.fileSelected.connect(self.load_image)
        self.lbl_open_image.drop.connect(self.load_image)

    def load_image(self, fileUrl):
        print(fileUrl)

    # change label text, to indicate that the file is wrong
    def show_drop_decline(self, event):
        if event:
            self.lbl_open_image.setText(u"<html><head/><body><p align='center'><span style='font-size:14pt;'>Please drop a <strong>single</strong> PNG or JPEG</span></p></body></html>")
        else:
            self.lbl_open_image.setText(self.initialText)

    # reset the label text, if it was changed by the drop event
    def leaveEvent(self, event):
        if self.lbl_open_image.text() != self.initialText:
            self.show_drop_decline(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())
