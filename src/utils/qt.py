from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices


def open_url(url):
    QDesktopServices.openUrl(QUrl(url, QUrl.StrictMode))
