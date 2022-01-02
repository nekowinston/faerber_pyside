from PySide6.QtCore import QObject, QUrl, Slot


# custom protocol handler for the "farber://" protocol
class FaerberProtocolHandler(QObject):
    def __init__(self: QObject, parent):
        super().__init__()
        self.logger = parent.logger

    @Slot(QUrl)
    def handle(self, event):
        self.logger.info("FaerberProtocolHandler")
        self.logger.info(event)
