import logging
from os import path

from PySide6.QtWidgets import QApplication


class Logger(logging.Logger):
    def __init__(self, parent: QApplication):
        super().__init__("faerber")
        formatter = logging.Formatter("%(asctime)s - %(message)s", datefmt="%H:%M:%S")

        # file handler
        fh = logging.FileHandler(path.join(parent.cache, "faerber.log"))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        # stream handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)

        self.setLevel(logging.DEBUG)
        self.addHandler(fh)
        self.addHandler(ch)
        self.info("initialized")
