import sys, os
from PyQt5 import QtCore, QtWidgets, QtPrintSupport

class Print_Dialog(QtWidgets.QWidget):
    def __init__(self):
        super(Print_Dialog, self).__init__()
        self.setWindowTitle('Document Printer')
        self.editor = QtWidgets.QTextEdit(self)
        self.editor.textChanged.connect(self.handleTextChanged)
        self.buttonOpen = QtWidgets.QPushButton('Open', self)
        self.buttonOpen.clicked.connect(self.handleOpen)
        self.buttonPrint = QtWidgets.QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QtWidgets.QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        layout.addWidget(self.buttonOpen, 1, 0)
        layout.addWidget(self.buttonPrint, 1, 1)
        layout.addWidget(self.buttonPreview, 1, 2)
        self.auto_opened_file()
        self.handleTextChanged()

    def handleOpen(self):
        path = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open file', '',
            'HTML files (*.html);;Text files (*.txt)')[0]
        if path:
            file = QtCore.QFile(path)
            if file.open(QtCore.QIODevice.ReadOnly):
                stream = QtCore.QTextStream(file)
                text = stream.readAll()
                info = QtCore.QFileInfo(path)
                if info.completeSuffix() == 'html':
                    self.editor.setHtml(text)
                else:
                    self.editor.setPlainText(text)
                file.close()


    def auto_opened_file(self):
        path = 'GUI/data.txt'
        file = QtCore.QFile(path)
        if file.open(QtCore.QIODevice.ReadOnly):
            stream = QtCore.QTextStream(file)
            text = stream.readAll()
            info = QtCore.QFileInfo(path)
            if info.completeSuffix() == 'txt':
                self.editor.setPlainText(text)
            file.close()
            self.handlePreview()
            sys.exit()
        

    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.editor.document().print_(dialog.printer())

    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.editor.print_)
        dialog.exec_()

    def handleTextChanged(self):
        enable = not self.editor.document().isEmpty()
        self.buttonPrint.setEnabled(enable)
        self.buttonPreview.setEnabled(enable)


# if __name__ == '__main__':

def run():
    app = QtWidgets.QApplication(sys.argv)
    window = Print_Dialog()
    window.resize(400, 200)
    window.show()
    sys.exit(app.exec_())

