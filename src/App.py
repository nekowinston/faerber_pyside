from PySide6.QtCore import QFile, QTranslator, QLibraryInfo, QLocale
from PySide6.QtWidgets import QApplication


class App(QApplication):
    def __init__(self, args):
        super().__init__(args)

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

    def load_stylesheet(self, res="Dracula"):
        rc = QFile(":/styles/{}".format(res))
        rc.open(QFile.ReadOnly)
        content = rc.readAll().data()
        self.setStyleSheet(str(content, "utf-8"))
