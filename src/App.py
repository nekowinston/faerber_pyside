import os

from PySide6.QtCore import (
    QEvent,
    QFile,
    QLibraryInfo,
    QLocale,
    QStandardPaths,
    QTranslator,
    QUrl,
    Signal,
)
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QApplication

from utils.FaerberProtocolHandler import FaerberProtocolHandler
from utils.logger import Logger


class App(QApplication):
    openFileRequest = Signal(QUrl)

    def __init__(self, args):
        super().__init__(args)

        self.setOrganizationName("farbenfroh")
        self.setOrganizationDomain("farbenfroh.io")
        self.setApplicationName("faerber")

        # create cache
        self.cache = QStandardPaths.writableLocation(QStandardPaths.CacheLocation)
        os.makedirs(self.cache, exist_ok=True)

        self.logger = Logger(self)

        # set up scheme handler
        self.protocolHandler = FaerberProtocolHandler(self)
        QDesktopServices.setUrlHandler("faerber", self.protocolHandler, "handle")

        # i18n
        # load translation from resources, if available
        path = ":/i18n"
        translator = QTranslator(self)
        lang_avail = translator.load(QLocale.system(), "", "", path)
        if lang_avail:
            self.installTranslator(translator)
        # also load Qt-internal translation only if a provided one was loaded
        path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
        translator = QTranslator(self)
        if translator.load(QLocale.system(), "qtbase", "_", path) and lang_avail:
            self.installTranslator(translator)

    def load_stylesheet(self, res: str = "Dracula") -> None:
        rc = QFile(":/styles/{}".format(res))
        rc.open(QFile.ReadOnly)
        content = rc.readAll().data()
        self.setStyleSheet(str(content, "utf-8"))

    def event(self, event: QEvent) -> bool:
        if event.type() == QEvent.FileOpen:
            self.openFileRequest.emit(event.url())
        return super().event(event)
