from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QComboBox


class menu_abbonamento(object):

    def setupUi(self, abbonamento):

        if not abbonamento.objectName():
            abbonamento.setObjectName(u"abbonamento")
        abbonamento.resize(640, 480)

        self.comboBox = QComboBox(abbonamento)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(180, 220, 151, 21))

        self.retranslateUi(abbonamento)

        QMetaObject.connectSlotsByName(abbonamento)

    def retranslateUi(self, abbonamento):

        abbonamento.setWindowTitle(QCoreApplication.translate("abbonamento", u"Tipo di abbonamento", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("abbonamento", u"mensile", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("abbonamento", u"annuale", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("abbonamento", u"tempo indeterminato", None))

