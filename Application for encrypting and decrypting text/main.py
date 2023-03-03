from PyQt5 import QtCore, QtGui, QtWidgets
from app import Ui_MainWindow
from tab import crypt, decrypt
import doubletab as dtab


def clear():
    ui.textResult.setText('')



def resV():
    ui.textResult.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
    if (ui.crypt_radioButton.isChecked() == True) and (ui.textEdit_V.toPlainText() != '') and (ui.textKey.toPlainText() != ''):
        if ui.textResult.toPlainText() == '':
            ui.textResult.setText(crypt(ui.textEdit_V.toPlainText().upper(), ui.textKey.toPlainText().upper()))
        else:
            ui.textResult.setText(ui.textResult.toPlainText() + '\n' + crypt(ui.textEdit_V.toPlainText().upper(), ui.textKey.toPlainText().upper()))

    elif (ui.decrypt_radioButton.isChecked() == True) and (ui.textEdit_V.toPlainText() != '') and (ui.textKey.toPlainText() != ''):
        if ui.textResult.toPlainText() == '':
            ui.textResult.setText(decrypt(ui.textEdit_V.toPlainText().upper(), ui.textKey.toPlainText().upper()))
        else:
            ui.textResult.setText(ui.textResult.toPlainText() + '\n' + decrypt(ui.textEdit_V.toPlainText().upper(), ui.textKey.toPlainText().upper()))

    else:
        if ui.textResult.toPlainText() == '':
            ui.textResult.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
            ui.textResult.setText('!!!Choice encryption or decryption, enter text and key!!!')
        else:
            ui.textResult.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
            ui.textResult.setText(ui.textResult.toPlainText() + '\n' + '!!!Choice encryption or decryption, enter text and key!!!')



def resW():
    ui.textResult.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
    if (ui.textEdit_W.toPlainText() != '') and (ui.textKey1.toPlainText() != '') and (ui.textKey2.toPlainText() != '') and (len(ui.textEdit_W.toPlainText()) % 2 == 0):
        if ui.textResult.toPlainText() == '':
            ui.textResult.setText(dtab.res(ui.textEdit_W.toPlainText().upper(), ui.textKey1.toPlainText().upper(), ui.textKey2.toPlainText().upper()))
        else:
            ui.textResult.setText(ui.textResult.toPlainText() + '\n' + dtab.res(ui.textEdit_W.toPlainText().upper(), ui.textKey1.toPlainText().upper(), ui.textKey2.toPlainText().upper()))        
    
    if len(ui.textEdit_W.toPlainText()) % 2 != 0:
        if ui.textResult.toPlainText() == '':
            ui.textResult.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
            ui.textResult.setText('!!!The string must be divisible by 2!!!')
        else:
            ui.textResult.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
            ui.textResult.setText(ui.textResult.toPlainText() + '\n' + '!!!The string must be divisible by 2!!!')

    if (ui.textEdit_W.toPlainText() == '') or (ui.textKey1.toPlainText() == '') or (ui.textKey2.toPlainText() == ''):
        if ui.textResult.toPlainText() == '':
            ui.textResult.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
            ui.textResult.setText('!!!Enter text and keys!!!')
        else:
            ui.textResult.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")
            ui.textResult.setText(ui.textResult.toPlainText() + '\n' + '!!!Enter text and keys!!!')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()

    ui.resultButton_V.clicked.connect(lambda: resV())
    ui.resultButton_W.clicked.connect(lambda: resW())
    ui.clearButton.clicked.connect(lambda: clear())
    sys.exit(app.exec_())