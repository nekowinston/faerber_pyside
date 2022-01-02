from typing import Any, Dict, Union

from PySide6.QtCore import (
    QAbstractTableModel,
    QFile,
    QJsonDocument,
    QModelIndex,
    QPersistentModelIndex,
    Qt,
)
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QAbstractItemView, QMainWindow

from ui.Preferences import Ui_Preferences


# TODO: save colorscheme changes made by the user
class PreferencesWindow(QMainWindow, Ui_Preferences):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # load default color schemes
        rc = QFile(":/data/colorschemes.json")
        rc.open(QFile.ReadOnly)
        self.colorschemes = QJsonDocument.fromJson(rc.readAll().data())
        self.cbb_colorscheme.addItems(self.colorschemes.object().keys())
        self.cbb_colorscheme.setCurrentIndex(0)

        # change the tbl_colors data model to the selected scheme, connect for changes
        self.change_tbl(self.cbb_colorscheme.currentText())
        self.cbb_colorscheme.currentTextChanged.connect(self.change_tbl)
        self.tbl_colors.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_colors.verticalHeader().hide()
        self.tbl_colors.horizontalHeader().setStretchLastSection(True)
        self.tbl_colors.horizontalHeader().hide()
        self.tbl_colors.resizeColumnToContents(0)

    def change_tbl(self, value):
        self.tbl_colors.setModel(TableModel(self.colorschemes.object()[value]))


class TableModel(QAbstractTableModel):
    def __init__(self, data: Dict):
        super().__init__()
        self._data = data
        self._checked = [Qt.Checked for i in range(self.rowCount())]
        print(self._checked)

    def data(
        self, index: Union[QModelIndex, QPersistentModelIndex], role: int = ...
    ) -> Any:
        if role == Qt.DisplayRole:
            if index.column() == 0:
                return self._data[index.row()]["name"]
            if index.column() == 1:
                return self._data[index.row()]["hex"]
            # row 3 is used for the color preview, empty text
            if index.column() == 2:
                return None

        # display a checkbox for the first row
        if role == Qt.CheckStateRole:
            if index.column() == 0:
                return self._checked[index.row()]

        # display the color on the third row
        if role == Qt.ItemDataRole.BackgroundRole:
            if index.column() == 2:
                hex_val = self._data[index.row()]["hex"]
                # replace the hash sign with "0x", then cast it to int with base 16
                if hex_val.startswith("#"):
                    color = int(hex_val.replace("#", "0x"), 16)
                    return QColor(color)

    def flags(self, index: Union[QModelIndex, QPersistentModelIndex]) -> Qt.ItemFlags:
        if index.column() == 0:
            return super().flags(index) | Qt.ItemIsUserCheckable | Qt.ItemIsEditable
        elif index.column() == 2:
            return super().flags(index) & Qt.ItemIsSelectable
        else:
            return super().flags(index) | Qt.ItemIsEditable

    def rowCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self._data)

    def columnCount(
        self, parent: Union[QModelIndex, QPersistentModelIndex] = ...
    ) -> int:
        return 3

    def setData(
        self,
        index: Union[QModelIndex, QPersistentModelIndex],
        value: Any,
        role: int = ...,
    ) -> bool:
        if index.isValid() and role == Qt.EditRole:
            newVal = str()
            if index.column() == 0:
                key = "name" if index.column() == 0 else "hex"
            if index.column() == 1:
                key = "name" if index.column() == 0 else "hex"
            self._data[index.row()][key] = str(newVal)
            return True
        if role == Qt.CheckStateRole:
            print(value)
            self._checked[index.row()] = value
            return True
        return False
