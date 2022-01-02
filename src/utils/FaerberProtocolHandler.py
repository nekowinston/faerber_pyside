from PySide6.QtCore import QEvent, QObject, QUrl, Slot


# custom protocol handler for the "farber://" protocol
class FaerberProtocolHandler(QObject):
    def __init__(self: QObject, parent):
        super().__init__()
        self.logger = parent.logger

    # TODO: implement useful functions like:
    #   - OAuth with farbenfroh.io for unrestricted API access
    #   - Colorscheme import via URI
    @Slot(QUrl)
    def handle(self, event: QEvent):
        self.logger.info("FaerberProtocolHandler")
        self.logger.info(event)
