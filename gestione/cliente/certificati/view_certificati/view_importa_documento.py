from PyQt5.QtWidgets import QFileDialog, QMessageBox

from gestione.cliente.GestioneCertificati.controller_GestioneCertificati.controller_GestioneCertificati import \
    Controller_GestioneCertificati


class VistaImportaDocumento(QFileDialog):

    def __init__(self, controller,parent=None):
        super(VistaImportaDocumento, self).__init__(parent)
        self.controller = controller
        self.file_name = self.getOpenFileName(None, 'Seleziona il documento', "", "Pdf files (*.pdf)")
        self.path = self.file_name[0]
        if self.path is None or self.path == '':

            QMessageBox.about(self, "Nessun Documento", "Nessun documento caricato")
            self.close()

            return
        QMessageBox.about(self, "Completato", "Il documento si trova i: ")
        self.close()