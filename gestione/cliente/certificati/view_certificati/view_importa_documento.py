from PyQt5.QtWidgets import QFileDialog, QMessageBox


class VistaImportaDocumento(QFileDialog):

    def __init__(self, controller, parent=None):
        super(VistaImportaDocumento, self).__init__(parent)

        self.controller = controller
        self.file_name = self.getOpenFileName(None, 'Seleziona il documento', "", "Pdf files (*.pdf)")
        self.path = self.file_name[0]
        if self.path is None or self.path == '':

            QMessageBox.about(self, "Nessun Documento", "Nessun documento caricato")
            self.close()

            return
        self.controller.set_documento_identita(self.path)
        QMessageBox.about(self, "Completato", "Il caricamento del documento è stato completato")
        self.close()