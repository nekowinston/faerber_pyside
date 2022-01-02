from typing import Union

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices


# open either str (parsed with Strict Mode) or QUrl with QDesktopServices
# returns: True when successful
def open_url(url: Union[str, QUrl]) -> bool:
    if type(url) == str:
        QDesktopServices.openUrl(QUrl(url, QUrl.ParsingMode.StrictMode))
    elif type(url) == QUrl:
        QDesktopServices.openUrl(url)
    else:
        return False

    return True
